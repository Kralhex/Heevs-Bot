from nextcord.ext import commands

from dateparser import parse
import datetime
import time

@commands.command(name="notify")
async def notify(ctx: commands.Context):
	content = str(ctx.message.content)

	# Trim command text
	content = content[len("/notify "):]

	# If there are mentions trim until them
	# Channels start with "<#" and User mentions start with "<@", only "<" is checked so order of those parameters are interchangable.
	if content.find("<") != -1:
		content = content[: content.find("<")]

	# Some clean up
	content = content.replace("on", "").replace("in", "").replace("at", "").replace("me", "").replace("by", "").replace("us", "")

	# Fuzzy parse time text
	notification_datetime = parse(date_string = content)
	if notification_datetime is None:
		notification_datetime = datetime.datetime.now()
		print(f"Couldn't parse {content}")
	
	# If a channel is provided/mentioned in the command text, use that channel to notify, oterwise use this channel instead.
	if ctx.message.channel_mentions:
		channel = ctx.message.channel_mentions[0]
	else:
		channel = ctx.channel
	
	# If there are members provided in command text, mention them in notification too.
	# Command author is always notified/mentioned.
	notify_message = f"It is time. {ctx.author.mention}"
	if ctx.message.mentions:
		for member in ctx.message.mentions:
			notify_message += f" {member.mention}"
	
	wait_time = (notification_datetime - datetime.datetime.now()).total_seconds()
	wait_time = wait_time if wait_time > 0 else 5
	# Confirmation message and notification
	await ctx.send(f"Okie dokie, will ping you in {channel.mention} at {notification_datetime.strftime('%H:%M:%S on %d %b %Y')}.")
	# This needs to be threaded \|/
	time.sleep(wait_time)
	await channel.send(content = notify_message)
