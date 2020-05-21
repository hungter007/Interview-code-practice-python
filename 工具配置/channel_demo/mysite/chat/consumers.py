# chat/consumers.py
# async
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    # 所有websocket链接用户拥有
    return_dict = {}

    async def connect(self):
        # 当前用户拥有这些数据
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.return_list = []
        self.uuid = ''
        print("connect return list = {}".format(self.return_list))
        print("connect uuid = {}".format(self.uuid))
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        print("before disconnect return list = {}".format(self.return_list))
        print("before disconnect dict return list = {}".format(self.return_dict[self.room_group_name]))
        print("before disconnect uuid = {}".format(self.uuid))
        for i in range(len(self.return_list)):
            if self.return_list[i]['uuid'] == self.uuid:
                del self.return_list[i]
                break
        print("disconnect return list = {}".format(self.return_list))
        print('disconnect dict return list = {}'.format(self.return_dict[self.room_group_name]))
        print("disconnect uuid = {}".format(self.uuid))
        self.return_dict[self.room_group_name] = self.return_list

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': self.return_list
            }
        )

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        print("before receive return list = {}".format(self.return_list))
        try:
            print("before receive dict return list = {}".format(self.return_dict[self.room_group_name]))
        except Exception as e:
            print(e)
        print("before receive uuid = {}".format(self.uuid))
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.uuid = message
        dict = {}
        try:
            self.return_list = self.return_dict[self.room_group_name]
            for i in range(len(self.return_list)):
                if self.return_list[i]['uuid'] == self.uuid:
                    self.return_list[i]['uuid'] = message
                    have_flag = 1
            if not have_flag:
                dict['uuid'] = message
                self.return_list.append(dict)
        except Exception as e:
            print(e)
            dict['uuid'] = message
            self.return_list.append(dict)
        self.return_dict[self.room_group_name] = self.return_list
        # Send message to room group
        print("receive return list = {}".format(self.return_list))
        print("receive dict return list = {}".format(self.return_dict[self.room_group_name]))
        print("receive uuid = {}".format(self.uuid))
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': self.return_list
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
# import json
#
# sync
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#
#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         self.accept()
#
#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#
#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#
#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']
#
#         # Send message to WebSocket
#         self.send(text_data=json.dumps({
#             'message': message
#         }))
