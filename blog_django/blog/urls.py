from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', all_articles, name='all_articles'),
    path('<int:id>/<slug:slug>/', get_article, name='get_article')

]