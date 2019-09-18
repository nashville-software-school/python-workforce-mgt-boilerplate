from django.shortcuts import render

def home(request):
    if request.method == 'GET':
        template = 'hrapp/home.html'
        context = {}

        return render(request, template, context)
