from .server_base import ServerBase


class ServerRole(ServerBase):
    ID_NAME = 'role_id'
    DB_NAME = 'role'

    def __init__(self):
        super(ServerRole, self).__init__()

