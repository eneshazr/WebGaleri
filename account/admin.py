from django.contrib import admin
from django.db import models
# from django.contrib.auth.models import User
from .models import Galeri


class LISTELE(admin.ModelAdmin):
    list_display = ("bolge", "resim", "aciklama", "kategori")
    list_editable = ("resim", "kategori",)
    select_related = "bolge",

admin.site.register(Galeri, LISTELE)
