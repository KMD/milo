from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from usermanage.models import MyUser


def index(request):
    users = MyUser.objects.all()
    context = {'users': users}
    return render(request, "usermanage/index.html", context)


def show_user(request, id):
    my_user = MyUser.objects.get(id=id)
    context = {'user': my_user}
    return render(request, "usermanage/user.html", context)


class MyUserCreate(CreateView):
    model = MyUser
    fields = ['username', 'first_name', 'last_name', 'email', 'birthday']


class MyUserDelete(DeleteView):
    model = MyUser
    success_url = '/'


class MyUserUpdate(UpdateView):
    model = MyUser
    fields = ['username', 'first_name', 'last_name', 'email', 'birthday']
    template_name_suffix = '_update_form'
