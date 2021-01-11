import typing
import time
import random
import string

from blueprint.field import Field
from blueprint.backend import Backend
from blueprint.exceptions import BluePrintInitException


class BluePrintMeta(type):
    def __new__(mcs, name: typing.AnyStr, bases: typing.Tuple, class_dict: typing.Dict):
        class_dict_copy = class_dict.copy()

        _instance_id = Field(
            verbose_name='Instance ID',
            data_type='string',
            required=True,
            default=None,
        )
        _create_ts = Field(
            verbose_name='Creation Timestamp',
            data_type='int',
            required=True,
            default=None,
        )

        class_dict_copy.update({
            '_instance_id': _instance_id,
            '_create_ts': _create_ts,
        })

        for k, v in class_dict_copy.items():
            if isinstance(v, Field):
                v.name = k
                v.fullname = f'{name.lower()}.{k}'
                v.internal_name = f'field__{k}'
                if v.verbose_name is None:
                    v.verbose_name = v.name

        meta_context: typing.Dict = {}
        meta_class = class_dict.get('Meta')
        if meta_class:
            assert isinstance(meta_class, type)
            m_dict: typing.Dict = meta_class.__dict__
            for mk, mv in m_dict.items():
                if not mk.startswith('__'):
                    meta_context.update({mk: mv})
        class_dict_copy.update({'meta_context': meta_context})

        def _random_string(self):
            return ''.join(random.sample(string.ascii_letters + string.digits, 6))
        class_dict_copy.update({'random_string': property(_random_string)})

        def _config(self):
            pass
        class_dict_copy.update({'config': property(_config)})

        def initialize_instance(self, init_data: typing.Dict) -> typing.NoReturn:
            cls_dict: typing.Dict = self.__class__.__dict__
            for sk, sv in cls_dict.items():
                if isinstance(sv, Field):
                    if sk in init_data:
                        sk_v = init_data[sk]
                        data_type: typing.Any = sv.data_type

                        multi: bool = sv.multi
                        v_deserialized = None
                        if multi:
                            assert isinstance(sk_v, list)
                            if isinstance(data_type, BluePrintMeta):
                                if issubclass(data_type, BluePrint):
                                    v_deserialized = [
                                        data_type(**d)
                                        for d in sk_v
                                    ]
                            else:
                                v_deserialized = sk_v
                        else:
                            assert not isinstance(sk_v, list)
                            if isinstance(data_type, BluePrintMeta):
                                if issubclass(data_type, BluePrint):
                                    v_deserialized = data_type(**sk_v)
                            else:
                                v_deserialized = sk_v

                        setattr(self, sk, v_deserialized)
                    else:
                        if sv.multi:
                            sv.default = []

            # If no self._create_ts, supply one
            if not self._create_ts:
                self._create_ts = int(time.time())

            # Generate `self._instance_id` according to this format template
            instance_id_template = self.meta_context.get('instance_id_template')
            if not instance_id_template:
                raise BluePrintInitException(msg=f'instance_id_template not configured for <{self.__class__.__name__}>')
            self.instance_id_template = instance_id_template

            # Can be saved to backend at this level ?
            is_top = self.meta_context.get('is_top', False)
            self.is_top = is_top

            # Check instance state (without _instance_id)
            # And build instance id render context
            self.instance_id_render_context = {}

            for sk, sv in cls_dict.items():
                if sk == '_instance_id':
                    continue

                if isinstance(sv, Field):
                    sk_v = getattr(self, sk, None)
                    self.instance_id_render_context.update({sk: sk_v})
                    if sv.required and sv.default is None:
                        if sk_v is None:
                            raise BluePrintInitException(msg=f'Please specify value for {sv.fullname}')

            self._backend = Backend()  # Redis ?

        def init(self, **kwargs) -> typing.NoReturn:
            self.initialize_instance(kwargs)

            if self._instance_id:
                pass
            else:
                self._instance_id = self.instance_id_template.format(
                    random_string=self.random_string,
                    **self.instance_id_render_context
                )

        def serialize(self) -> typing.Dict:
            cls_dict: typing.Dict = self.__class__.__dict__
            serialized: typing.Dict = {}

            for sk, sv in cls_dict.items():
                if isinstance(sv, Field):
                    sk_v = getattr(self, sk)

                    data_type: typing.Any = sv.data_type
                    multi: bool = sv.multi
                    if multi:
                        assert isinstance(sk_v, list)
                        if isinstance(data_type, BluePrintMeta):
                            if issubclass(data_type, BluePrint):
                                serialized.update({sk: [item.serialize() for item in sk_v]})
                        else:
                            serialized.update({sk: sk_v})
                    else:
                        assert not isinstance(sk_v, list)
                        if isinstance(data_type, BluePrintMeta):
                            if issubclass(data_type, BluePrint):
                                serialized.update({sk: sk_v.serialize()})
                        else:
                            serialized.update({sk: sk_v})
            return serialized

        class_dict_copy.update({
            '__init__': init,
            'initialize_instance': initialize_instance,
            'serialize': serialize,
        })

        cls = type.__new__(mcs, name, bases, class_dict_copy)
        return cls


class BluePrint(metaclass=BluePrintMeta):
    def save(self):
        assert self.is_top
        self._backend.set('x', 'y')

