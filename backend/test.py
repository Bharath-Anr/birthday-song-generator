import requests

# Chat Completions (POST /v1/chat/completions)
response = requests.post(
  "https://api.sarvam.ai/v1/chat/completions",
  headers={
    "api-subscription-key": "sk_zx28olbd_glswkKZVr78wLKimu0IrpRZN"
  },
  json={
    "messages": [
      {
        "content": "Tell me a joke",
        "role": "user"
      }
    ],
    "model": "sarvam-m"
  },
)

od=response.json()
content=od["choices"][0]["message"]["content"]
print(content)