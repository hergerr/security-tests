from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    string = "<script>alert('dzien dobry')</script>"
    return render(request, 'xss.html', {'string': string})


def param_string(request):
    param = request.GET.get('q', '')
    return render(request, 'param_string.html', {'param': param})
