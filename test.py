import botpy
from botpy.message import Message
from qqbot.core.util.yaml_util import YamlUtil
import os

class MyClient(botpy.Client):
    async def on_at_message_create(self, message: Message):
        await self.api.post_message(channel_id=message.channel_id, content="content")

robot_config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "config.yaml"))

intents = botpy.Intents(public_guild_messages=True) 
client = MyClient(intents=intents)
client.run(appid=robot_config["token"]["appid"], secret=robot_config["token"]["secret"])