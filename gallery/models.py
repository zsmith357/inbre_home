from django.db import models

class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='background_images/')
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"Background Image {'Active' if self.active else 'Inactive'}"

    class Meta:
        verbose_name_plural = "Background Image"

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption

class SiteLink(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title

