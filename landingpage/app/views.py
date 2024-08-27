from django.shortcuts import render, redirect
from .models import user,Comment
from .forms import AddForm
from django.views.generic.edit import CreateView 

card_db = user.objects.all()
def landing_page(request):
    all_post=user.objects.all().order_by('-id')[:3]
    
    all_post = all_post[::-1]
    
    
    return render(request, 'app/landing.html',{'Postaa':all_post})

def card_details(request,post_id):
   
    # post_image = images[post_id]
    description_detail=user.objects.all().get(slug=post_id)
    comments=Comment.objects.filter(post_id=description_detail.id)
    return render(request, 'app/card_details.html', {'desc':description_detail,'comments':comments
        })

def all_post(request):
    all_post=user.objects.all()
    return render(request, 'app/all_post.html', {'Postaa':all_post
        })

def add_bike(request):
    if request.method == 'POST':
        form = AddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_post')
    else:
        form = AddForm(request.POST)
    
    return render(request, 'app/add_bike.html', {'form': form})

class commentCreateView(CreateView):
    model = Comment
    template_name = "app/comment.html"
    fields = '__all__'
    success_url ='/'
    