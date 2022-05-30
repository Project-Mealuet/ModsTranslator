from sys import argv, exit

from PyQt6.QtWidgets import QApplication

from run.progress import progress
from run.translator import jarTranslation

if __name__ == '__main__':
    app = QApplication(argv)
    UI_Translator = None


    def showTranslator(authBack):
        global UI_Translator
        UI_Translator = jarTranslation(authBack)
        UI_Progress.close()
        UI_Translator.show()


    UI_Progress = progress()
    UI_Progress.trigger.connect(showTranslator)
    UI_Progress.show()
    UI_Progress.run()

    exit(app.exec())
