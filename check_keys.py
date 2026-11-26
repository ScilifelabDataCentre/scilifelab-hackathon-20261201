"""Check that the API keys in .env work: lists models and sends a short prompt."""
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def check(name, api_key, base_url=None, model=None):
    if not api_key:
        print(f"[SKIP] {name}: no API key set")
        return False
    try:
        client = OpenAI(api_key=api_key, base_url=base_url)
        models = [m.id for m in client.models.list().data]
        model = model or models[0]
        reply = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "Reply with the single word: OK"}],
            max_tokens=5,
        )
        print(f"[OK]   {name}: {len(models)} models available; {model} replied "
              f"{reply.choices[0].message.content.strip()!r}")
        return True
    except Exception as e:
        print(f"[FAIL] {name}: {type(e).__name__}: {e}")
        return False


results = [
    check("OpenAI", os.getenv("OPENAI_API_KEY"), model="gpt-4o-mini"),
    check("Open LLM", os.getenv("OPENLLM_API_KEY"),
          base_url=os.getenv("OPENLLM_BASE_URL", "https://openllm.scilifelab.se/api"),
          model=os.getenv("OPENLLM_MODEL") or None),
]
sys.exit(0 if all(results) else 1)
