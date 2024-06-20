from ttsClient import TTSClient
from llama3Client import Llama3Client

ttsClient = TTSClient('http://localhost:8080/',seed=20)
ttsClient.init()
llaClient = Llama3Client('http://localhost:11434/api/chat')
llaClient.init()

while(True):
    user_input = input("you:>>")
    if not user_input.strip():
        print("请输入内容哦!")
    elif user_input == 'bye':
        ttsClient.generateVoice('再见哦，很期待和你的下次交谈')
        ttsClient.close()
    else:
        response = llaClient.chat_with_llama3(user_input)
        print('AI :>> ',response)
        ttsClient.generateVoice(response)