import os

class ServerProperty:
    def __init__(self, guild_dir: str):
        self.__guild_dir = guild_dir
        self.__guild_app_dir = os.path.join(self.__guild_dir, 'command_parrot')

    @property
    def guild_dir(self):
        return self.__guild_dir

    @property
    def voice_dir(self):
        path = os.path.join(self.__guild_app_dir, 'voice')
        
        return path

    @property
    def role_dir(self):
        path = os.path.join(self.__guild_app_dir, 'role')
        
        return path 
              
            
    
