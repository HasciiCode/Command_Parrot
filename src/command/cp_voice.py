import discord
from discord import Interaction, app_commands
from discord.app_commands import Group
from .property.application_property import ApplicationProperty

class VoiceChannelCommand(Group):
    def __init__(self, application_property: ApplicationProperty):
        super().__init__(name="cp-voice")
        self.app = application_property

    @app_commands.command(name='connect', description='指定したボイスチャンネルに接続します。')
    @app_commands.rename(voice_channel='接続するボイスチャンネル')
    async def connect(self, interaction: Interaction, voice_channel: discord.VoiceChannel):
        voice_client = discord.utils.get(interaction.client.voice_clients, guild=interaction.guild)        
       
        if not voice_client == None:
            await interaction.response.send_message(f'ボイスチャンネル\"{voice_client.channel}\"に接続されているため、"{voice_channel.name}"に接続することができません。') 
            return 

        await voice_channel.connect(timeout=30.0, reconnect=False)
        voice_client = discord.utils.get(interaction.client.voice_clients, guild=interaction.guild)
        await interaction.response.send_message(f'\"{voice_client.channel}\"に接続しました。') 
    
    @app_commands.command(name="disconnect", description="読み上げ機能の切断をします。")
    async def disconnect(self, interaction: Interaction):
        voice_client = discord.utils.get(interaction.client.voice_clients, guild=interaction.guild)

        await interaction.guild.voice_client.disconnect() 
        await interaction.response.send_message(f'ボイスチャンネル{voice_client.channel}から切断しました。')

    '''
    英訳機能
    コンテキストの取得が有効か確認するデコレータ必要
    '''    
    # @app_commands.command(name="translate", description="テキストを翻訳します。")
    # @app_commands.choices(
    #     language=[
    #         discord.app_commands.Choice(name='English', value='en-US'),
    #         discord.app_commands.Choice(name='Japanese', value='ja')
    #     ]
    # )    
    # @app_commands.rename(text='翻訳するテキスト')
    # async def translate(self, interaction: Interaction, language: str, text: str):
        
    #     if len(text) > 250:
    #         await interaction.response.send_message(f'Text limitation; upto 250 characters')
    #         return 
        
    #     if language == 'en-US':
    #         translate_lang = discord.Locale.american_english
    #     elif language == 'ja':
    #         translate_lang = discord.Locale.japanese
        
    #     translated_text = interaction.translate(translate_lang)
    #     await interaction.response.send_message(f'Text: {text}\n Translation: {translated_text}')
        
    