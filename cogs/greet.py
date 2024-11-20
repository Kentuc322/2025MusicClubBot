import discord
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content
        channel = message.channel
        author = message.author

        print(f"{author} said : \n{msg}")

        if author.bot:
            return

        if msg == "Hey":
            await channel.send("|ω・｀)ﾉ ﾔｧ")
            return


async def setup(bot):
    await bot.add_cog(Greetings(bot))
