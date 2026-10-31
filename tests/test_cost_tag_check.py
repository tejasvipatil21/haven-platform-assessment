from pathlib import Path

from scripts.cost_tag_check import check_plan


PLAN = Path(__file__).resolve().parents[1] / "fixtures" / "plan.json"


def test_fixture_reports_only_missing_tags(capsys):
    result = check_plan(PLAN)
    output = capsys.readouterr().out

    assert result == 1
    assert "listing_media" in output
    assert "mls_feed_sync" in output
    assert "landlord_media[0]" not in output
    assert "screening_report_export" not in output


def test_repeated_check_has_same_output_without_duplicates(capsys):
    first_result = check_plan(PLAN)
    first_output = capsys.readouterr().out

    second_result = check_plan(PLAN)
    second_output = capsys.readouterr().out

    assert first_result == second_result == 1
    assert first_output == second_output
    assert first_output.count("listing_media") == 1
    assert first_output.count("mls_feed_sync") == 1
