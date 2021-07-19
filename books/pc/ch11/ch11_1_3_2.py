import urllib.request


if __name__ == '__main__':
    password_mgr = urllib.request.HTTPPasswordMgr()
    password_mgr.add_password('pypi', 'http://pypi.python.org', 'username', 'password')
    auth = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(auth)

    r = urllib.request.Request('http://pypi.python.org/pypi?:action=login')
    u = opener.open(r)
    resp = u.read()
    print(resp.decode())
