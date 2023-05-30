from django.db import models

# Create your models here.

class Post(models.Model):
    titolo = models.CharField(max_length=100)
    descr = models.TextField()
    
    def __str__(self):
        return str(self.titolo)

    class Meta:
        verbose_name_plural = 'Posts'
    