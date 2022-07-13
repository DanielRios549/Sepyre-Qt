from dataclasses import dataclass
from pathlib import Path
from configparser import ConfigParser
from main import Sepyre


@dataclass()
class Config():
    main: Sepyre

    def __post_init__(self):
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
        height = self.main.page.height() - (self.main.page.height() * reduction / 100)
        width = self.main.page.width() - (self.main.page.width() * reduction / 100)

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
