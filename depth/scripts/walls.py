#!/usr/bin/env python3
"""Honest three-tier wall-busting ladder doctor.

Checks what is actually usable: headless browser (tier 1), the user's real
signed-in browser via OpenCLI (tier 2), and API computer-use keys (tier 3).
A binary existing is not readiness; each tier reports 'ready', 'installable',
or 'unavailable' with a reason. Exit 0 when at least one tier is ready.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil

import browser_read

TIERS = ('headless', 'real_browser', 'api_computer')


def tools_prefix(env):
    value = env.get('DEPTH_TOOLS_PREFIX')
    return Path(value).expanduser() if value else Path.home() / '.local/share/depthengine/tools'


def headless_status(env):
    prefix = tools_prefix(env)
    candidates = [env.get('DEPTH_AGENT_BROWSER'), shutil.which('agent-browser'),
                  str(prefix / 'node_modules/.bin/agent-browser')]
    for candidate in candidates:
        if candidate and Path(candidate).is_file() and os.access(candidate, os.X_OK):
            return {'status': 'ready', 'via': candidate}
    if shutil.which('playwright-cli') or shutil.which('npx'):
        return {'status': 'installable',
                'reason': 'agent-browser not found; playwright-cli or npx present — run scripts/tooling.py setup-browser or install playwright-cli'}
    return {'status': 'unavailable', 'reason': 'no headless browser tooling found'}


def real_browser_status(env):
    explicit = env.get('DEPTH_OPENCLI_PACKAGE')
    try:
        node, root, main, doctor_file = browser_read.resolve_package(explicit or None)
        health = browser_read.doctor(root)
        if health.get('status') == 'ready':
            return {'status': 'ready', 'via': str(root),
                    'scope': 'Synthetic bridge probe only; no website login qualification'}
        return {'status': 'installable', 'via': str(root),
                'reason': 'OpenCLI installed but bridge not healthy: ' + json.dumps(health)}
    except ValueError as error:
        return {'status': 'unavailable', 'reason': str(error)}


def api_status(env):
    keys = {name: bool(env.get(name)) for name in ('ANTHROPIC_API_KEY', 'OPENAI_API_KEY')}
    if any(keys.values()):
        return {'status': 'configured', 'configured': [k for k, v in keys.items() if v],
                'scope': 'Key presence only; no tier-3 adapter is bundled — a host-native computer-use tool or a custom caller is required. Validity, plan, and rate limits are not checked'}
    return {'status': 'unavailable', 'reason': 'neither ANTHROPIC_API_KEY nor OPENAI_API_KEY is set'}


def doctor(env=None, overrides=None):
    env = dict(os.environ if env is None else env)
    statuses = {
        'headless': headless_status(env),
        'real_browser': real_browser_status(env),
        'api_computer': api_status(env),
    }
    if overrides:
        for key, value in overrides.items():
            if key in statuses:
                statuses[key] = value
    ready = [name for name in TIERS if statuses[name].get('status') == 'ready']
    recommended = ready[0] if ready else None
    return {
        'status': 'ready' if ready else 'none_ready',
        'recommended_tier': recommended,
        'ready_tiers': ready,
        'tiers': statuses,
        'ladder': ['headless (ordinary pages)', 'real_browser (login walls)',
                   'api_computer (captcha-heavy walls; a key alone is not readiness — no tier-3 adapter is bundled)'],
        'honest_note': 'Doctor verifies what exists; each wall still requires an actual attempt.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('doctor', 'ladder'))
    args = parser.parse_args()
    if args.command == 'ladder':
        print(json.dumps(doctor()['ladder'], indent=2))
        return 0
    result = doctor()
    print(json.dumps(result, indent=2))
    return 0 if result['status'] == 'ready' else 1


if __name__ == '__main__':
    raise SystemExit(main())
