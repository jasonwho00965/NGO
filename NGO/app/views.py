from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import RegisterForm
from .forms import NameForm

from NGO.app.models import User


def get_name(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def home(request):
	users = User.objects.all()
	return render(request, 'home.html', {'users': users})


"""TODO: We need an event_detail.html page"""
def event_detail(request, id):
	try:
		event = Event.objects.get(id=id)
	except User.DoesNotExist:
		raise Http404('Event not found...')
	return render(request, '''event_detail.html''', {'event': event})
	pass