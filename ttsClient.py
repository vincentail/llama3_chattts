import requests
import pygame

class TTSClient:
    def __init__(self,ttsServerUrl,temperature=0.3,seed=-1):
        self.ttsServerUrl = ttsServerUrl
        self.seed = seed
        self.temperature = temperature
    
    def init(self):
        # 初始化pygame
        pygame.init()

        # 创建一个pygame窗口（虽然不会显示，但是需要）
        pygame.display.set_mode((0,0))

    def generateVoice(self,text):
        print('generating voice........')
        res = requests.post(self.ttsServerUrl, data={
            "text": text,
            "prompt": "",
            "voice": self.seed,
            "temperature": self.temperature,
            "top_p": 0.7,
            "top_k": 20,
            "skip_refine": 0,
            "custom_voice": 0
        })
        voicePath=res.json().get('audio_files')[0]('filename')
        self.__speak(voicePath)
    
    def __speak(self,voicePath):
        sound = pygame.mixer.Sound(voicePath)
        # 播放音频
        pygame.mixer.Sound.play(sound)
        # 等待音频播放完毕
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)

    def close(self):
        # 关闭pygame
        pygame.quit()
