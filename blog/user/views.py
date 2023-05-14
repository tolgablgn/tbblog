from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages


# Create your views here.





def register(request): #"request" burada Django web framework'ünün "views.py" dosyasındaki bir fonksiyonun argümanı olarak kullanılan bir değişkendir. Django'da, bir kullanıcı bir web sayfasını ziyaret ettiğinde, Django bir HTTP isteği (HTTP request) oluşturur ve bu istek, Django'nun "views.py" dosyasındaki uygun fonksiyona yönlendirilir. Bu fonksiyon, isteğin bilgilerine erişmek ve yanıt (response) olarak ne gösterileceğine karar vermek için bu isteği kullanır. "request" değişkeni, bu HTTP isteği hakkında bilgi içeren bir nesnedir ve bu fonksiyon tarafından kullanılabilir. Örneğin, bu değişken aracılığıyla kullanıcının IP adresine, kullanıcının tarayıcı bilgilerine, HTTP isteğinin yöntemine (GET, POST vb.) ve diğer ayrıntılara erişilebilir.
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            newUser = User(username = username)
            newUser.set_password(password)
            
            newUser.save()
            login(request,newUser)
            messages.info(request,"Başarıyla Kayıt Oldunuz..") #kayıt olduktan sonra ki flash mesajı..
            return redirect("index")
        context = {
            "form" : form
        }
        return render(request, "register.html",context)
    else:
        form = RegisterForm()
        context = {
            "form" : form
        }
        return render(request, "register.html",context)


    """
    form = RegisterForm()
    context = {
        "form": form
    }
    
    
    return render(request,"register.html",context)
"""
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı..")
            return render(request,"login.html",context)
        
        messages.success(request,"Başarıyla Giriş Yaptınız..")
        login(request,user)
        return redirect("index")
    
    return render(request,"login.html",context)


def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız..")
    return redirect("index")
