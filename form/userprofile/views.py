from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from .form import Feedbackform
from .models import Review

# Create your views here.

# def index(request):
#     return render(request,'userprofile/index.html')
def feedbackform(request):
    if request.method == 'POST': #True
        # print("fhdfgj")
        # enter_username = request.POST['username']
        # print("fhdfgj")
        # print(enter_username)
        form = Feedbackform(request.POST)
 
        # if enter_username == "":
        #     return render(request,'userprofile/feedback.html',{
        #         'haserror':True
        #     })
        if form.is_valid():
            review = Review(
                user_name = form.cleaned_data['user_name'],
                text = form.cleaned_data['text'],
                rating = form.cleaned_data['rating']
            )
            review.save()
            print(form.cleaned_data)
            return HttpResponseRedirect('thankyou')
    else:    
        form = Feedbackform()
 
    return render(request,'userprofile/feedback.html',{
        'form':form
     })
 
def thanku(request):
    return render(request,'userprofile/thank_you.html')