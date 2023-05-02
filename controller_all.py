from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def wecome():
    return ""


@app.route('/getData', methods=['POST'])
def login_api():
    data=request.json
    # return backend_login(data['username'], data['password'])






if __name__ == "__main__":
    app.run(debug=True, port=7000)