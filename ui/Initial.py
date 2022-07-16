from dataclasses import dataclass
from main import Sepyre
import app


@dataclass()
class InitialWindow(app.qt.QWebEngineView):
    main: Sepyre

    def __post_init__(self):
        super().__init__()
        self.env = self.main.options['env']
        self.path = self.main.options["path"]

        if self.env == 'production':
            self.handler = app.ui.SchemeHandler(self.main)
            self.page().profile().installUrlSchemeHandler(
                b'ui', self.handler
            )

            file = open(f'{self.path}/build/initial.html', 'r')
            html = file.read()
            file.close()

            self.setHtml(html)

        elif self.env == 'development':
            self.load('http://localhost:3000/initial')

        else:
            raise Exception(f'Unknown environment configuration: {self.env}')

        self.setWindowFlags(app.qt.Qt.FramelessWindowHint | app.qt.Qt.WindowStaysOnTopHint)

        self.channels = app.channels.set(self.main, self)
        self.page().setWebChannel(self.channels)

    def loadUi(self):
        self.setWindowIcon(
            app.qt.QIcon('public/favicon.png')
        )

        self.setWindowTitle('Initital Settings')
        self.setFixedSize(800, 600)
        self.show()
