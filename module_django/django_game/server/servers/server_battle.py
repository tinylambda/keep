from .server_base import ServerBase


class ServerBattle(ServerBase):
    ID_NAME = "battle_id"
    DB_NAME = "battle"

    def __init__(self):
        super(ServerBattle, self).__init__()
