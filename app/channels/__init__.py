from app.qt import QWebChannel, QWebEngineView
from app.channels.config import Config
from app.channels.pages import Pages
from app.channels.functions import Functions
from main import Sepyre


# Setup Channels to communicate with Svelte Front-end
def set(main: Sepyre, window: QWebEngineView):
    channels = QWebChannel()
    channels.registerObjects({
        'config': Config(main, window),
        'pages': Pages(main, window),
        'functions': Functions(main, window)
    })

    return channels
