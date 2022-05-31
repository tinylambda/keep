from abc import ABC
from datetime import datetime
from pathlib import Path
from typing import Optional, Awaitable, Any, Dict

import attr
import tornado.web
import tornado.ioloop
import tornado.locale
from tornado.locale import Locale
from tornado.routing import URLSpec

from module_tornado import ui_modules


@attr.s
class User:
    id: int = attr.ib()
    name: str = attr.ib()
    prefs: Dict[str, Any] = attr.ib()


@attr.s
class Entry:
    id: int = attr.ib()
    title: str = attr.ib()
    create_time: datetime = attr.ib()
    update_time: datetime = attr.ib()


class BaseHandler(tornado.web.RequestHandler, ABC):
    def __init__(self, *arg, **kwargs):
        users = [
            User(1, "Felix", {"locale": "zh_CN"}),
            User(2, "Cheng", {"locale": "zh_CN"}),
            User(3, "Jim", {"locale": "en_US"}),
        ]
        self.backend: Dict[int, User] = {item.id: item for item in users}

        entries = [
            Entry(1, "Foo", datetime.now(), datetime.now()),
            Entry(2, "Bar", datetime.now(), datetime.now()),
            Entry(3, "Baz", datetime.now(), datetime.now()),
        ]
        self.entry_backend: Dict[int, Entry] = {item.id: item for item in entries}

        super(BaseHandler, self).__init__(*arg, **kwargs)

    def set_default_headers(self) -> None:
        self.set_header("Server", "TestServer")

    def prepare(self) -> Optional[Awaitable[None]]:
        pass

    def get_current_user(self) -> User:
        user_id = self.get_secure_cookie("user")
        if not user_id:
            return self.backend.get(1)  # test without login
            # return None
        user_id = int(user_id)
        return self.backend.get(user_id)

    def get_user_locale(self) -> Optional[tornado.locale.Locale]:
        if "locale" not in self.current_user.prefs:
            return None
        return Locale.get(self.current_user.prefs["locale"])

    def on_connection_close(self) -> None:
        pass

    def write_error(self, status_code: int, **kwargs: Any) -> None:
        self.render(f"{status_code}.html")


class MainHandler(BaseHandler):
    def get(self):
        print(tornado.locale.get_supported_locales())
        self.write("Hello, world")


class AsyncMainHandler(BaseHandler):
    async def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        response = await http.fetch("https://www.baidu.com/")
        self.write({"body": response.effective_url})


class ErrorHandler(BaseHandler):
    async def get(self):
        raise tornado.web.HTTPError(404, log_message="Not found you")


class StoryHandler(BaseHandler):
    def __init__(self, *args, **kwargs):
        self.db = None
        super(StoryHandler, self).__init__(*args, **kwargs)

    def initialize(self, db):
        self.db = db

    def get(self, story_id):
        self.write("this is story %s" % story_id)


class FormHandler(BaseHandler):
    def get(self):
        self.render("form.html")

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))


class TemplateHandler(BaseHandler):
    async def get(self):
        items = [f"item{i}" for i in range(10)]
        await self.render("template.html", title="My Page", items=items)


class TemplateI18NHandler(BaseHandler):
    async def get(self):
        await self.render("template_i18n.html")


# test UI module
class HomeHandler(BaseHandler):
    def get(self):
        entries = self.entry_backend.values()
        self.render("home.html", entries=entries)


class EntryHandler(BaseHandler):
    def get(self, entry_id: int):
        int_id = int(entry_id)
        entry = self.entry_backend.get(int_id)
        if not entry:
            raise tornado.web.HTTPError(404)
        self.render("entry.html", entry=entry)


def make_app():
    tornado.locale.load_translations(Path.cwd() / "locale")
    return tornado.web.Application(
        [
            URLSpec(r"/", MainHandler),
            URLSpec(r"/story/([0-9]+)", StoryHandler, dict(db=None), name="story"),
            URLSpec(r"/form", FormHandler),
            URLSpec(
                r"/redirect",
                tornado.web.RedirectHandler,
                dict(url="https://www.baidu.com/", permanent=True),
            ),
            URLSpec(r"/async", AsyncMainHandler),
            URLSpec(r"/error", ErrorHandler),
            URLSpec(r"/template", TemplateHandler),
            URLSpec(r"/template_i18n", TemplateI18NHandler),
            URLSpec(r"/home", HomeHandler),
            URLSpec(r"/entry/([0-9]+)", EntryHandler),
        ],
        template_path=Path.cwd() / "templates",
        compiled_template_cache=False,
        cookie_secret="abc123",
        ui_modules=ui_modules,
        xsrf_cookies=True,
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
