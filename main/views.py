from django.http.response import JsonResponse
from django.shortcuts import render

# def index(request):
#     return render(request, 'main/index.html', {})

def room(request, room_name):
    return render(request, 'main/room.html', {
        'room_name': room_name
    })


def create_message(request):
    return_dict = dict()
    print(request.POST)
    
    data = request.POST
    
    message = data.get('message')
    user_username =  data.get('user_username')
    datetime = data.get('datetime')
    roomname = data.get('roomname')
    
    Message.objects.create(text=message, user=user_username, date_time=datetime, roomname=roomname )
    return JsonResponse(return_dict)







from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

def send_message(user, message, room_name):
    async_to_sync(channel_layer.group_send)('1', {
                'type': 'chat_message',
                'message': message,
                # 'username': user,
            })
    print(user, message, room_name)



from .models import Message
from django.utils import timezone

def index(request):
    all_massages = Message.objects.all()
    for i in all_massages:
        now = timezone.now().strftime("%d-%m-%Y %H:%M:%S")
        date_time = i.date_time.strftime("%d-%m-%Y %H:%M:%S")

        send_message(i.user, i.text, i.roomname)
        # if date_time==now:
        #     print('!!!next')
        #     send_message(i.user, i.text, i.roomname)
        # i.delete()

    return render(request, 'main/index.html', {})








