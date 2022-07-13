from dataclasses import dataclass
from app.channels.config import Config
from app.qt import QWebChannel, QWebEngineView
from app.channels import Config
from main import Sepyre


@dataclass()
class Set():
    main: Sepyre
    window: QWebEngineView

    # Setup Channels to communicate with Svelte Front-end
    def __post_init__(self):
        super().__init__()
        self.channel = QWebChannel()

        self.channel.registerObject('config', Config(self.main))
        self.window.page().setWebChannel(self.channel)
