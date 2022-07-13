from dataclasses import dataclass
from main import Sepyre
import json
import app


@dataclass()
class Config(app.qt.QObject):
    main: Sepyre
    window: app.qt.QWebEngineView

    def __post_init__(self):
        super().__init__(self.window)

    @app.qt.Slot(str, str, str, result=str)  # type: ignore
    @app.qt.Slot(str, str, result=str)       # type: ignore
    def get(self, section: str, value: str, default: str = 'Default') -> str:
        return self.main.config.get(section, value, default)

    @app.qt.Slot(result=str)  # type: ignore
    def getAll(self) -> str:
        configs = self.main.config.getAll()
        return json.dumps(configs)

    @app.qt.Slot(str, str, str)
    def set(self, section: str, key: str, value: str):
        self.main.config.update(section, key, value)
