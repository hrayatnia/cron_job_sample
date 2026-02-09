from datetime import datetime, timezone

from src.main import run_job


def test_run_job_returns_expected_message_and_timestamp() -> None:
    fixed = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    result = run_job(lambda: fixed)

    assert result.timestamp == fixed
    assert result.message == "[2024-01-01T12:00:00+00:00]: - Hello World"
