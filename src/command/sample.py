import discord
from discord import Interaction, app_commands
from discord.app_commands import CommandTree, Group

class RoleManager(Group):
    def __init__(self):
        super().__init__(name="group")

    @app_commands.command(name="cv-test-1", description="subcommand description")
    async def subcommand(self, interaction: Interaction, target_role: discord.Role):
        guild = interaction.guild
        role_name = target_role
        autorize_role = await guild.create_role(name=role_name)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True),
            autorize_role: discord.PermissionOverwrite(read_messages=True)
        }
        await guild.create_text_channel(target_role, overwrites=overwrites)
        await interaction.author.add_roles(autorize_role)
        
    @app_commands.command(name="cv-test-2", description="another command description")
    async def another_command(self, interaction: Interaction):
        await interaction.response.send_message("this is group another command")