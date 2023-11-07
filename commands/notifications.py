import nextcord
from nextcord.ext import commands

import time

@commands.command(name="notify")
async def notify(ctx: commands.Context, wait_time: int, channel: nextcord.TextChannel= None, *members: nextcord.Member):
	if not channel:
		channel= ctx.channel
	await ctx.send(f"Okie dokie, will ping you in {channel.mention} in {wait_time} seconds.")
	time.sleep(float(wait_time))
	notify_message = f"It is time. {ctx.author.mention}"
	if members:
		for member in members:
			notify_message += f" {member.mention}"
	await channel.send(content = notify_message)
