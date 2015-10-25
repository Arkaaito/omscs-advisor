from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return redirect('planner')

def planner(request):
    return render(request, "planner.html")