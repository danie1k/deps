from typing import get_type_hints

from attr import attrs as original_attrs, Factory
import inject

__all__ = ('attributes', 'attrs', 's', 'Interface')
__version__ = '0.1'


class Interface:
    pass


def attrs(*args, **kwargs):
    def wrap(cls):
        hints = get_type_hints(cls)

        for property_name, property_type in hints.items():
            if isinstance(property_type, type) and issubclass(property_type, Interface):
                setattr(cls, property_name, Factory(lambda: inject.instance(property_type)))

        kwargs['auto_attribs'] = True
        return original_attrs(*args, **kwargs)(cls)

    return wrap


s = attributes = attrs
