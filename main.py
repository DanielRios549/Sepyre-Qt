from dataclasses import dataclass
from os import environ, path
from sys import exit, argv
from threading import Thread
from dotenv import load_dotenv
import app

load_dotenv()

ENVIRONMENT = environ['ENVIRONMENT']


@dataclass()
class Sepyre():
    app: app.qt.QApplication

    def __post_init__(self):
        self.page: app.qt.QMainWindow | app.qt.QWebEngineView
        self.ui: app.qt.QWebEngineView

        self.options = {
            'path': path.abspath(path.dirname(__file__)),
            'env': ENVIRONMENT,
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
        self.app.setApplicationName(self.options['name'])

        self.config = app.config.Config(self)

        # Define which to load next

        if self.config.initialSettings is True:
            # Load Initial Settings Window
            self.page = app.ui.InitialWindow(self)
            self.ui = self.page
        else:
            # Load Main Interface
            self.page = app.ui.MainWindow(self)
            self.ui = self.page.ui

        # Add Scheme to handle ui:/// URLs
        self.handler = app.ui.SchemeHandler(self)
        self.ui.page().profile().installUrlSchemeHandler(
            b'ui', self.handler
        )

        self.setup()
        self.page.loadUi()

    # Add Channels to communicate with Svelte front-end
    # Accesible through window.app object
    def setup(self):
        self.channels = app.channels.set(self, self.ui)
        self.ui.page().setWebChannel(self.channels)


if __name__ == "__main__":
    # Serve static files build using svelte
    # if ENVIRONMENT == 'production':
    #     svelte = Thread(target=app.svelte.serve, daemon=True)
    #     svelte.start()

    # Register custom URL Scheme
    scheme = app.qt.QWebEngineUrlScheme(b'ui')
    scheme.setFlags(app.qt.QWebEngineUrlScheme.CorsEnabled)
    app.qt.QWebEngineUrlScheme.registerScheme(scheme)

    # Init PySide application
    application = app.qt.QApplication(argv)
    Sepyre(application)

    # Run Application
    exit(application.exec())
