from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "<Your_API_key>"

client = OpenAI(base_url="https://hkucvm.dynv6.net/v1")

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "Please explain what a large language model is?"}
]

response = client.chat.completions.create(
    model="Qwen3-Coder-480B-A35B-Instruct-FP8",
    messages=messages,
    temperature=0.6,
    top_p=0.8,
    timeout=120,
    extra_body={
        "chat_template_kwargs": {"enable_thinking": False}  # 必须加
    }
)

print(response.choices[0].message.content)