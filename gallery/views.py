from django.shortcuts import render
from .models import GalleryImage, SiteLink, BackgroundImage

def index(request):
    images = GalleryImage.objects.all()
    links = SiteLink.objects.all()
    background_image = BackgroundImage.objects.filter(active=True).first()
    return render(request, 'index.html', {
        'images': images,
        'links': links,
        'background_image': background_image,
})
