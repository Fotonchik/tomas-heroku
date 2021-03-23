from django.db import models

class Post(models.Model):
    text=models.TextField()
    # python manage.py makemigrations posts
    #python manage.py migrate posts
    
    def __str__(self):
        """ Строковое отображение модели """
        return self.text[:50]
    