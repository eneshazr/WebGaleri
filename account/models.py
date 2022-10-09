from django.db import models
from random import choices

class Galeri(models.Model):
    bolge = models.CharField("Bölge", max_length=45, null=False)
    resim = models.ImageField("Resim", upload_to="uploads", null=False)
    aciklama = models.TextField("Açıklama", null=True, blank=True)
    # kategoriSec = [(i, str(i)) for _, i in enumerate({"1":"Yer", "2":"Gök", "3":"Derya"})]
    kategoriSec = [(str(_), str(i)) for _, i in enumerate({"Yer", "Gök","Derya"})]
    kategori = models.CharField("Kategori", max_length=25, choices=kategoriSec)
    # print(kategoriSec)
    def __str__(self):
        return self.bolge

    class Meta:
        verbose_name_plural = "Galeri"
