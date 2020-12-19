static_config = {
    'characters': [
        {
            'character_id': 20001,
            'name': 'SunWu',
            'name remarks': 'SunWu remarks',
            'quality': 2,
            'career': 1,
            'animation': 'battle_name',
            'animation_wait': 'wait_name',
            'animation_wait_direction': 'wait_battle_name',
            'country': 1,
            'attr': {
                1: 482,
                2: 181,
                3: 91,
                4: 10,
                5: 7,
                6: 6,
                10: 1,
                11: 1,
                12: 1,
                13: 1,
                20: 100,
            },
            'talent': 1,
            'base_skill': '2000111,2000121,2000131,2000141',
            'particular_skill': '',
            'exchange_skill': '',
            'general_attack': '10001',
            'shards_id': '2620001',
            'number': 10,
        }
    ],
    'items': {

    }
}


rules = {
    'character': [
        {
            'name': 'upgrade_talent',
            'match': [
                ['>=', 'character.level', 10]
            ]
        }
    ]
}


state = {
    'characters': {
        'c1': {
            'id': 'c1',
            'character_id': 20001,
            'level': 1,
            'talent': {
                'id': 1,
                'level': 0
            }
        }
    }
}

events = []


