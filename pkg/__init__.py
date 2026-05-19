_m1 = __import__(__name__ + '.m1', fromlist=['*'])
__all__ = [name for name in _m1.__dict__ if not (name.startswith('__') and name.endswith('__'))]
globals().update({name: getattr(_m1, name) for name in __all__})
