from django.db import models

class Contacto(models.Model):

   name = models.CharField(max_length=15)
   email = models.EmailField(blank=True) 
   message = models.TextField()
     
   def __unicode__(self):
        return self.name
