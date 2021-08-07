# Create your tasks here

from chat.celery import app
from .models import Message

from django.utils import timezone

@app.task
def time_check():
    all_delayed_messages = Message.objects.all()
    for i in all_delayed_messages:
        try:
            date_time = i.date_time.strftime("%d-%m-%Y %H:%M:%S")
            now = timezone.now().strftime("%d-%m-%Y %H:%M:%S")

            if now==date_time:
                
                send_message(i.user, i.text, i.roomname)
                # i.delete()

        except:
            pass

from channels.layers import get_channel_layer

from asgiref.sync import async_to_sync

@app.task
def send_message(user, message, room_name):
    channel_layer = get_channel_layer()
    # layer = get_channel_layer()
    # layer.group_send(room_name, message)

    async_to_sync(channel_layer.group_send)(room_name, {
                'type': 'chat_message',
                'message': message,
                'username': user,
            })
    print("SEND")


