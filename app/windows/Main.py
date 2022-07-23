from dataclasses import dataclass
from main import Sepyre
import app


@dataclass()
class Main(app.qt.QMainWindow):
    main: Sepyre

    def __post_init__(self):
        super().__init__()
        self.ui = app.qt.QWebEngineView()
        self.env = self.main.options['env']
        self.path = self.main.options['path']

        if self.env == 'production':
            file = open(f'{self.path}/build/index.html', 'r')
            html = file.read()
            file.close()

            self.ui.setHtml(html)

        elif self.env == 'development':
            self.ui.load('http://localhost:3000')

        else:
            raise Exception(f'Unknown environment configuration: {self.env}')

        app.menu.Main(self.main, self)

    def closeEvent(self, event):
        reply = app.qt.QMessageBox.question(
            self, "Confirm", f"Do want to close {self.main.options['name']}?",
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

        self.setWindowTitle(self.main.options['name'])
        self.setCentralWidget(self.ui)
        self.showMaximized()
