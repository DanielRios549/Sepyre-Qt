from app.qt import QWebChannel, QWebEngineView
from app.channels.config import Config
from app.channels.pages import Pages
from main import Sepyre


# Setup Channels to communicate with Svelte Front-end
def set(main: Sepyre, window: QWebEngineView):
    channels = QWebChannel()
    channels.registerObject('config', Config(main, window))
    channels.registerObject('pages', Pages(main, window))

    return channels
