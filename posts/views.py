from django.views.generic import ListView

from .models import Post

class HomePageView(ListView):
    model=Post                  #Название модели
    template_name='home.html'   #Ссылка на шаблон