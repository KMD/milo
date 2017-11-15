from django.shortcuts import render
from django.views.generic.edit import CreateView

from usermanage.models import MyUser


def index(request):
    return render(request, "usermanage/index.html", {})

def show_user(request, id):
    return render(request, "usermanage/index.html", {})


class MyUserCreate(CreateView):
    model = MyUser
    fields = ['username','first_name', 'last_name', 'email', 'birthday']
