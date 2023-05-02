import outgoing_api_requests
import backend_repository


def print_hi(name):
    print(f'Hi, {name}')
    outgoing_api_requests.chat_gpt_completions("create a health chart")
    # backend_repository.insert_data()


if __name__ == '__main__':
    print_hi('PyCharm')
