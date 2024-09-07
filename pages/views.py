from django.shortcuts import render
# Ana sayfa görünüm fonksiyonu
def home(request):
    # 'index.html' şablonunu render eder ve kullanıcıya ana sayfayı gösterir.
    return render(request, 'index.html')

# İçerik ekleme sayfası görünüm fonksiyonu
def add(request):
    # Bu fonksiyon, 'pages/add.html' şablonunu render eder.
    # İçerik ekleme işlemleri burada yapılabilir.
    return render(request, 'pages/add.html')

# Hakkımızda sayfası görünüm fonksiyonu
def about(request):
    # 'pages/about.html' şablonunu render eder ve Hakkımızda sayfasını gösterir.
    return render(request, 'pages/about.html')

'''
Django'daki views.py dosyasi, web uygulamanizin iş mantiğini ve kullaniciya gösterilecek içerikleri yönetir. "Görünümler" (views), web sayfalarinizin nasil oluşturulacağini ve hangi verilerin gösterileceğini belirleyen Python fonksiyonlaridir. 
İşte views.py dosyasinin nasil çaliştiği ve ne işe yaradiği hakkinda detayli bir açiklama:

views.py Dosyasinin Temel İşlevleri
HTTP İsteklerini İşleme:

Web tarayicisi veya başka bir istemci, bir HTTP isteği gönderdiğinde (örneğin, bir sayfayi ziyaret ettiğinde), Django bu isteği alir ve uygun bir yanit oluşturur.
views.py dosyasinda tanimladiğiniz fonksiyonlar, bu HTTP isteklerini alir, işleme alir ve uygun bir HTTP yaniti döndürür.
Görünüm Fonksiyonlari:

Her görünüm fonksiyonu bir HTTP isteği alir ve genellikle bir HTTP yaniti döndürür. Yanit, genellikle bir HTML şablonunun render edilmiş hali, bir JSON verisi veya başka bir veri formati olabilir.
render() fonksiyonu, belirli bir şablon dosyasini ve bu şablona gönderilecek verileri alir. Şablon dosyasi, kullaniciya gösterilecek HTML içeriğini tanimlar.
Şablonlari Kullanma:

Görünüm fonksiyonlari, render() işlevini kullanarak HTML şablonlarini render eder. Şablonlar, genellikle templates klasöründe bulunur ve HTML içeriğinizi tanimlar.
Şablonlari kullanarak, dinamik verileri (örneğin, kullanici adi, blog yazilari) HTML sayfalarina ekleyebilirsiniz.
Veri İşleme:

Görünüm fonksiyonlari, istekle birlikte gelen verileri işleyebilir. Örneğin, bir form gönderildiğinde, form verilerini alir, işler ve sonuçlari döndürebilir.
Form işlemleri, kullanici kayitlari veya başka etkileşimli içerikler burada işlenir.
Yönlendirme:

redirect() fonksiyonu, kullaniciyi başka bir URL'ye yönlendirmek için kullanilir. Genellikle bir form başariyla gönderildikten sonra veya bir işlem tamamlandiğinda kullanilir.
'''