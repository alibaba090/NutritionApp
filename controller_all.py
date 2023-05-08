from flask import Flask, jsonify, request
import outgoing_api_requests
import json

app = Flask(__name__)


@app.route('/')
def wecome():
    return ""


@app.route('/nutritionplan', methods=['POST'])
def login_api():
    data = request.json
    id = data['id']
    age = data['age']
    cuisine = data['cuisine']
    allergies = data['allergies']
    diet_type = data['diet']
    gender = data['gender']
    goal = data['goal']

    prompt = "Create a concise 7 day per meal plan for a " + age + " years old " + gender + " with a goal of " + goal + ". "
    if allergies != 'NA':
        prompt = prompt + "Foods should not contain any " + allergies + "."
    prompt = prompt + " Only use foods from " + cuisine + " cuisines."
    prompt = prompt + "Include foods which are strictly in the " + diet_type + " diet."

    print(prompt)

    api_response = outgoing_api_requests.chat_gpt_completions(prompt)
    response_json = json.loads(api_response.text)
    diet_plan = response_json['choices'][0]['message']['content']

    # choices_array = api_response['choices']
    # choice1 = choices_array[0]
    # message = choice1['message']
    # role = message['role']
    # content = message['content']

    # print(content)
    return response_json

    # return backend_login(data['username'], data['password'])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
