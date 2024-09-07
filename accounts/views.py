from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

def register(request):
    # Kullanıcı kayıt işlemi için görünüm fonksiyonu
    if request.method == 'POST':  # Form verisi gönderildiyse
        form = RegisterForm(request.POST)  # Formu POST verileri ile oluştur
        if form.is_valid():  # Formun geçerli olduğunu kontrol et
            form.save()  # Formu kaydet (kullanıcıyı oluştur)
            return redirect('login')  # Başarıyla kayıt edildikten sonra giriş sayfasına yönlendir
    else:
        form = RegisterForm()  # Formun boş bir örneğini oluştur
    return render(request, 'pages/register.html', {'form': form})  # Formu kayıt sayfasına gönder

def login(request):
    # Kullanıcı giriş işlemi için görünüm fonksiyonu
    if request.method == 'POST':  # Form verisi gönderildiyse
        form = LoginForm(request.POST)  # Formu POST verileri ile oluştur
        if form.is_valid():  # Formun geçerli olduğunu kontrol et
            # Oturum açma işlemi yapılabilir (bu örnekte, kullanıcıyı doğrudan yönlendiriyoruz)
            return redirect('home')  # Başarıyla giriş yapıldıktan sonra ana sayfaya yönlendir
    else:
        form = LoginForm()  # Formun boş bir örneğini oluştur
    return render(request, 'pages/login.html', {'form': form})  # Formu giriş sayfasına gönder
