from django.contrib.auth.forms import UserCreationForm
from django.http.response import JsonResponse
from django.shortcuts import render, redirect

from .models import Message

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/chat/my_chat/')
    else:
        form = UserCreationForm()
        
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                
                return redirect('login')
        
        context = {'form':form}
        return render(request, 'main/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/chat/my_chat/')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('/chat/my_chat/')

        context = {}
        return render(request, 'main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def room(request, room_name):
    return render(request, 'main/room.html', {
        'room_name': room_name
    })


def create_message(request):
    return_dict = dict()

    data = request.POST
    
    message = data.get('message')
    user_username =  data.get('user_username')
    datetime = data.get('datetime')

    Message.objects.create(text=message, user=user_username, date_time=datetime )
    return JsonResponse(return_dict)
