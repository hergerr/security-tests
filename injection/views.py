from django.shortcuts import render
from django.http import HttpResponse
from .forms import FileForm


def index(request):
    form = FileForm()
    string = "<script>alert('dzien dobry')</script>"
    return render(request, 'injection.html', {'form': form, 'string': string})
