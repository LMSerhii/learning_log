from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """  """
    if request.method == 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            user_name = form.save()
            login(request, user_name)
            return redirect(request, 'learning_logs:index')

    context = {'form': form}

    return render(request, 'registration/register.html', context)



