class Entity:
    def __init__(self):
        self.battle_buffs = {}
        self.farming_buffs = {}
        self.wood_cutting_buffs = {}
        self.stone_mining_buffs = {}
        self.gold_mining_buffs = {}
        self.level = None


class Architecture(Entity):
    def __init__(self):
        super(Architecture, self).__init__()
        self.combat_effectiveness = 0  # 战力


class CityHall(Architecture):
    def __init__(self):
        super(CityHall, self).__init__()
        self.queue_num = 1
        self.capacity = 0


class Hospital(Architecture):
    def __init__(self):
        super(Hospital, self).__init__()
        self.capacity = 0

    def from_state(self, state: dict):
        pass


class Farm(Entity):
    def __init__(self):
        super(Farm, self).__init__()


class Game:
    pass
