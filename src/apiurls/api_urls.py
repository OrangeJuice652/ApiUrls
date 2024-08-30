from apiurls.sub_directories import SubDirecotries


class ApiUrlsMixin:
    def __init_subclass__ (cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if f'_protocol' not in cls.__dict__:
            raise ValueError('ApiProtocol is required')
        
        if f'_domain' not in cls.__dict__:
            raise ValueError('ApiDomain is required')

        if f'_sub_directories' not in cls.__dict__:
            raise ValueError('SubDirectories is required')
        
        if not isinstance(cls.__dict__[f'_sub_directories'], SubDirecotries):
            raise TypeError('__sub_directories is not SubDirecotries')

    def _origin(self):
        return f'{self._protocol}://{self._domain}'

    def __getattr__(self, name):
        if name in self._sub_directories:
            return self.__url(name)
        return super().__getattr__(name)
    
    def __url(self, sub_directory_name):
        return f'{self._origin()}{self._sub_directories[sub_directory_name]}'
