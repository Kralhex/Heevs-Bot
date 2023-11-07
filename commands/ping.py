from nextcord.ext import commands

@commands.command(name="ping")
async def ping(ctx: commands.Context, *arg):
	await ctx.send("Pong. Kidding. I am here, hit me up with any command you want.")