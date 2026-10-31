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
