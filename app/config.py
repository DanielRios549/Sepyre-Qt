from dataclasses import dataclass
from pathlib import Path
from configparser import ConfigParser
from main import Sepyre
import app


@dataclass()
class Config(app.qt.QObject):
    main: Sepyre

    def __post_init__(self):
        super().__init__(self.main)
        userFolder = Path.home()

        self.folder = userFolder.joinpath(self.main.options['configFolder'])
        self.file = self.folder.joinpath(self.main.options['configFile'])
        self.initialSettings = False

        if self.folder.exists() is False:
            print(f'Creating Config Folder at \033[34m{self.folder}\033[m...')
            self.folder.mkdir(0o775, False, False)
            self.initialSettings = True

        if self.file.exists() is False:
            print(f'Creating Config File at \033[34m{self.file}\033[m...')
            self.file.touch(0o775, False)
            self.initialSettings = True

    def getWindowDimensions(self, reduction: int = 20) -> dict:
        height = self.main.height() - (self.main.height() * reduction / 100)
        width = self.main.width() - (self.main.width() * reduction / 100)

        return {'width': width, 'height': height}

    def getAll(self) -> dict:
        file = str(self.file)
        parser = ConfigParser()
        parser.read(file)

        configs: dict = {}

        for section in parser.sections():
            configs[section] = {}

            for option, value in parser.items(section):
                configs[section][option] = value

        return configs

    def get(self, section: str, config: str, default: str) -> str:
        if section == 'env':
            return self.main.options[config]
        else:
            configs = self.getAll()

            if section in configs.keys() and config in configs[section]:
                return configs[section][config]
            else:
                return default

    def update(self, section: str, key: str, value: str):
        configFile = str(self.file)
        parser = ConfigParser()
        parser.read(configFile)

        if section not in parser.sections():
            parser.add_section(section)

        parser.set(section, key, value)

        with open(configFile, 'w+') as config:
            parser.write(config)

    def defaultOptions(self):
        self.update('app', 'theme', 'dark')
