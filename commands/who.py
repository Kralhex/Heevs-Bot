from nextcord.ext import commands


@commands.command(name="who_are_you")
async def whoareyou(ctx: commands.Context):
	msg = f"Hello, I am {ctx.bot.user} with the ID {ctx.bot.user.id} created by Kralhex.\nMy prefix is {ctx.bot.command_prefix} and you can learn more about my commands with !help command."
	# msg += ("\n".join([command.name for command in ctx.bot.commands]))
	await ctx.send(msg)


@commands.command(name="who_am_i")
async def whoami(ctx: commands.Context):
	author = ctx.author
	msg = f"You are {author.name} with the ID {author.id}.\n"
	msg += f"You have created your nextcord account on {author.created_at:%d %B %Y } at {author.created_at:%H:%M } and joined this server on {author.joined_at:%d %B %Y } at {author.joined_at:%H:%M }.\n"
	await ctx.send(msg)


@commands.command(name="who_is")
async def whois(ctx: commands.Context, searched_id: int):
	searched = [member for member in ctx.guild.members if member.id == searched_id]
	if not searched:
		await ctx.send("Member not found.")
		return
	else:
		searched = searched[0]
	msg = f"They are {searched.name} with the ID {searched.id}.\n"
	msg += f"They have created their nextcord account on {searched.created_at:%d %B %Y } at {searched.created_at:%H:%M } and joined this server on {searched.joined_at:%d %B %Y } at {searched.joined_at:%H:%M }.\n"
	await ctx.send(msg)
