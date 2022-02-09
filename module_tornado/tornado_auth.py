from typing import Any

import tornado.web
from tornado.ioloop import IOLoop
from tornado.routing import URLSpec

from module_tornado.tornado_helloworld import BaseHandler


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name = self.current_user.name
        self.write(f'Hello, {name}')


class LoginHandler(BaseHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="user_id">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

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
        cookie_secret='abc123',
        login_url='/login',
    )
    return application


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()
