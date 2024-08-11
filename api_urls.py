from sub_directories import SubDirecotries


class ApiUrlsMeta(type):
    def __new__(meta, name, bases, attributes):
        if f'_{name}__protocol' not in attributes:
            raise ValueError('ApiProtocol is required')
        
        if f'_{name}__domain' not in attributes:
            raise ValueError('ApiDomain is required')

        if f'_{name}__sub_directories' not in attributes:
            raise ValueError('SubDirectories is required')
        
        if not isinstance(attributes[f'_{name}__sub_directories'], SubDirecotries):
            raise TypeError('__sub_directories is not SubDirecotries')
    
        return type.__new__(meta, name, bases, attributes)

    def __origin(self):
        return f'{self.__protocol}://{self.__domain}'

    def __getattr__(self, name):
        import pdb
        pdb.set_trace()
        if name in self.__sub_directories:
            return self.__url(name)
        return super().__getattr__(name)
    
    def __url(self, subdirectory):
        return f'{self.__origin}/{self.__sub_directories[subdirectory]}'
