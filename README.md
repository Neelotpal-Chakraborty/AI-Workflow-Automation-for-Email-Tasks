# AI Workflow Automation for Email & Tasks (Flask + Postgres)

## Features
- Poll IMAP for unseen emails
- LLM-based classification and action planning
- Actions: REPLY (SMTP), TASK (Trello), SCHEDULE (stub)
- Background scheduler (APScheduler)
- REST API under `/api/*`

## Quick Start
```bash
cp .env.example .env
# edit .env with IMAP/SMTP and (optionally) OPENAI key

docker-compose up --build
# API: http://localhost:8000
# Health: GET /health

# Manual triggers:
curl -X POST http://localhost:8000/api/agent/ingest
curl -X POST http://localhost:8000/api/agent/process
curl -X POST http://localhost:8000/api/agent/execute
