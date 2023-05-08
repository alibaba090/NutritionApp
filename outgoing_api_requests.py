import requests
import json
from decouple import config


def chat_gpt_completions(content_value):
    url = "https://api.openai.com/v1/chat/completions"
    token = config('OPEN_API_KEY', default='')

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
        'Authorization': 'Bearer ' + token
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    return response
