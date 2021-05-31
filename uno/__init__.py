import collections
from typing import TypedDict, Coroutine, Any

import discord
import toml
from discord.ext import commands
from discord.ui import *

try:
    import aioredis
except ImportError:
    aioredis = None

from uno import util


__all__ = ["UNO"]


class _ConfigExists(TypedDict, total=False):
    redis: str


class Config(_ConfigExists):
    token: str
    prefix: list[str]
    owner_ids: list[int]


class UNO(commands.Bot):
    def __init__(self) -> None:
        with open("config.toml") as f:
            self.config: Config = toml.load(f)  # type: ignore

        intents = discord.Intents()
        intents.guilds = True
        intents.members = True
        intents.guild_messages = True
        intents.guild_reactions = True

        super().__init__(command_prefix=self.config['prefix'], owner_ids=self.config['owner_ids'],
                         intents=intents)

        self.load_extension("uno.game")
        self.load_extension("jishaku")
        self.stats = collections.Counter()

        if aioredis:
            self.redis = await aioredis.create_redis_pool(self.config.get("redis"))
        else:
            self.redis = None

    async def _check(self, ctx: commands.Context):
        if ctx.channel.id != 741656304359178271:
            return True

        if self.redis is None:  # testing
            return await self.is_owner(ctx.author)

        ids = [int(k.decode()) for k in await self.redis.smembers("whitelist")]
        return ctx.author.id in ids

    async def on_socket_response(self, msg):
        self.stats[msg.get('t')] += 1

    async def on_ready(self) -> None:
        print("HI")

    def run(self) -> None:
        super().run(self.config['token'])

    def logout(self) -> Coroutine[Any, Any, None]:
        return self.close()
