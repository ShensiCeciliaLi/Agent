from openai import OpenAI

client = OpenAI(
    api_key="sk-erwu8G5WMUfrUUusMV1yziyVru5uoUED0B7H8TRBcu4ClJ9i",
    base_url="https://hkucvm.dynv6.net/v1"  # 示例
)

# 调用 Embedding 模型
response = client.embeddings.create(
    model="Qwen3-Embedding-8B",
    input="这是一个测试"
)

print("向量维度:", len(response.data[0].embedding))