from chat.celery import app
from .models import Message
from django.utils import timezone
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

@app.task
def time_check():
    # check postponed messages
    all_delayed_messages = Message.objects.all()
    for i in all_delayed_messages:
        try:
            date_time = i.date_time.strftime("%d-%m-%Y %H:%M:%S")
            now = timezone.now().strftime("%d-%m-%Y %H:%M:%S")
            if now==date_time:
                send_message(i.user, i.text)
                i.delete()
        except:
            pass


@app.task
def send_message(user, message):
    # send postponed message
    async_to_sync(channel_layer.group_send)('my_chat', {
                'type': 'chat_message',
                'message': message,
                'username': user,
            })
