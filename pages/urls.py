from django.urls import path
from .views import home, add, about

# Uygulamanin URL yönlendirmeleri
urlpatterns = [
    # '/home/' URL yoluna gelen istekler home görünüm fonksiyonuna yönlendirilir
    path('', home, name='home'),
    
    # '/add/' URL yoluna gelen istekler add görünüm fonksiyonuna yönlendirilir
    path('add/', add, name='add'),
    
    # '/about/' URL yoluna gelen istekler about görünüm fonksiyonuna yönlendirilir
    path('about/', about, name='about'),
]
