from dataclasses import dataclass
from main import Sepyre
import app


@dataclass()
class Initial(app.qt.QMainWindow):
    main: Sepyre

    def __post_init__(self):
        super().__init__()
        self.ui = app.qt.QWebEngineView()
        self.env = self.main.options['env']
        self.path = self.main.options['path']

        if self.env == 'production':
            file = open(f'{self.path}/build/initial.html', 'r')
            html = file.read()
            file.close()

            self.ui.setHtml(html)

        elif self.env == 'development':
            self.ui.load('http://localhost:3000/initial')

        else:
            raise Exception(f'Unknown environment configuration: {self.env}')

        self.setWindowFlags(app.qt.Qt.FramelessWindowHint | app.qt.Qt.WindowStaysOnTopHint)

    def loadUi(self):
        self.setWindowIcon(
            app.qt.QIcon('public/favicon.png')
        )

        self.setWindowTitle('Initital Settings')
        self.setFixedSize(800, 600)
        self.show()
