from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMessageBox, QMainWindow

from run.threads.progress_API_access import progress_API_access
from run.threads.progress_config_exist import progress_config_exist
from ui.Create import Ui_Dialog


class progress(Ui_Dialog, QMainWindow):
    trigger = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.progressBar.setRange(0, 2)
        self.configExist = progress_config_exist()
        self.configExist.trigger.connect(self.setConfigStatus)
        self.APIAccess = progress_API_access()
        self.APIAccess.trigger.connect(self.setAPIStatus)
        self.APIAccess.errorType.connect(self.setAPIErrorType)
        self.APIAccess.authBack.connect(self.setAuthToken)

    def setConfigStatus(self, status):
        self.progressBar.setValue(1)
        if not status:
            QMessageBox.critical(self, '错误', 'config文件不存在，已重新创建，请填写后重新打开应用', QMessageBox.StandardButton.Ok)
            return
        self.progressBar.setValue(2)
        self.progressLabel.setText('API鉴权中...')
        self.APIAccess.start()
        self.APIAccess.wait()

    def setAPIStatus(self, status):
        if status:
            self.progressLabel.setText('API鉴权...OK')

    def setAPIErrorType(self, errorType):
        QMessageBox.critical(self, '错误', errorType, QMessageBox.StandardButton.Ok)

    def setAuthToken(self, authBack):
        self.trigger.emit(authBack)

    def run(self):
        self.progressLabel.setText('检查config是否存在...')
        self.configExist.start()
        self.configExist.wait()
