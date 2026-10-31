"""
B2, part 2 — implement the cost-tagging check.

Read fixtures/plan.json for the shape of a `terraform show -json` plan: a `resource_changes`
list, where each entry has a `type`, an `address`, and `change.after.tags`.

Implement check_plan() so it:
  - Looks at every resource being created or changed (skip anything not in
    change.actions, e.g. a pure "no-op" / "read" change).
  - Fails (returns a non-zero exit code) if the resource is missing the tag that identifies
    the real billing unit, per README.md's domain model — not whatever tag the resource
    happens to already carry.
  - Is idempotent: running this twice against the same plan file produces the same result,
    with no duplicate output and no flipped pass/fail.
  - Prints which specific resource address(es) are missing the tag.

Run manually: python scripts/cost_tag_check.py fixtures/plan.json
"""
import json
import sys


def check_plan(plan_path: str) -> int:
    """
    Returns an exit code: 0 if every taggable resource being created/changed has
    `landlord_account_id`, non-zero otherwise.
    """
    try:
        with open(plan_path, encoding="utf-8") as plan_file:
          plan = json.load(plan_file)

        missing = set()
        for resource in plan["resource_changes"]:
          change = resource["change"]
          if not ({"create", "update"} & set (change["actions"])):
             continue

          after = change.get("after") or {}
          tags = after.get("tags") or {}
          if not isinstance(tags, dict) or not tags.get("landlord_account_id"):
              missing.add(resource["address"])

        for address in sorted(missing):
           print(f"Missing landlord_account_id: {address}")
        return 1 if missing else 0
    except (OSerror, ValueError, KeyError, TypeError) as error:
        print(f"Cannot check plan {error}", file=sys.stderr)

        return 2

if __name__ =="__main__":
    sys.exit(check_plan(sys.argv[1]))