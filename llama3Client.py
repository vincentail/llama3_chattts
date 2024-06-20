import requests


class Llama3Client:
    def __init__(self,llamaUrl,model='llama3'):
        self.model = model
        self.api = llamaUrl
        self.messages = []

    
    def init(self):
        self.chat_with_llama3('后面所有的内容都用中文回复，并且不要带表情,特殊符号等内容')
    

    def chat_with_llama3(self,content):
        self.messages.append({
            'role':'user',
            'content':content
        })
        data = {
            'model': self.model,
            'stream': False,
            'messages': self.messages
        }
        try:
            response = requests.post(self.api, json=data, timeout=30)
            response.raise_for_status()  # 如果响应状态码不是200，抛出异常
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except requests.exceptions.ConnectionError as conn_err:
            print(f'Connection error occurred: {conn_err}')
        except requests.exceptions.Timeout as timeout_err:
            print(f'Timeout error occurred: {timeout_err}')
        except requests.exceptions.RequestException as req_err:
            print(f'An error occurred: {req_err}')
        else:
            # 请求成功
            print('Request was successful')
            print(response.json())
            data=response.json()
            self.messages.append(data.get('message'))
            return data.get('message', {}).get('content', None)