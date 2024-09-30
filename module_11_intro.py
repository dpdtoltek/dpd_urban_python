import inspect
import os

cur_dir = os.getcwd()


class Intro:
    def __init__(self, attribute=None):
        self.attribute = attribute


def introspection_info(obj):
    obj_info = {'type': type(obj)}
    if isinstance(obj, Intro):
        obj_info['value'] = repr(obj.attribute)
        obj_info['class_name'] = Intro.__name__
    elif not isinstance(obj, Intro):
        obj_info['value'] = repr(obj)
    obj_info['func_name'] = introspection_info.__name__
    obj_info['id'] = id(obj)
    obj_info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    obj_info['methods'] = [meth for meth in dir(obj) if callable(getattr(obj, meth))]
    obj_info['module'] = inspect.getmodule(introspection_info)
    return obj_info


arg_info = introspection_info(42)
print(arg_info)

arg_1 = Intro(attribute=42)
arg_info = introspection_info(arg_1)
print(arg_info)

arg_2 = Intro('Hello')
arg_info = introspection_info(arg_2)
print(arg_info)

list_arg = [42, 'Hello']
arg_3 = Intro(list_arg)
arg_info = introspection_info(arg_3)
print(arg_info)

arg_4 = Intro()
arg_info = introspection_info(arg_4)
print(arg_info)

list_arg = [42, 'Hello']
arg_info = introspection_info(list_arg)
print(arg_info)
