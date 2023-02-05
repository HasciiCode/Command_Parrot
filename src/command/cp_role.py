import discord
from discord import Interaction, app_commands
from discord.app_commands import CommandTree, Group
from .property.application_property import ApplicationProperty

class RoleCommand(Group):
    def __init__(self,application_property: ApplicationProperty):
        super().__init__(name='cp-role')
        
    @app_commands.checks.has_permissions(manage_channels=True, manage_roles=True)
    @app_commands.command(name='get', description='実行した人に指定したロールの付与をします。')
    async def role_get(self, interaction: Interaction,guild_role: discord.Role):
        '''
        [fix]ロールが既に付与されているか確認の処理を入れる。
        '''
        try:
            await interaction.user.add_roles(guild_role)
            await interaction.response.send_message(f'{interaction.user.name}に{guild_role.name}を付与しました。')

            return        
        except discord.Forbidden:          
            await interaction.response.send_message(f'このコマンドの操作権限がありません。')
            return 
        except discord.HTTPException:
            await interaction.response.send_message(f'コマンドの操作に失敗しました。')
            return 
        
    @app_commands.checks.has_permissions(manage_channels=True, manage_roles=True)
    @app_commands.command(name='remove', description='実行した人から指定したロールを削除します(*チャンネルからロールは削除されません)。')
    async def role_remove(self, interaction: Interaction, guild_role: discord.Role):
        '''
        [fix]ロールが既に付与されているか確認の処理を入れる。
        '''
        try:
            await interaction.user.remove_roles(guild_role)
            await interaction.response.send_message(f'{interaction.user.name}から{guild_role.name}を削除しました。')
            return        
        except discord.Forbidden:
            await interaction.response.send_message(f'このコマンドの操作権限がありません。')
            return 
        except discord.HTTPException:
            await interaction.response.send_message(f'コマンドの操作に失敗しました。')
            return 
    
    @app_commands.command(name='register', description='[管理者権限] Command Parrotで操作できるロールの登録を行います。')
    @app_commands.checks.has_permissions(administrator=True)
    async def register(self, interaction: Interaction, guild_role: discord.Role):
        pass
    
    @app_commands.command(name='unregister', description='[管理者権限] Command Parrotに登録したロールの解除を行います。')
    @app_commands.checks.has_permissions(administrator=True)
    async def unregister(self, interaction: Interaction, guild_role: discord.Role):
        pass
    
    '''
    @app_commands.command(name='minimum-function', description='another command description')
    async def another_command(self, interaction: Interaction):
        await interaction.response.send_message('this is group another command')
    '''