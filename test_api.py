'''
from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
resp = client.models.list()
print(resp.data[0].id)
'''

from openai import OpenAI

client = OpenAI(api_key="sk-erwu8G5WMUfrUUusMV1yziyVru5uoUED0B7H8TRBcu4ClJ9i")
resp = client.models.list()
print(resp.data[0].id)