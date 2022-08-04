from dataclasses import dataclass
from main import Sepyre
# import spleeter.separator as spleeter
import json
import app


@dataclass()
class Functions(app.qt.QObject):
    main: Sepyre
    window: app.qt.QWebEngineView

    def __post_init__(self):
        super().__init__(self.window)

    @app.qt.Slot(result=list)  # type: ignore
    def getFiles(self) -> list:
        separations = []

        try:
            folder = self.main.config.folder.joinpath('separation')

            for subFolder in folder.iterdir():
                if subFolder.is_dir():
                    separations.append(subFolder.name)

        except FileNotFoundError:
            print('No Separations folder, add your first one.')

        except Exception:
            print('It runs in a problem.')

        return separations

    @app.qt.Slot(str, result=str)  # type: ignore
    def getInfo(self, name: str) -> str:
        file = self.main.config.folder.joinpath('separation').joinpath(name).joinpath('info.conf')
        info = app.utils.parser.config(str(file), True)

        return json.dumps(info)

    @app.qt.Slot(str)
    def copy(self, file: str):
        # separator = spleeter.Separator('spleeter:5stems')

        # separator.separate_to_file(
        #     base64.b64decode(file),
        #     '/home/daniel/Python/_dev/Sepyre/test123'
        # )
        # try:
        # file = base64.b64decode(file)
        # with open('/home/daniel/Python/_dev/Sepyre/test123', 'w+') as f:
        #     f.write(file.decode())

        # except Exception:
        #     print('Problem to get the File')
        print(f'The file is: {file}')
        print(f'The file converted is: {json.loads(file)}')
