from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Callable


@dataclass(frozen=True)
class JobResult:
    timestamp: datetime
    message: str


def run_job(now_fn: Callable[[], datetime] | None = None) -> JobResult:
    now_fn = now_fn or (lambda: datetime.now(timezone.utc))
    ts = now_fn()
    return JobResult(timestamp=ts, message=f"[{ts.isoformat()}]: - Hello World")


def main() -> None:
    result = run_job()
    print(result.message)


if __name__ == "__main__":
    main()
