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
        self.page: app.qt.QMainWindow
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

        self.config = app.config.Config(self)

        # Load Initial Settings Window
        if self.config.initialSettings is True:
            self.page = app.windows.Initial(self)

        # Load Main Interface
        else:
            self.page = app.windows.Main(self)

        self.ui = self.page.ui

        # Add Scheme to handle ui:/// URLs
        self.handler = app.windows.SchemeHandler(self)
        self.ui.page().profile().installUrlSchemeHandler(
            b'ui', self.handler
        )

        self.inspector = app.qt.QWebEngineView()
        self.setup()
        self.page.loadUi()

    def showDevTools(self):
        # Show if is hidden
        if self.splitter.count() == 1:
            self.inspector.page().setInspectedPage(self.ui.page())
            self.splitter.addWidget(self.inspector)

        # Close if is opened
        else:
            self.inspector.page().setInspectedPage(None)    # type: ignore
            self.inspector.setParent(None)                  # type: ignore

    def setup(self):
        #  Add Shortcut Keys
        self.key_f5 = app.qt.QShortcut(app.qt.QKeySequence(app.qt.Qt.Key_F5), self.page)
        self.key_f5.activated.connect(self.ui.reload)       # type: ignore
        self.key_f12 = app.qt.QShortcut(app.qt.QKeySequence(app.qt.Qt.Key_F12), self.page)
        self.key_f12.activated.connect(self.showDevTools)   # type: ignore

        # Create Splitter to show inpector
        self.box = app.qt.QHBoxLayout(self.page)

        self.splitter = app.qt.QSplitter(app.qt.Qt.Horizontal)
        self.splitter.addWidget(self.ui)

        self.box.addWidget(self.splitter)
        self.page.setLayout(self.box)

        # Add Channels to communicate with Svelte front-end
        # Accesible through window.app object
        self.channels = app.channels.set(self, self.ui)
        self.ui.page().setWebChannel(self.channels)

        self.page.setCentralWidget(self.splitter)

        # General Applications options
        self.app.setApplicationName(self.options['name'])


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
