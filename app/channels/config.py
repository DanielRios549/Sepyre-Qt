from dataclasses import dataclass
from main import Sepyre
import json
import app


@dataclass()
class Config(app.qt.QObject):
    main: Sepyre

    def __post_init__(self):
        super().__init__(self.main)

    @app.qt.Slot(str, str, str, result=str)  # type: ignore
    @app.qt.Slot(str, str, result=str)       # type: ignore
    def get(self, section: str, value: str, default: str = 'Default') -> str:
        return self.main.config.get(section, value, default)

    @app.qt.Slot(result=str)  # type: ignore
    def getAll(self) -> str:
        configs = self.main.config.getAll()
        return json.dumps(configs)
