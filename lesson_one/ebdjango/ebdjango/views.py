from django.http import HttpResponse 

def hello(request):
    return HttpResponse("Hello World!!!!!!!!!")


# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")