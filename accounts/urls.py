from django.urls import path
from .views import register, login

urlpatterns = [
    # Kullanıcı kayıt sayfası için URL yapılandırması
    path('register/', register, name='register'),  # '/register/' yoluna gelen istekler register görünüm fonksiyonuna yönlendirilir
    
    # Kullanıcı giriş sayfası için URL yapılandırması
    path('login/', login, name='login'),  # '/login/' yoluna gelen istekler login görünüm fonksiyonuna yönlendirilir
]
