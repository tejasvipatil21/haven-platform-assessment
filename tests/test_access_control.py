"""
Write tests here proving:
  1. A PropertyManager scoped to la-001 (pm-001) is DENIED access to la-002's tenant's
     screening report (rep-002).
  2. The same PropertyManager (pm-001) IS allowed access to their own account's screening
     report (rep-001).

Use the `property_managers`, `properties`, `tenants`, and `screening_reports` fixtures from
conftest.py — don't re-invent the seed data here.
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

def test_empty_account_ids_denied(
    property_managers, screening_reports, tenants, properties
):
    from dataclasses import replace

    report = screening_reports[0]
    tenant = next(t for t in tenants if t.id==report.tenant_id)
    property_record = next(p for p in properties if p.id==tenant.property_id)

    manager = replace(property_managers[0], landlord_account_id="")
    empty_property = replace(property_record, landlord_account_id="")

    assert not can_access_screening_report(
	manager, report, properties=[empty_property], tenants=tenants
   )
