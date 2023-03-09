from django.shortcuts import render

# Create your views here.

def index(request):
    news = News.objects.all()
    return = render(request, 'news/index/html', {'news': news, 'title': })
