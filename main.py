import vk_api
import random
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_bot import VkBot

def write_msg(peer_id, message):
    session.method('messages.send', {'peer_id': peer_id, 'message': message, 'random_id': random.randint(0,999999999999)})
    
session = vk_api.VkApi(token='69a17e5303be5bc5218137622fa9684f6ac9b11d32f15c6b0b58cd3d1e1e8eee8ad89b443fb66c77d0c77')

#api = vk.get_api()
longpoll = VkBotLongPoll(session, 182437918)

print('Started!')


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:

        bot = VkBot()
        write_msg(event.message.peer_id, bot.new_message(event.message.text))