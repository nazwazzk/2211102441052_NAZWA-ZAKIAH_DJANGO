from django.shortcuts import render

def home(request):
    template_name = "halaman/index.html"
    context = {
        'title':'MOOSIX'
    }

    return render(request, template_name, context)

def about(request):
    template_name = "about.html"
    context = {
        'title':'selamat datang di about'
    }

    return render(request, template_name, context)