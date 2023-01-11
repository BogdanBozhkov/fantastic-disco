import os
import openai
import base64
import time

openai.api_key = "sk-NYRrDSU5U64jLzFVVlbbTsT3BlbkFJBFYCf5z7vGXA4tjYD3rN"

response = openai.Image.create(
    prompt = "red apple",
    n=1,
    size="1024x1024",
    response_format = "b64_json"
)

print(response)

for i in range(0, len(response['data'])):
    b64 = response['data'][i]['b64_json']
    filename = f'image_{int(time.time())}_{i}.png'
    print("Saving file" + filename)
    with open(f'image_{i}.png', 'wb') as f:
        f.write(base64.urlsafe_b64decode(b64))
