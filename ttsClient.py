from gradio_client import Client
import pygame

class TTSClient:
    def __init__(self,ttsServerUrl,temperature=0.3,seed=-1):
        self.ttsServerUrl = ttsServerUrl
        self.seed = seed
        self.temperature = temperature
    
    def init(self):
        self.client = Client(self.ttsServerUrl)
        if self.seed == -1:
            self.__generateSeed()
        # 初始化pygame
        pygame.init()

        # 创建一个pygame窗口（虽然不会显示，但是需要）
        pygame.display.set_mode((0,0))

    def generateVoice(self,text):
        print('generating voice........')
        result = self.client.predict(
            text=text,
            temperature=self.temperature,
            audio_seed_input=self.seed,
            api_name="/generate_audio"
        )
        voicePath = result[0]
        self.__speak(voicePath)
    
    def __speak(self,voicePath):
        sound = pygame.mixer.Sound(voicePath)
        # 播放音频
        pygame.mixer.Sound.play(sound)
        # 等待音频播放完毕
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)

    def __generateSeed(self):
        result = self.client.predict(api_name="/generate_seed")
        self.seed = result['value']

    def close(self):
        # 关闭pygame
        pygame.quit()