****
deps
****

Python >=3.6 dependency injection based on attrs. Very simple, yet powerful.

Inspired by `inject-attrs <https://github.com/dradetsky/inject-attrs/>`_.


Usage
-----
``deps`` **works only with typing annotations defined as presented below!**

1. First, replace your ``@attr.s(...)`` decorators:
    .. code-block:: python

      @attr.s(auto_attribs=True, <other args/kwargs...>)
      class Thing:
        cfg: Config
        some_dep: SomeClass

   With:
    .. code-block:: python

      import deps

      @deps.s(<other args/kwargs...>)
      class Thing:
          cfg: IConfig
          some_dep: ISomeClass

   Notice that ``auto_attribs=True`` is no more needed, it will be forced by this package.

2. Next you have to prepare - somewhere in your codebase - an abstract interfaces classes for your attributes:
    .. code-block:: python

      import deps

      class IConfig(deps.Interface)
          # ...

      class ISomeClass(deps.Interface)
          # ...

3. Now prepare interfaces implementations:
    .. code-block:: python

      from interfaces import IConfig, ISomeClass

      class Config(IConfig)
          # ...

      class SomeClass(ISomeClass)
          # ...

4. Finally, configure dependency injection bindings provided by `Inject <https://pypi.org/project/Inject/>`_ package, using ``bind_to_constructor`` directive.


License
-------
MIT


Creator
-------
Daniel Kuruc
