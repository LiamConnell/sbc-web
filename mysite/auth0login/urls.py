from django.urls import include, path

from . import views

app_name = 'auth0login'
urlpatterns = [
    path('idx/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('', include('django.contrib.auth.urls')),
    # path('', include('social_django.urls'))
]