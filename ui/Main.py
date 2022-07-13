from dataclasses import dataclass
from os import environ
from dotenv import load_dotenv
from main import Sepyre
import app

load_dotenv()

ENVIRONMENT = environ['ENVIRONMENT']


@dataclass()
class MainWindow(app.qt.QMainWindow):
    main: Sepyre

    def __post_init__(self):
        super().__init__()
        self.ui = app.qt.QWebEngineView()

        if ENVIRONMENT == 'production':
            self.ui.load(app.qt.QUrl('http://localhost:8000'))
        elif ENVIRONMENT == 'development':
            self.ui.load(app.qt.QUrl('http://localhost:3000'))
        else:
            raise Exception(f'Unknown environment configuration: {ENVIRONMENT}')

        app.channels.Set(self.main, self.ui)
        app.menu.Main(self.main, self)

    def closeEvent(self, event):
        reply = app.qt.QMessageBox.question(
            self, "Confirm", "Do want to close Holyrics?",
            app.qt.QMessageBox.Yes or app.qt.QMessageBox.No,
            app.qt.QMessageBox.No
        )

        if reply == app.qt.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

        self.loadUi()

    def loadUi(self):
        self.setWindowIcon(
            app.qt.QIcon('public/favicon.png')
        )

        self.setCentralWidget(self.ui)
        self.showMaximized()
