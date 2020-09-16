from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrapp.models import Photo
from ..forms import PhotoForm

# @login_required
def photo_form(request):
    if request.method == 'GET':
        upload_field = PhotoForm()
        template = 'photos/form.html'
        context = {
            'upload_field': upload_field
        }

        return render(request, template, context)
