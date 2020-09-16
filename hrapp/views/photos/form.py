from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import Photo
from ..forms import PhotoForm

# @login_required
def photo_form(request):
    if request.method == 'GET':
        upload_form = PhotoForm()
        template = 'photos/form.html'
        context = {
            'upload_form': upload_form
        }

        return render(request, template, context)
