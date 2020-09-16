from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from hrapp.models import Photo
from ..forms import PhotoForm

def photo_list(request):
    if request.method == 'POST':
        # TODO: Convert to model form validation? Doesn't seem to work this way
        # new_photo = Photo(
        #     title = request.POST["title"],
        #     description = request.POST["description"],
        #     image = request.POST["image"]
        #   )
        # new_photo.save()
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse('hrapp:photos'))
        else:
            print("you suck. Now what?", form.errors)
            return redirect(reverse('hrapp:photo_form'))

    elif request.method == 'GET':
        photos = Photo.objects.all()
        return render(request, 'photos/list.html', {"photo_list": photos})

def success(request):
    return HttpResponse('successfully uploaded')
