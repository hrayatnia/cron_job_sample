# Cron Job Sample

A tiny Python project that prints a timestamped message. The job is designed to
be run on a schedule (local cron, container, or CI scheduler).

## Local run

```bash
python -m src.main
```

## Tests

```bash
pytest
```

## Docker

Build:

```bash
docker build -t cron-job-sample .
```

Run once:

```bash
docker run --rm cron-job-sample
```

## CI/CD schedule

The GitHub Actions workflow includes a cron schedule. GitHub only guarantees a
minimum 5-minute schedule interval; a `* * * * *` expression will still run at
best every 5 minutes in practice. If you need true 1-minute cadence, use an
external scheduler or a self-hosted runner with system cron.
