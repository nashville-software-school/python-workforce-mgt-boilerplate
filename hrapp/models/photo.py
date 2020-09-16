from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    # 'upload_to' will specify which directory the images should live in. By default django creates the directory under the 'media' directory which will be automatically created when we upload an image. No need to make media directory ourselves.
    image = models.ImageField(upload_to='images/', null=True, blank=True)
