from django.shortcuts import render

# Create your views here.


def check_headers(request):
    print(request.headers)
    return ''
