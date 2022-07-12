from os import environ
from sys import exit, argv
from threading import Thread
from dotenv import load_dotenv
import app

load_dotenv()

ENVIRONMENT = environ['ENVIRONMENT']


class Sepyre(app.qt.QWebEngineView):
    def __init__(self):
        super().__init__()

        if ENVIRONMENT == 'production':
            self.load(app.qt.QUrl('http://localhost:8000'))
        elif ENVIRONMENT == 'development':
            self.load(app.qt.QUrl('http://localhost:3000'))
        else:
            raise Exception(f'Unknown environment configuration: {ENVIRONMENT}')

        self.options = {
            'name': environ['NAME'],
            'charset': environ['CHARSET'],
            'version': environ['VERSION'],
            'iconFolder': environ['ICONFOLDER'],
            'styleFolder': environ['STYLEFOLDER'],
            'langFolder': environ['LANGFOLDER'],
            'configFolder': environ['CONFIGFOLDER'],
            'configFile': environ['CONFIGFILE'],
            'themesFolder': environ['THEMESFOLDER']
        }

        self.config = app.config.Config(self)
        self.config.defaultOptions()

        self.channels()
        self.loadUi()

    # Setup Channels to communicate with Svelte Front-end
    def channels(self):
        self.channel = app.qt.QWebChannel()

        self.channel.registerObject('config', app.channels.config.Config(self))
        self.page().setWebChannel(self.channel)

    # Setup the MainWindow
    def loadUi(self):
        self.setWindowIcon(
            app.qt.QIcon('public/favicon.png')
        )

        self.showMaximized()


if __name__ == "__main__":
    # Serve static files build using svelte
    if ENVIRONMENT == 'production':
        svelte = Thread(target=app.svelte.serve, daemon=True)
        svelte.start()

    # Init PySide application
    core = app.qt.QApplication(argv)
    view = Sepyre()
    view.show()

    # Run Application
    exit(core.exec())
