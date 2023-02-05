import discord
from discord import Interaction, app_commands
from discord.app_commands import CommandTree, Group
from .property.application_property import ApplicationProperty
from .property.server_property import ServerProperty
import shutil
import os

class ServerCommand(Group):
    def __init__(self, application_property: ApplicationProperty):
        super().__init__(name="cp-server")
        self.__app = application_property

    @app_commands.command(name='authorize', description='Command Parrotの認証を行います。認証されていない場合はCommand Parrotを使用することはできません。')
    @app_commands.checks.has_permissions(administrator=True)
    async def authorize(self, interaction: Interaction):
        # guild_dir = '{0}/{1}'.format(self.__app.server_dir, str(interaction.guild_id))
        
        server_dir = os.path.join(self.__app.server_dir, str(interaction.guild_id))
        sever_property = ServerProperty(server_dir)
        is_authorised = True
            
        try:
            if not os.path.isdir(server_dir):
                os.mkdir(server_dir)
                is_authorised = False
            
            if not os.path.isdir(sever_property.voice_dir): 
                os.makedirs(sever_property.voice_dir)
                is_authorised = False
            
            if not os.path.isdir(sever_property.role_dir): 
                os.makedirs(sever_property.role_dir)
                is_authorised = False

            if is_authorised:            
                await interaction.response.send_message("このサーバーは既に認証済みです。")
            else:
                await interaction.response.send_message("このサーバーの初期化に成功しました。")
                
            return
        
        except FileExistsError:
            await interaction.response.send_message('初期化に失敗しました。再度/cp-server authorizeコマンドを使用して初期化してください。')
            return