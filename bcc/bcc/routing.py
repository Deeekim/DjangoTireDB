from django.urls import re_path
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class EchoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        # Echo back whatever is sent
        await self.send(text_data=json.dumps({"message": text_data}))

websocket_urlpatterns = [
    re_path(r"ws/echo/$", EchoConsumer.as_asgi()),
]
