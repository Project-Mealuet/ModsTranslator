from json import load

from PyQt6.QtCore import QThread, pyqtSignal
from requests import post


class progress_API_access(QThread):
    trigger = pyqtSignal(bool)
    errorType = pyqtSignal(str)
    authBack = pyqtSignal(str)

    def __init__(self):
        super(progress_API_access, self).__init__()

    def run(self) -> None:
        configFile = open('config.json', 'r', encoding='UTF-8')
        authInfo = load(configFile)
        configFile.close()
        authHost = 'https://aip.baidubce.com/oauth/2.0/token'
        authData = {
            'grant_type': 'client_credentials',
            'client_id': authInfo['client_id'],
            'client_secret': authInfo['client_secret']
        }
        authResponse = post(authHost, authData)
        if authResponse.status_code != 200:
            self.trigger.emit(False)
            self.errorType.emit('网络错误: 请检查网络是否正常连接或关闭代理服务')
            return
        if 'error' in authResponse.json().keys():
            self.trigger.emit(False)
            self.errorType.emit('鉴权错误: ' + authResponse.json()['error_description'])
            return
        self.trigger.emit(True)
        self.authBack.emit(authResponse.json()['access_token'])
