from nextcord.ext import commands

@commands.command(name="team_me")
async def team_me(ctx: commands.Context, teammate_no: int, game_name: str):
	channel = ctx.channel
	await channel.delete_messages([ctx.message])
	author = ctx.author
	if game_name in [channel.name for channel in ctx.guild.text_channels if channel.name == game_name]:
		channel = [channel for channel in ctx.guild.text_channels if channel.name == game_name][0]
	msg = f"<@{author.id}> is looking for {teammate_no} players to team up with in <#{channel.id}>"
	await channel.send(msg)