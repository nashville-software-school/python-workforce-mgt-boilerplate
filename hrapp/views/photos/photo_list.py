from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from hrapp.models import Photo

def photo_list(request):
    if request.method == 'POST':
        new_photo = Photo(
            title = request.POST["title"],
            description = request.POST["description"],
            # NOTE! The image comes in on the FILES property of request, not POST
            image = request.FILES["image"]
          )

        new_photo.save()
        return redirect(reverse('hrapp:photos'))

    elif request.method == 'GET':
        photos = Photo.objects.all()
        return render(request, 'photos/list.html', {"photo_list": photos})

def success(request):
    return HttpResponse('successfully uploaded')
