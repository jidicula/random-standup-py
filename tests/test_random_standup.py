from click.testing import CliRunner

from datetime import date

from random_standup.standup import standup


def test_standup_cli():
    runner = CliRunner()
    result = runner.invoke(standup, ["example-roster.toml"])
    assert result.exit_code == 0
    assert str(date.today()) in result.output
    assert "## Subteam-1" in result.output
