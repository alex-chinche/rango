
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rango_app import views

app_name = 'rango_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('category/<slug:slug>/', views.show_category, name='show_category'
    ),
    path('add_category', views.add_category, name='add_category'),
    path('category/<slug:slug>/add_page/', views.add_page, name='add_page')
]


urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
