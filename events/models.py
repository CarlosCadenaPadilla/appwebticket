from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="titulo")
    #description = models.TextField(verbose_name="descripcion")
    description = RichTextField(verbose_name="descripcion")
    image = models.ImageField(verbose_name="imagen", upload_to="events")
    link = models.URLField(null=True,blank=True, verbose_name="Direccion Web") 
    created = models.DateTimeField(auto_now_add=True,verbose_name="fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="fecha de edicion")
    

    class Meta:
        verbose_name = "evento"
        verbose_name_plural = "eventos"
        ordering = ["-created"] 

    def __str__(self):
        return self.title    

#@property
#def image_url(self):
#    if self.image and hasattr(self.image, 'url'):
#        return self.image.url