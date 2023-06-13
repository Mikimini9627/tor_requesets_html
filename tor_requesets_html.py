import subprocess
import time
import requests

class TorSession:

    # プロキシ
    __proxies = {
            'http':'socks5://127.0.0.1:9050',
            'https':'socks5://127.0.0.1:9050'
            }

    # セッション
    __session = None

    # Torプロセス
    __tor = None

    def __init__(self):

        # セッション生成
        self.__session = requests.Session()

        # Tor実行
        self.__tor = subprocess.Popen(".\\Tor\\tor.exe", shell=False)

        # 少し待機
        time.sleep(10)

    def close(self):
        self.__session.close()

        # Tor停止
        self.__tor.kill()

    def get(self, url : str):
        return self.__session.get(url, proxies = self.__proxies)
    
    def post(self, url : str, data : dict):
        return self.__session.post(url, data = data, proxies = self.__proxies)