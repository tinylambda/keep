from blueprint import BluePrint
from blueprint.field import Field


class Character(BluePrint):
    config_id = Field(
        verbose_name='Configuration ID',
        data_type='string',
        required=True,
    )
    level = Field(
        verbose_name='Level',
        data_type='int',
        required=True,
        default=1,
    )
    star = Field(
        verbose_name='Star',
        data_type='int',
        required=True,
        default=1,
    )
    exp = Field(
        verbose_name='Experience',
        data_type='int',
        required=True,
        default=0,
    )

    class Meta:
        config_key = 'character'
        instance_id_template = '{config_id}_{random_string}_{_create_ts}'
        single_instance_per_config = True  # 1 config to 1 instance ?
        top = False


class Item(BluePrint):
    config_id = Field(
        verbose_name='Configuration ID',
        data_type='string',
        required=True,
    )
    amount = Field(
        verbose_name='Item amount',
        data_type='int',
        required=True,
        default=0,
    )


class Equip(BluePrint):
    pass


class Role(BluePrint):
    server_id = Field(
        verbose_name='Server ID',
        data_type='string',
        required=True,
    )
    role_id = Field(
        verbose_name='Role ID',
        data_type='string',
        required=True,
    )
    characters = Field(
        verbose_name='Characters',
        data_type=Character,
        multi=True,
    )
    items = Field(
        verbose_name='Items',
        data_type=Item,
        multi=True,
    )

    class Meta:
        instance_id_template = 'role_{server_id}_{role_id}'
        single_instance_per_config = True  # 1 config to 1 instance ?
        top = True

    def add_character(self, character: Character):
        self.characters.append(character)


if __name__ == '__main__':
    # character = Character(config_id='20001')
    # character.save()
    # print(character.exp)
    # print(character.instance_id_render_context)

    role = Role(server_id='s113', role_id='r10002', characters=[
        {'_instance_id': 'i1', 'level': 10, 'star': 2, 'config_id': '20001'},
        {'_instance_id': 'i2', 'level': 12, 'star': 2, 'config_id': '20002'},
    ])
    print(role.instance_id_render_context)
    print(role.server_id)
    print(role.characters)
    character = Character(config_id='20003')
    role.add_character(character)
    print(role.characters)

    from blueprint import BluePrintMeta
    print(isinstance('x', BluePrintMeta))
    print(issubclass(Character, BluePrint))

    import pprint
    pprint.pprint(role.serialize())
