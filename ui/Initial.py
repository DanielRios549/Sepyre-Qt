from dataclasses import dataclass
from main import Sepyre
import app


@dataclass()
class InitialWindow(app.qt.QWebEngineView):
    main: Sepyre

    def __post_init__(self):
        super().__init__()

        self.load(app.qt.QUrl('http://localhost:3000/initial'))
        self.setWindowFlags(app.qt.Qt.FramelessWindowHint or app.qt.Qt.WindowStaysOnTopHint)

        app.channels.Set(self.main, self)

    def loadUi(self):
        self.setFixedSize(800, 600)
        self.show()
