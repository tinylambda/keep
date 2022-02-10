from pathlib import Path
from typing import Any

import tornado.web
import tornado.httpserver
from tornado.ioloop import IOLoop
from tornado.routing import URLSpec

from module_tornado.tornado_helloworld import BaseHandler, User


class MyBaseHandler(BaseHandler):
    def get_current_user(self) -> User:
        user_id = self.get_secure_cookie('user')
        if not user_id:
            return None
        user_id = int(user_id)
        return self.backend.get(user_id)


class MainHandler(MyBaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = self.current_user.name
        self.write(f'Hello, {name}')


class LoginHandler(MyBaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        user_id = int(self.get_argument('user_id'))
        user = self.backend.get(user_id)
        if user is not None:
            self.set_secure_cookie('user', str(user.id))
        else:
            raise tornado.web.HTTPError(404, log_message='no such user!')
        self.redirect('/')


def make_app():
    application = tornado.web.Application([
        URLSpec(r'/', MainHandler),
        URLSpec(r'/login', LoginHandler),
    ],
        template_path=Path.cwd() / 'templates',
        cookie_secret='abc123',
        login_url='/login',
        xsrf_cookies=True,
    )
    return application


if __name__ == '__main__':
    app = make_app()

    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)
    server.start(0)

    IOLoop.current().start()
