from nextcord.ext import commands

@commands.command(name="delete_limited")
async def delete_limited(ctx, limit: int):
	channel = ctx.channel
	messages = [message async for message in channel.history(limit = limit)]
	await channel.delete_messages(messages)

@commands.command(name="delete_all")
async def delete_all(ctx):
	channel = ctx.channel
	messages = [message async for message in channel.history(limit = None)]
	await channel.delete_messages(messages)

@commands.command(name="delete_mine")
async def delete_mine(ctx):
	channel = ctx.channel
	author = ctx.author
	messages = [message async for message in channel.history(limit = None) if message.author is author]
	await channel.delete_messages(messages)

@commands.command(name="delete_mine_limited")
async def delete_mine_limited(ctx, limit: int):
	channel = ctx.channel
	author = ctx.author
	messages = [message async for message in channel.history(limit = limit) if message.author is author]
	await channel.delete_messages(messages)