#This is a Code for Database...
#This is a part of the code
#You need the basic setup to run this code
#more info youtube

#FOR KICK COMMAND #3 






@client.command(aliases = ['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason=None):
	if reason == None:
		reason = "fall damage"
	await ctx.guild.kick(member)
	embed = discord.Embed(
		title="Kicked",
		description=f"{member.mention} fell from a high place",
		colour = discord.Colour.red())
	embed.add_field(name="reason:", value=reason, inline=False)
	await ctx.send(embed=embed)
