from dataclasses import dataclass
from main import Sepyre
from app.windows.Main import Main
from app.windows.Initial import Initial
import app


@dataclass()
class SchemeHandler(app.qt.QWebEngineUrlSchemeHandler):
    main: Sepyre

    def __post_init__(self):
        super().__init__()

    def requestStarted(self, request: app.qt.QWebEngineUrlRequestJob):
        method = request.requestMethod()

        if method != b'GET':
            print(f"Method '{method}' not allowed")
            request.fail(app.qt.QWebEngineUrlRequestJob.RequestDenied)

            return

        url = request.requestUrl()
        path = url.path()

        file = app.qt.QFile(f"{self.main.options['path']}/build" + path)
        file.setParent(request)

        request.destroyed.connect(file.deleteLater)

        if not file.exists() or file.size() == 0:
            print(f"Resource '{path}' not found or is empty")
            request.fail(app.qt.QWebEngineUrlRequestJob.UrlNotFound)

            return

        type = app.qt.QMimeDatabase().mimeTypeForFile(
            app.qt.QFileInfo(file)
        )

        request.reply(type.name().encode(), file)
