from django.shortcuts import render

# Create your views here.


def homeView (request):
    if not request.user.is_authenticated():
        return render(request, 'registration/login.html')
    else:
        return render(request, 'home/index.html')

