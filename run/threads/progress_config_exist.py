from json import dump
from os.path import exists

from PyQt6.QtCore import QThread, pyqtSignal


class progress_config_exist(QThread):
    trigger = pyqtSignal(bool)

    def __init__(self):
        super(progress_config_exist, self).__init__()

    def run(self) -> None:
        if not exists('config.json'):
            configFile = open('config.json', 'w', encoding='UTF-8')
            configJson = {
                'client_id': 'Enter your API Key',
                'client_secret': 'Enter your Secret Key'
            }
            dump(configJson, configFile, indent=4)
            configFile.close()
            self.trigger.emit(False)
        else:
            self.trigger.emit(True)
