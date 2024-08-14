from django.shortcuts import render
from . models import author
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect


# Create your views here.

author_list = (author.objects.all())
auth_dict={}
for auth in author_list:
    auth_dict[auth.first_name]=auth
    
    
def index(request):
    auth = (author.objects.all())
    return render(request,'author_details/author_details.html',
                  {
                      'author' : auth
                  })
    
    
def author_details(request, author):
    try:
        auth_text = auth_dict[author]
        # responce_data = render_to_string('month_details/month.html') # or
        responce_data =render(request,'author_details/auth.html',
        {
            "text" : auth_text

        })

        return HttpResponse(responce_data)
    except:
        return HttpResponseNotFound('<h1>This is not mentioned<h1>')

# with slug method 

def author_slug(request, slug):
    try:
        auth_text = author.objects.get(slug=slug)
        responce_data =render(request,'author_details/auth.html',
        {
            "text" : auth_text

        })

        return HttpResponse(responce_data)
    except:
        return HttpResponseNotFound('<h1>This is not mentioned<h1>')
    

def author_info(request, id):
    try:
        # auth_value = author.objects.get(id=author)
        auth_value=author.objects.get(id=id)
        print(F'-------------{author}')
        
        response_data = render(request, 'author_details/auth.html', {
            "text": auth_value
        })
        return HttpResponse(response_data)
    except : 
        return HttpResponseNotFound('<h1>This is not mentioned</h1>') 
