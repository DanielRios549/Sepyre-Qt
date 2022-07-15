from dataclasses import dataclass
from main import Sepyre
import app


@dataclass()
class InitialWindow(app.qt.QWebEngineView):
    main: Sepyre

    def __post_init__(self):
        super().__init__()

        self.load(app.qt.QUrl('http://localhost:3000/initial'))
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
