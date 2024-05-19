from django.http import HttpResponse, HttpRequest


def say_hello(request):
    return HttpResponse('Hello from Scaler - Rahul Hatwar')


def say_hello_with_name(request:HttpRequest, name):
    print(request.headers)
    print(request.path)
    print(request.content_params)
    return HttpResponse(f'Hello from scaler , {name}')
