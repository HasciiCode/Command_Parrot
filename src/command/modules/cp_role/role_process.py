import os
import discord

class RoleProcess:
    def __init__(self, guild_dir: str):
        self.__guild_dir = guild_dir
        self.__role_output_dir = os.path.join(self.__guild_dir, 'command_parrot/role')
        
        
    def process_check(self):
        # サーバーの初期化が行われていない場合、処理を終了
        if not os.path.isdir(self.__guild_dir):
            return False
        
        # ロール情報の格納先がない場合、処理を終了
        if not os.path.isdir(self.__role_output_dir):
            return False
        
        return True
    
    def create_role_file(self, role: discord.Role):
        output_file = os.path.join(self.__role_output_dir, str(role.id))
        
        # ロール情報ファイル
        with open(output_file, 'w') as file:
            pass
    
    def remove_role_file(self, role: discord.Role):
        remove_file = os.path.join(self.__role_output_dir, str(role.id))
        
        # 削除対象のロール情報ファイルがある場合は、削除し、Trueを返す。
        if os.path.isfile(remove_file):
            os.remove(remove_file)
            
            return True
        
        # 削除対象のロール情報ファイルが存在しない場合、Falseを返す。
        else:
            return False            
        
        