# scilifelab-hackathon-20261201
Template repo for the AI Hackathon on 2026-12-01: https://www.scilifelab.se/event/hackathon-ai-agents-transforming-life-sciences-medicine-and-healthcare/

> **Participants:** fork this repo and fill in the sections below.

This is a very basic repo to help you get started. Feel free to change anything about it, but please follow the structure for presentation and the project description in the readme file.

The technical part is on you.

## Team

**Team name:** _TBD_

| Name | Affiliation | GitHub |
|------|-------------|--------|
|      |             |        |

## Project description

_What problem are you solving, who is it for, and how do AI agents help? (2–5 sentences)_

## How to run



```bash
# install uv: https://docs.astral.sh/uv/getting-started/installation/
uv sync                   # create .venv and install dependencies
cp .env.example .env      # add the API keys from the organizers
uv run check_keys.py      # verify the keys work
```

### API keys

The organizers provide keys for two services. Put them in `.env`, which git ignores, so never commit it:

| Variable | What it is |
|----------|------------|
| `OPENAI_API_KEY` | OpenAI API key |
| `OPENLLM_API_KEY` | API key for [SciLifeLab Open LLM](https://openllm.scilifelab.se/) (an OpenAI-compatible API) |
| `OPENLLM_BASE_URL` | Open LLM API address. Keep the default |
| `OPENLLM_MODEL` | Optional. The Open LLM model `check_keys.py` tests with. If empty, it uses the first available model |

`check_keys.py` prints `[OK]`, `[FAIL]` or `[SKIP]` for each service. In your code, load the keys with `python-dotenv`:

## Results / demo

_Screenshot, GIF, or link to a demo video._

## Presentation

Put your slides in [`presentation/`](presentation/) — a PDF is preferred. If the slides live online, add the link to [`presentation/README.md`](presentation/README.md).
