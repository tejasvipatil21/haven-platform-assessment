**********************
Windows PowerShell transcript start
Start time: 20261031180244
Username: TEJASVI-PATIL\HP
RunAs User: TEJASVI-PATIL\HP
Configuration Name: 
Machine: TEJASVI-PATIL (Microsoft Windows NT 10.0.26200.0)
Host Application: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
Process ID: 11636
PSVersion: 5.1.26100.9711
PSEdition: Desktop
PSCompatibleVersions: 1.0, 2.0, 3.0, 4.0, 5.0, 5.1.26100.9711
BuildVersion: 10.0.26100.9711
CLRVersion: 4.0.30319.42000
WSManStackVersion: 3.0
PSRemotingProtocolVersion: 2.3
SerializationVersion: 1.1.0.1
**********************
Transcript started, output file is TERMINAL_LOG.md
PS C:\Users\HP\haven-platform-assessment> python --version

PS C:\Users\HP\haven-platform-assessment> terraform version

PS C:\Users\HP\haven-platform-assessment> python -m pytest -v

PS C:\Users\HP\haven-platform-assessment> python scripts/cost_tag_check.py fixtures/plan.json

PS C:\Users\HP\haven-platform-assessment> python scripts/cost_tag_check.py fixtures/plan.json

PS C:\Users\HP\haven-platform-assessment> Stop-Transcript
**********************
Windows PowerShell transcript end
End time: 20261031180437
**********************
**********************
Windows PowerShell transcript start
Start time: 20261031181959
Username: TEJASVI-PATIL\HP
RunAs User: TEJASVI-PATIL\HP
Configuration Name: 
Machine: TEJASVI-PATIL (Microsoft Windows NT 10.0.26200.0)
Host Application: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
Process ID: 11636
PSVersion: 5.1.26100.9711
PSEdition: Desktop
PSCompatibleVersions: 1.0, 2.0, 3.0, 4.0, 5.0, 5.1.26100.9711
BuildVersion: 10.0.26100.9711
CLRVersion: 4.0.30319.42000
WSManStackVersion: 3.0
PSRemotingProtocolVersion: 2.3
SerializationVersion: 1.1.0.1
**********************
Transcript started, output file is TERMINAL_LOG.md
PS C:\Users\HP\haven-platform-assessment> python -m pytest -v

PS C:\Users\HP\haven-platform-assessment> notepad DESIGN_NOTES.md
PS C:\Users\HP\haven-platform-assessment> Get-Content scripts/cost_tag_check.py
"""
B2, part 2 â€” implement the cost-tagging check.

Read fixtures/plan.json for the shape of a `terraform show -json` plan: a `resource_changes`
list, where each entry has a `type`, an `address`, and `change.after.tags`.

Implement check_plan() so it:
  - Looks at every resource being created or changed (skip anything not in
    change.actions, e.g. a pure "no-op" / "read" change).
  - Fails (returns a non-zero exit code) if the resource is missing the tag that identifies
    the real billing unit, per README.md's domain model â€” not whatever tag the resource
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










PS C:\Users\HP\haven-platform-assessment> Get-Content DESIGN_NOTES.md
# Design Notes

## B2 â€” idempotency key

State exactly what key your `cost_tag_check.py` uses to decide a plan has already been
checked/reported on. Use the word "idempotency" in your explanation.

<!-- Your answer here -->

## Any other decision with a non-obvious alternative


##Access boundary
A manager can view screening report only when the tenant's property's lanlord_account
_id matches the manager's lanlord_account_id. Missing tenants or properties are denied.


##Idempotency key
The checker use the Terraform resources address as deduplication key within a run . It has no persistent cross-run key or state. Rechecking an unchanged plan produces the same sortes ouptuts; it does not create tags or findings.


##Assunptions and trade-offs
The checkers examines resources with create or update actions. It treats a missing or empty lanlord_account_id as a finding. This generic approach can report resources that do not support tags; a production version should use provider schema information to identify taggable resources types.


##AI Correction
The AI initially suggested a Powershell Terraform command whose quoting failed. I corrected it by using TF_VAR_landlord-accounts to pass the list, then ran the plan again
PS C:\Users\HP\haven-platform-assessment> notepad DESIGN_NOTES.md
PS C:\Users\HP\haven-platform-assessment> git status --short

PS C:\Users\HP\haven-platform-assessment> Get-ChildItem -Force .ai-conversation
Get-ChildItem : Cannot find path 'C:\Users\HP\haven-platform-assessment\.ai-conversation' because it does not exist.
At line:1 char:1
+ Get-ChildItem -Force .ai-conversation
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\HP\hav...ai-conversation:String) [Get-ChildItem], 
ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.GetChildItemCommand
Get-ChildItem : Cannot find path 'C:\Users\HP\haven-platform-assessment\.ai-conversation' because it does
not exist.
At line:1 char:1
+ Get-ChildItem -Force .ai-conversation
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\HP\hav...ai-conversation:String) [Get-ChildItem], It
   emNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.GetChildItemCommand

PS C:\Users\HP\haven-platform-assessment> Get-ChildItem -Force .ai-conversations


    Directory: C:\Users\HP\haven-platform-assessment\.ai-conversations


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        31-10-2026     02:18              0 .gitkeep


PS C:\Users\HP\haven-platform-assessment> notepad .ai-conversations\b2-conversation.md
PS C:\Users\HP\haven-platform-assessment> Get-Content .ai-conversations\b2-conversation.md
PS C:\Users\HP\haven-platform-assessment> notepad .ai-conversations\b2-conversation.md
PS C:\Users\HP\haven-platform-assessment> Get-Content .ai-conversations\b2-conversation.md
\# Partial B2 A1 conversation



The full chat was unavailable. These are excerpts, not complete trasnscript.



Assistant: I was too certain that persistent tracking is required. Repeated identical results may be sufficient for idempotency; we need exact B@ wording before changing checker.



Assistant: The wording confirms that \*\*Idempotency means the same result on an unchanged plan\*\*. Persistent tracking is not required. My earlier claim was worng.

PS C:\Users\HP\haven-platform-assessment> git status --short

PS C:\Users\HP\haven-platform-assessment> git --no pager diff

PS C:\Users\HP\haven-platform-assessment> git --no-pager diff

PS C:\Users\HP\haven-platform-assessment> git --no-pager diff --app/access_control.py scripts/cost_tag_check.py tests/test_access

PS C:\Users\HP\haven-platform-assessment> git --no-pager diff --app/access_control.py scripts/cost_tag_check.py tests/test_access_control.py tests/test_cost_tag_check.py

PS C:\Users\HP\haven-platform-assessment> git --no-pager diff

PS C:\Users\HP\haven-platform-assessment> git --no-pager diff --app/access_control.py scripts/cost_tag_check.py

PS C:\Users\HP\haven-platform-assessment> git --no-pager diff --app/access_control.py --scripts/cost_tag_check.py

PS C:\Users\HP\haven-platform-assessment> git --no-pager diff

PS C:\Users\HP\haven-platform-assessment> Get-Content app/access_control.py
"""
B2, part 1 â€” implement can_access_screening_report().

Read README.md's domain model first. A ScreeningReport belongs to a Tenant, a Tenant belongs to
a Property, and a Property belongs to a LandlordAccount. A PropertyManager is scoped to exactly
one LandlordAccount.

Work out from that hierarchy which boundary actually gates access to a ScreeningReport.
"""
from app.models import PropertyManager, ScreeningReport, Property, Tenant


def can_access_screening_report(
    actor: PropertyManager,
    report: ScreeningReport,
    *,
    properties: list[Property],
    tenants: list[Tenant],
) -> bool:
    """
    actor: the PropertyManager requesting access
    report: the ScreeningReport they're trying to view
    properties: all known Property records
    tenants: all known Tenant records

    Return True if actor may view report, False otherwise. Fail closed â€” if anything needed to
    make this determination is missing (tenant not found, property not found), return False.
    """
    tenant = next((t for t in tenants if t.id==report.tenant_id), None)
    if tenant is None:
       return False

    property_record = next((p for p in properties if p.id == tenant.property_id), None)
    if property_record is None:
        return False

    return property_record.landlord_account_id==actor.landlord_account_id
PS C:\Users\HP\haven-platform-assessment> Get-Content app/models.py
"""
Haven's tenancy model. Read README.md for how these fit together before you touch
access_control.py or cost_tag_check.py.

    LandlordAccount (billing unit)
      -> Property
           -> Tenant
                -> ScreeningReport

    PropertyManager is scoped to exactly one LandlordAccount.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class LandlordAccount:
    id: str
    name: str


@dataclass(frozen=True)
class Property:
    id: str
    landlord_account_id: str
    address: str


@dataclass(frozen=True)
class PropertyManager:
    id: str
    name: str
    landlord_account_id: str


@dataclass(frozen=True)
class Tenant:
    id: str
    name: str
    property_id: str


@dataclass(frozen=True)
class ScreeningReport:
    id: str
    tenant_id: str
    ssn_last4: str
    credit_score: int
PS C:\Users\HP\haven-platform-assessment> Get-Content app/access_control.py
"""
B2, part 1 â€” implement can_access_screening_report().

Read README.md's domain model first. A ScreeningReport belongs to a Tenant, a Tenant belongs to
a Property, and a Property belongs to a LandlordAccount. A PropertyManager is scoped to exactly
one LandlordAccount.

Work out from that hierarchy which boundary actually gates access to a ScreeningReport.
"""
from app.models import PropertyManager, ScreeningReport, Property, Tenant


def can_access_screening_report(
    actor: PropertyManager,
    report: ScreeningReport,
    *,
    properties: list[Property],
    tenants: list[Tenant],
) -> bool:
    """
    actor: the PropertyManager requesting access
    report: the ScreeningReport they're trying to view
    properties: all known Property records
    tenants: all known Tenant records

    Return True if actor may view report, False otherwise. Fail closed â€” if anything needed to
    make this determination is missing (tenant not found, property not found), return False.
    """
    tenant = next((t for t in tenants if t.id==report.tenant_id), None)
    if tenant is None:
       return False

    property_record = next((p for p in properties if p.id == tenant.property_id), None)
    if property_record is None:
        return False

    return property_record.landlord_account_id==actor.landlord_account_id
PS C:\Users\HP\haven-platform-assessment> notrpad app/access_control.py
notrpad : The term 'notrpad' is not recognized as the name of a cmdlet, function, script file, or operable program. 
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ notrpad app/access_control.py
+ ~~~~~~~
    + CategoryInfo          : ObjectNotFound: (notrpad:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
notrpad : The term 'notrpad' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the
name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ notrpad app/access_control.py
+ ~~~~~~~
    + CategoryInfo          : ObjectNotFound: (notrpad:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\HP\haven-platform-assessment> notepad app/access_control.py
PS C:\Users\HP\haven-platform-assessment> python -m pytest tests/test_access_control.py -v

PS C:\Users\HP\haven-platform-assessment> Get-Content tests/test_access_control.py
"""
Write tests here proving:
  1. A PropertyManager scoped to la-001 (pm-001) is DENIED access to la-002's tenant's
     screening report (rep-002).
  2. The same PropertyManager (pm-001) IS allowed access to their own account's screening
     report (rep-001).

Use the `property_managers`, `properties`, `tenants`, and `screening_reports` fixtures from
conftest.py â€” don't re-invent the seed data here.
"""
from app.access_control import can_access_screening_report

def test_same_Account_allowed(property_managers, screening_reports, tenants, properties):
    assert can_access_screening_report(
	property_managers[0], screening_reports[0], properties=properties, tenants=tenants
    )


def test_cross_account_denied(property_managers, screening_reports, tenants, properties):
    assert not can_access_screening_report(
	property_managers[0], screening_reports[1], properties=properties, tenants=tenants
    )
PS C:\Users\HP\haven-platform-assessment> notepad tests/test_access_control.py
PS C:\Users\HP\haven-platform-assessment> python -m pytest -v

PS C:\Users\HP\haven-platform-assessment> notepad tests/test_access_control.py
PS C:\Users\HP\haven-platform-assessment> python -m pytest -v

PS C:\Users\HP\haven-platform-assessment> notepad tests/test_access_control.py
PS C:\Users\HP\haven-platform-assessment> python -m pytest -v

PS C:\Users\HP\haven-platform-assessment> Start-transcript -Path TERMINAL_LOG.md -Append
Transcript started, output file is TERMINAL_LOG.md
PS C:\Users\HP\haven-platform-assessment> python -m pytest -v

PS C:\Users\HP\haven-platform-assessment> Stop-Transcript
Transcript stopped, output file is C:\Users\HP\haven-platform-assessment\TERMINAL_LOG.md
PS C:\Users\HP\haven-platform-assessment> git status --short

PS C:\Users\HP\haven-platform-assessment> git diff --check

PS C:\Users\HP\haven-platform-assessment> notepad scripts/cost_tag_check.py
PS C:\Users\HP\haven-platform-assessment> git diff --check

PS C:\Users\HP\haven-platform-assessment> python -m pytest -v

PS C:\Users\HP\haven-platform-assessment> git status --short

PS C:\Users\HP\haven-platform-assessment> Get-Content B1.md
# B1 â€” The Glacier cost gotcha

Assuming 	Glacier Flexible Retrival, deleting after 10 days incurs a charge for the remaining 80 days of its 90-day minimum, plus applicable transition and metadata charges.

I'd keep short lived photos in s3 Standard and archive only those likely to remain long enough to benefit. I'd still honor deletion requests immediately and monitor early-deletion costs.
PS C:\Users\HP\haven-platform-assessment> Get-Content -Encoding UTF8 DESIGN_NOTES,md
Get-Content : Cannot find path 'C:\Users\HP\haven-platform-assessment\DESIGN_NOTES' because it does not exist.
At line:1 char:1
+ Get-Content -Encoding UTF8 DESIGN_NOTES,md
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\HP\hav...nt\DESIGN_NOTES:String) [Get-Content], 
ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.GetContentCommand
Get-Content : Cannot find path 'C:\Users\HP\haven-platform-assessment\DESIGN_NOTES' because it does not exist.
At line:1 char:1
+ Get-Content -Encoding UTF8 DESIGN_NOTES,md
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\HP\hav...nt\DESIGN_NOTES:String) [Get-Content], ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.GetContentCommand

Get-Content : Cannot find path 'C:\Users\HP\haven-platform-assessment\md' because it does not exist.
At line:1 char:1
+ Get-Content -Encoding UTF8 DESIGN_NOTES,md
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\HP\haven-platform-assessment\md:String) [Get-Content], 
ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.GetContentCommand
Get-Content : Cannot find path 'C:\Users\HP\haven-platform-assessment\md' because it does not exist.
At line:1 char:1
+ Get-Content -Encoding UTF8 DESIGN_NOTES,md
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\HP\haven-platform-assessment\md:String) [Get-Content], ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.GetContentCommand

PS C:\Users\HP\haven-platform-assessment> Get-Content -Encoding UTF8 DESIGN_NOTES.md
# Design Notes

## B2 — idempotency key
The checker uses the Terraform resource address to deduplicate findings within
a run. It has no persistent cross-run key or state. An unchanged plan produces
the same sorted output and exit code on repeated runs.


## Access boundary

A manager can view a screening report only when the tenant's property's
`landlord_account_id` matches the manager's `landlord_account_id`. Missing
tenants or properties are denied.

## Assumptions and trade-offs

The checker examines resources with create or update actions. It treats a
missing or empty `landlord_account_id` as a finding. This may flag resources
that do not support tags. A production version should use provider schema
information to identify taggable resource types.

## AI correction

The AI initially suggested a PowerShell Terraform command whose quoting failed.
I used `TF_VAR_landlord_accounts` to pass the list and ran the plan again.
PS C:\Users\HP\haven-platform-assessment> Get-Content README.md
# Haven â€” Platform Infrastructure Assessment

Haven is a multi-tenant real estate platform.

## Domain model

```
LandlordAccount  (the billing unit)
  â””â”€â”€ Property
        â””â”€â”€ Tenant
              â””â”€â”€ ScreeningReport  (SSN, credit score)

PropertyManager  (scoped to exactly one LandlordAccount)
```

A `LandlordAccount` is the billing unit â€” every property, every tenant, every report underneath
it rolls up to exactly one. A `PropertyManager` is scoped to exactly one `LandlordAccount` and
everything under it.

This codebase currently tags and checks access using whatever ID happened to be on hand when
each piece was written â€” that reflects how it was built, not a spec to replicate.

## What not to modify

`app/seed_data.py`, `app/models.py`, `fixtures/plan.json`, `terraform/terraform.tfstate` â€” the
assignment's checks assume this data is unchanged.

`terraform/terraform.tfstate` is checked in deliberately, not an accident â€” it's a seeded state
representing 4 already-provisioned landlord media buckets, standing in for a real AWS account so
B0 can be reproduced with `terraform plan` instead of just reasoned about. See `terraform/main.tf`
for how to use it.

## Where things are

| Path | Task |
|---|---|
| `terraform/main.tf` | B0 |
| `terraform/lifecycle.tf` | B1 |
| `app/access_control.py`, `scripts/cost_tag_check.py` | B2 â€” stubs to implement |
PS C:\Users\HP\haven-platform-assessment> Get-Content README.md -Tail 30
        â””â”€â”€ Tenant
              â””â”€â”€ ScreeningReport  (SSN, credit score)

PropertyManager  (scoped to exactly one LandlordAccount)
```

A `LandlordAccount` is the billing unit â€” every property, every tenant, every report underneath
it rolls up to exactly one. A `PropertyManager` is scoped to exactly one `LandlordAccount` and
everything under it.

This codebase currently tags and checks access using whatever ID happened to be on hand when
each piece was written â€” that reflects how it was built, not a spec to replicate.

## What not to modify

`app/seed_data.py`, `app/models.py`, `fixtures/plan.json`, `terraform/terraform.tfstate` â€” the
assignment's checks assume this data is unchanged.

`terraform/terraform.tfstate` is checked in deliberately, not an accident â€” it's a seeded state
representing 4 already-provisioned landlord media buckets, standing in for a real AWS account so
B0 can be reproduced with `terraform plan` instead of just reasoned about. See `terraform/main.tf`
for how to use it.

## Where things are

| Path | Task |
|---|---|
| `terraform/main.tf` | B0 |
| `terraform/lifecycle.tf` | B1 |
| `app/access_control.py`, `scripts/cost_tag_check.py` | B2 â€” stubs to implement |
PS C:\Users\HP\haven-platform-assessment> Select-String -Path README.md -Pattern 'recording|https?://'
PS C:\Users\HP\haven-platform-assessment> Get-Content TERMINAL_LOG.md -First 30
**********************
Windows PowerShell transcript start
Start time: 20261031180244
Username: TEJASVI-PATIL\HP
RunAs User: TEJASVI-PATIL\HP
Configuration Name:
Machine: TEJASVI-PATIL (Microsoft Windows NT 10.0.26200.0)
Host Application: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
Process ID: 11636
PSVersion: 5.1.26100.9711
PSEdition: Desktop
PSCompatibleVersions: 1.0, 2.0, 3.0, 4.0, 5.0, 5.1.26100.9711
BuildVersion: 10.0.26100.9711
CLRVersion: 4.0.30319.42000
WSManStackVersion: 3.0
PSRemotingProtocolVersion: 2.3
SerializationVersion: 1.1.0.1
**********************
Transcript started, output file is TERMINAL_LOG.md
PS C:\Users\HP\haven-platform-assessment> python --version

PS C:\Users\HP\haven-platform-assessment> terraform version

PS C:\Users\HP\haven-platform-assessment> python -m pytest -v

PS C:\Users\HP\haven-platform-assessment> python scripts/cost_tag_check.py fixtures/plan.json

PS C:\Users\HP\haven-platform-assessment> python scripts/cost_tag_check.py fixtures/plan.json

PS C:\Users\HP\haven-platform-assessment> Stop-Transcript
PS C:\Users\HP\haven-platform-assessment> &{
"Python version:"
python --version
"Terraform version:"
terraform version
"Tests:"
python =m pytest -v
"Cost-tag check, run 1:"
python scripts/cost_tag_check.py fixtures/plan.json
"Cost-tag check, run 2:"
python scripts/cost_tag_check.py fixtures/plan.json
} | Tee-Object -FilePath terminal-output.txt
Python version:
Python 3.13.15
Terraform version:
Terraform v1.16.2
on windows_amd64

Your version of Terraform is out of date! The latest version
is 1.17.1. You can update by downloading from https://developer.hashicorp.com/terraform/install
Tests:
Cost-tag check, run 1:
Missing landlord_account_id: aws_lambda_function.mls_feed_sync
Missing landlord_account_id: aws_s3_bucket.listing_media
Cost-tag check, run 2:
Missing landlord_account_id: aws_lambda_function.mls_feed_sync
Missing landlord_account_id: aws_s3_bucket.listing_media
PS C:\Users\HP\haven-platform-assessment> &{
"Python version:"
python --version
"Terraform version:"
terraform version
"Tests:"
python -m pytest -v
"Cost-tag check, run 1:"
python scripts/cost_tag_check.py fixtures/plan.json
"Cost-tag check, run 2:"
python scripts/cost_tag_check.py fixtures/plan.json
} | Tee-Object -FilePath terminal-output.txt
Python version:
Python 3.13.15
Terraform version:
Terraform v1.16.2
on windows_amd64

Your version of Terraform is out of date! The latest version
is 1.17.1. You can update by downloading from https://developer.hashicorp.com/terraform/install
Tests:
============================= test session starts =============================
platform win32 -- Python 3.13.15, pytest-9.2.0, pluggy-1.7.0 -- C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\HP\haven-platform-assessment
collecting ... collected 5 items

tests/test_access_control.py::test_same_Account_allowed PASSED           [ 20%]
tests/test_access_control.py::test_cross_account_denied PASSED           [ 40%]
tests/test_access_control.py::test_empty_account_ids_denied PASSED       [ 60%]
tests/test_cost_tag_check.py::test_fixture_reports_only_missing_tags PASSED [ 80%]
tests/test_cost_tag_check.py::test_repeated_check_has_same_output_without_duplicates PASSED [100%]

============================== 5 passed in 0.08s ==============================
Cost-tag check, run 1:
Missing landlord_account_id: aws_lambda_function.mls_feed_sync
Missing landlord_account_id: aws_s3_bucket.listing_media
Cost-tag check, run 2:
Missing landlord_account_id: aws_lambda_function.mls_feed_sync
Missing landlord_account_id: aws_s3_bucket.listing_media
PS C:\Users\HP\haven-platform-assessment> Get-Content terminal-output.txt
Python version:
Python 3.13.15
Terraform version:
Terraform v1.16.2
on windows_amd64

Your version of Terraform is out of date! The latest version
is 1.17.1. You can update by downloading from https://developer.hashicorp.com/terraform/install
Tests:
============================= test session starts =============================
platform win32 -- Python 3.13.15, pytest-9.2.0, pluggy-1.7.0 -- C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\HP\haven-platform-assessment
collecting ... collected 5 items

tests/test_access_control.py::test_same_Account_allowed PASSED           [ 20%]
tests/test_access_control.py::test_cross_account_denied PASSED           [ 40%]
tests/test_access_control.py::test_empty_account_ids_denied PASSED       [ 60%]
tests/test_cost_tag_check.py::test_fixture_reports_only_missing_tags PASSED [ 80%]
tests/test_cost_tag_check.py::test_repeated_check_has_same_output_without_duplicates PASSED [100%]

============================== 5 passed in 0.08s ==============================
Cost-tag check, run 1:
Missing landlord_account_id: aws_lambda_function.mls_feed_sync
Missing landlord_account_id: aws_s3_bucket.listing_media
Cost-tag check, run 2:
Missing landlord_account_id: aws_lambda_function.mls_feed_sync
Missing landlord_account_id: aws_s3_bucket.listing_media
PS C:\Users\HP\haven-platform-assessment> Get-Content terminal-output.txt | Add-Content TERMINAL_LOG.md
Add-Content : The process cannot access the file 'C:\Users\HP\haven-platform-assessment\TERMINAL_LOG.md' because it is 
being used by another process.
At line:1 char:35
+ Get-Content terminal-output.txt | Add-Content TERMINAL_LOG.md
+                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : WriteError: (C:\Users\HP\hav...TERMINAL_LOG.md:String) [Add-Content], IOException
    + FullyQualifiedErrorId : GetContentWriterIOError,Microsoft.PowerShell.Commands.AddContentCommand
Add-Content : The process cannot access the file 'C:\Users\HP\haven-platform-assessment\TERMINAL_LOG.md' because it is being used by another
process.
At line:1 char:35
+ Get-Content terminal-output.txt | Add-Content TERMINAL_LOG.md
+                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : WriteError: (C:\Users\HP\hav...TERMINAL_LOG.md:String) [Add-Content], IOException
    + FullyQualifiedErrorId : GetContentWriterIOError,Microsoft.PowerShell.Commands.AddContentCommand

PS C:\Users\HP\haven-platform-assessment> Stop-Transcript
**********************
Windows PowerShell transcript end
End time: 20261031200900
**********************
Python version:
Python 3.13.15
Terraform version:
Terraform v1.16.2
on windows_amd64

Your version of Terraform is out of date! The latest version
is 1.17.1. You can update by downloading from https://developer.hashicorp.com/terraform/install
Tests:
============================= test session starts =============================
platform win32 -- Python 3.13.15, pytest-9.2.0, pluggy-1.7.0 -- C:\Users\HP\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\HP\haven-platform-assessment
collecting ... collected 5 items

tests/test_access_control.py::test_same_Account_allowed PASSED           [ 20%]
tests/test_access_control.py::test_cross_account_denied PASSED           [ 40%]
tests/test_access_control.py::test_empty_account_ids_denied PASSED       [ 60%]
tests/test_cost_tag_check.py::test_fixture_reports_only_missing_tags PASSED [ 80%]
tests/test_cost_tag_check.py::test_repeated_check_has_same_output_without_duplicates PASSED [100%]

============================== 5 passed in 0.08s ==============================
Cost-tag check, run 1:
Missing landlord_account_id: aws_lambda_function.mls_feed_sync
Missing landlord_account_id: aws_s3_bucket.listing_media
Cost-tag check, run 2:
Missing landlord_account_id: aws_lambda_function.mls_feed_sync
Missing landlord_account_id: aws_s3_bucket.listing_media
