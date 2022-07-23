from dataclasses import dataclass
from main import Sepyre
import app


@dataclass()
class Pages(app.qt.QObject):
    main: Sepyre
    window: app.qt.QWebEngineView

    def __post_init__(self):
        super().__init__(self.window)

    @app.qt.Slot()
    def mainWindow(self):
        self.main.page.close()
        self.main.page = app.windows.Main(self.main)
        self.main.ui = self.main.page.ui

        self.main.setup()
        self.main.page.loadUi()
