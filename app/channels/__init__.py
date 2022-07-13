from app.channels.config import Config
from app.qt import QWebChannel, QWebEngineView
from app.channels import Config
from main import Sepyre


# Setup Channels to communicate with Svelte Front-end
def set(main: Sepyre, window: QWebEngineView):
    channels = QWebChannel()
    channels.registerObject('config', Config(main, window))

    return channels
