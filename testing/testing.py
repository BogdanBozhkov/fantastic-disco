import os
import openai
import base64

openai.api_key = "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"

response = openai.Image.create(
    prompt = "red apple",
    n=2,
    size="1024x1024",
)

print(response)
