from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about_us, name='about_us'),
    path('category/<slug:slug>/', views.show_category, name='show_category'
    ),
    path('add_category', views.add_category, name='add_category'),
    path('category/<slug:slug>/add_page', views.add_page, name='add_page')
]


urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
