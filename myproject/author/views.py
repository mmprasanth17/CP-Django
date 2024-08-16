from django.shortcuts import render
from . models import author
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.db.models import Avg


# Create your views here.

author_list = (author.objects.all())
auth_dict={}
for auth in author_list:
    auth_dict[auth.first_name]=auth
    
    
def index(request):
    auth = (author.objects.all())

    #AVERAGE RATING FINDING
    avg_rating = round(author.objects.aggregate(Avg('rating'))['rating__avg'],2)
    #TOTAL AUTHOR
    tol_author = author.objects.count()
    return render(request,'author_details/author_details.html',
                  {
                      'author' : auth,
                      'avg_rating':avg_rating,
                      'tol_author':tol_author,
                    
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
#eg.prasanth-mani o/p in http link we will see this 
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
    
#geting user by id value
def author_info(request, id):
    try:
        # auth_value = author.objects.get(id=author)
        auth_value=author.objects.get(id=id)
        
        response_data = render(request, 'author_details/auth.html', {
            "text": auth_value
        })
        return HttpResponse(response_data)
    except : 
        return HttpResponseNotFound('<h1>This is not mentioned</h1>') 
