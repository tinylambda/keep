import inspect
import pprint

import module_inspect.example as example


pprint.pprint(
    inspect.getsourcelines(example.A.get_name)
)

