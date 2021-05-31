import collections
from typing import TypedDict, Coroutine

import toml
from discord.ext import commands
from discord.ui import *


__all__ = ["UNO"]


class Config(TypedDict):
    token: str
    prefix: list[str]
    owner_ids: list[int]


class UNO(commands.Bot):
    def __init__(self) -> None:
        with open("config.toml") as f:
            self.config: Config = toml.load(f)  # type: ignore

        super().__init__(command_prefix=self.config['prefix'], owner_ids=self.config['owner_ids'])
        self.load_extension("uno.game")
        self.load_extension("jishaku")
        self.stats = collections.Counter()

    async def on_socket_response(self, msg):
        self.stats[msg.get('t')] += 1

    async def on_ready(self) -> None:
        print("HI")

    def run(self) -> None:
        super().run(self.config['token'])

    def logout(self) -> Coroutine[None, None, None]:
        return self.close()
