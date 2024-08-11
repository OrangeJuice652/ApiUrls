from sub_directories import SubDirecotries

class ApiUrlsMeta(type):
    def __new__(meta, name, bases, attributes):
        sub_direcories_attr_name = next(
            filter(lambda key: isinstance(attributes[key], SubDirecotries), attributes.keys()),
            None
        )
        if sub_direcories_attr_name is None:
            raise ValueError('SubDirectories attributes is required')
        attributes['__subdirectories_attr_name'] = sub_direcories_attr_name
    
        return type.__new__(meta, name, bases, attributes)


class ApiUrlsMixin(metaclass=ApiUrlsMeta):
    def __getattr__(self, name):
        if name in self.__subdirectories_attr_name:
            return 
        return super().__getattr__(name)
