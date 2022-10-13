from django.shortcuts import render
from .models import Galeri

def index(request):
    DATA = {
        "yer": Galeri.objects.filter(kategori=0),
        "gok": Galeri.objects.filter(kategori=1),
        "derya": Galeri.objects.filter(kategori=2),
    }
    print(len(list(DATA["yer"])))
    return render(request, "index.html", DATA)
