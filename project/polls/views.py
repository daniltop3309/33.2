from django.shortcuts import render, redirect
from .forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import PostList


def former(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'index.html', {'form': form})


def index(request):
    posts = PostList.objects.all()
    return render(request, 'index1.html', {'plist': posts})
