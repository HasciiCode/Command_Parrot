import os

class ApplicationProperty:
    '''
    
    '''
    def __init__(self, application_root_dir: str):
        self.__application_path = application_root_dir
    
    '''
    # def application_dir
    type: property
    return: application root directiory path
    '''
    @property
    def application_dir(self):      
        return self.__application_path

    @property
    def system_dir(self):
        path = '{0}/system'.format(self.__application_path)        
        return path
            
    @property
    def server_dir(self):
        path = '{0}/server'.format(self.__application_path)
        return path
    
