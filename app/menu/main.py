from dataclasses import dataclass
from main import Sepyre
import app


@dataclass
class Main():
    main: Sepyre
    window: app.qt.QMainWindow

    def __post_init__(self):
        self.mainMenu = {
            'file': {
                'name': '&File',
                'actions': {
                    'bible': {
                        'name': 'goToBible',
                        'text': 'Go to &Bible',
                        'shortcut': 'F7',
                        'icon': 'text/font-size',
                        'function': None
                    }
                }
            },
            'new': {
                'name': '&New',
                'actions': {
                    'music': {
                        'name': 'newMusic',
                        'text': '&New Music',
                        'shortcut': 'CTRL+1',
                        'icon': 'player/pause',
                        'function': None  # lambda: self.newLyricUi()
                    },
                    'theme': {
                        'name': 'newTheme',
                        'text': '&New Theme',
                        'shortcut': 'CTRL+2',
                        'icon': 'player/previous',
                        'function': None  # lambda: self.newThemeUi()
                    },
                }
            }
        }
        self.setMenu()

    def setMenu(self):
        menuBar = app.qt.QMenuBar(self.window)
        menuBar.setObjectName('mainMenu')

        app.widgets.menu.Create(self.mainMenu, menuBar, True)

        self.window.setMenuBar(menuBar)
