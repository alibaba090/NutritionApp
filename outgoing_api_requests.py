import requests
import json


def chat_gpt_completions(content_value):
    url = "https://api.openai.com/v1/chat/completions"

    payload = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": content_value
            }
        ],
        "temperature": 0.7
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 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'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
