from django.shortcuts import render
from . models import author

# Create your views here.

def index(request):
    auth = (author.objects.all())
    return render(request,'author_details/author_details.html',
                  {
                      'author' : auth
                  })