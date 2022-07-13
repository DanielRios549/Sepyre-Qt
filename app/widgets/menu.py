from dataclasses import dataclass
import app


@dataclass
class Item(app.qt.QMenu):
    element: app.qt.QObject

    def __post_init__(self):
        super().__init__(self.element)

    # TODO Get icon color based on the current theme.
    # Paint Event could also be used
    # Therefore, it does not work when exporting the menu

    def drawIcons(self):
        # List of Actions

        actions: list[app.qt.QAction] = self.findChildren(app.qt.QAction)

        for action in actions:
            self.iconName: str = action.property('iconName')

            if '' != self.iconName is not None:
                # folder = 'ui/icons'
                # iconPath = f'{folder}/{self.iconName}.svg'
                iconPath = 'public/favicon.png'

                icon = app.qt.QPixmap(iconPath)
                painter = app.qt.QPainter(icon)
                painter.setCompositionMode(app.qt.QPainter.CompositionMode_SourceIn)
                painter.fillRect(icon.rect(), '#d6d6d6')

                painter.end()
                action.setIcon(icon)


@dataclass
class Create():
    options: dict
    parent: app.qt.QObject
    menuBar: bool = False

    def __post_init__(self):
        for item in self.options.values():
            # *********************************
            #              Menu
            # *********************************

            self.menu = Item(self.parent)
            self.menu.setTitle(item['name'])

            # *********************************
            #             Actions
            # *********************************

            for action in item['actions']:
                current = item['actions'][action]

                # Create the Action

                addAction = app.qt.QAction(self.menu)
                addAction.setText(current['text'])
                addAction.setObjectName(current['name'])
                addAction.setShortcut(app.qt.QKeySequence(current['shortcut']))
                addAction.setProperty('iconName', current['icon'])
                addAction.triggered.connect(current['function'])

                # Add Actions to Menu

                self.menu.addAction(addAction)

            # If self.menuBar is True, self.parent must be a QMenuBar
            # So it adds the Menu to the Menu Bar

            if self.menuBar is not False:
                self.parent.addMenu(self.menu)

            self.menu.drawIcons()

    def getMenu(self) -> Item:
        return self.menu
