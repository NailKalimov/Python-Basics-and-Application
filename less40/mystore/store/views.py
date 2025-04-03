from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import UserProfile


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            '''Every ModelForm also has a save() method. This method creates and saves a database object from
            the data bound to the form. A subclass of ModelForm can accept an existing model instance as the
            keyword argument instance; if this is supplied, save() will update that instance. If it’s not supplied,
            save() will create a new instance of the specified model:'''
            user_profile = form.save()
            return redirect('profile', user_profile.id)
    else:
        form = RegistrationForm()
    return render(request, 'store/register.html', {'form': form})


def profile(request, user_profile_id):
    user_profile = UserProfile.objects.get(id=user_profile_id)
    return render(request, 'store/profile.html', {'user_profile': user_profile})

def multiplication_table(request):
    start = end = 0
    if request.method == 'POST':
        if 'start' in request.POST and 'end' in request.POST:
            start = int(request.POST.get('start'))
            end = int(request.POST.get('end'))
    return render(request, 'store/multiplication_table.html', {'numbers': [i for i in range(start, end + 1)]})
