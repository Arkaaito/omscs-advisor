from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def home(request):
    return redirect('planner')

def planner(request):
    return render(request, "planner.html")

def get_viewed_user(viewer, id=None):
    # TODO: permissions checking
    if id is not None:
        return User.objects.get(id=id)
    else:
        return viewer

@login_required()
def profile_info(request, viewed=None):
    viewed_user = get_viewed_user(request.user, viewed)
    if request.user == viewed_user:
        return render(request, "edit_info.html")
    else:
        return render(request, "info.html")

@login_required()
def profile_plan(request, viewed=None):
    viewed_user = get_viewed_user(request.user, viewed)
    if request.user == viewed_user:
        return render(request, "edit_plan.html")
    else:
        return render(request, "plan.html")