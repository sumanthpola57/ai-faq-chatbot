import json
from openai import OpenAI
from app.core.config import GROQ_API_KEY
from app.core.redis_client import redis_client

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def generate_answer(session_id, question):

    history = redis_client.get(session_id)

    if history:
        messages = json.loads(history)
    else:
        messages = [
            {"role": "system", "content": "You are a helpful FAQ assistant"}
        ]

    messages.append({"role": "user", "content": question})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    answer = response.choices[0].message.content

    messages.append({"role": "assistant", "content": answer})

    redis_client.set(session_id, json.dumps(messages))

    return answer