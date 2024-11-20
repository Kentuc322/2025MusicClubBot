import asyncio
import json
import logging
import os
import subprocess
import sys

import discord
from discord.ext import commands

import lists

intents = discord.Intents.all()

discord.utils.setup_logging(level=logging.INFO, root=False)


def restart():
    print("\n---\nBlocked by API.\nRestarting now...\n")
    subprocess.call(["python", "restart/restarter.py"])


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="?",
            case_insensitive=True,
            intents=intents,
            activity=discord.Game("音楽部の統治"),
        )

    async def setup_hook(self):
        self.tree.copy_global_to(guild=discord.Object(1304826224828219422))
        await self.tree.sync()
        print("Commands synced!!")

    async def on_ready(self):
        print(f"Logged in as {self.user}")
        print("Good Morning!!!")


async def main():
    bot = MyBot()
    for cog in lists.cogs:
        await bot.load_extension(cog)

    # keep_alive.keep_alive()
    try:
        # await bot.start(os.getenv("TOKEN"))
        await bot.start(
            "MTMwNzg5NjY2NzcwOTY0MDcyNA.Gm3_rn.PZpaTa7JvZDgDVbXMZbYqSv9HhzWwjAOf0Qm8c"
        )
    except discord.errors.HTTPException:
        # restart()
        os.system("kill 1")


if __name__ == "__main__":
    asyncio.run(main())
