import nextcord
from nextcord.ext import commands

from commands import delete_messages, who, ping, team_up, notifications

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

bot.add_command(ping.ping)
bot.add_command(delete_messages.delete_limited)
bot.add_command(delete_messages.delete_all)
bot.add_command(delete_messages.delete_mine)
bot.add_command(delete_messages.delete_mine_limited)
bot.add_command(who.whoareyou)
bot.add_command(who.whoami)
bot.add_command(who.whois)
bot.add_command(team_up.team_me)
bot.add_command(notifications.notify)

@bot.event
async def on_ready():
	print(f"This is {bot.user} with {bot.user.id} ID.")

@bot.event
async def on_message_edit(before, after):
	msg = f"**{before.author}** edited their message:\n{before.content} -> {after.content}"
	print(msg)
	await before.channel.send(msg)