import discord 
from discord import app_commands
from discord.app_commands import CommandTree, Group
from discord import Interaction, app_commands
from command.cp_role import RoleCommand
from command.cp_voice import VoiceChannelCommand
from command.cp_server import ServerCommand
from command.property.application_property import ApplicationProperty
from command.modules.cp_voice.voice_process import VoiceProcess
import os


class CommandParrotVoice(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        application_dir = '{0}/application'.format(os.path.dirname(__file__))               
        self.__application_property = ApplicationProperty(application_dir)

    async def setup_hook(self):
        self.tree.add_command(RoleCommand(self.__application_property))
        self.tree.add_command(ServerCommand(self.__application_property))
        self.tree.add_command(VoiceChannelCommand(self.__application_property))

        my_guild = discord.Object(id=833290234891599872)
        self.tree.copy_global_to(guild=my_guild)
        await self.tree.sync(guild=my_guild)
        # await self.tree.sync()

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")
        
    # member: イベントを発生させたメンバーの情報が入る
    # before
    # async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    #     # print('ボイチャに変化あり')
    #     # print(f'before.channel: {before.channel}')
    #     # print(f'after.channel: {after.channel}')
    #     # print(f'member.voice.channel: {member.voice.channel}')
    #     # print(f'member.guild.voice_client: {member.guild.voice_client}')

    #     # if before.channel is not after.channel:
    #     #     pass
        
    #     # print('-----------------')
        
    #     pass
    
    async def on_message(self, message: discord.Message):
        print(message.content)
        # ボイスチャンネルに接続されているか確認
        if message.guild.voice_client == None:
            return 
        
        # テキストメッセージがボットの場合           
        if message.author.bot:
            return 
        
        # メッセージがボイスチャンネルと同じチャンネルでない場合処理を終了する
        if not message.channel.id == message.guild.voice_client.channel.id:
            return 
        
        # intentの取得が許可されてない場合はテキストは空になるので無視
        if message.content == '':
            return       
        
        guild_dir = os.path.join(self.__application_property.server_dir, str(message.guild.id))
        voice_line = VoiceProcess(guild_dir)

        if voice_line.process_check():
            # 読み上げボットが再生中じゃない場合に音声を再生する。   
            if not message.guild.voice_client.is_playing():
                sound_path = voice_line.create(message.content)

                if not sound_path == None:
                    message.guild.voice_client.play(discord.FFmpegPCMAudio(source = voice_line.create(message.content) , options = "-loglevel panic"))
                    return

                # 正規表現でテキストが無くなり、読むものがなかった場合は処理終了                
                else:
                    return
        
        # 音声を読み上げるうえで処理してはいけないタイミングの場合、処理終了
        else:
            return