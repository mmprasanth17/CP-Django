from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect


# Create your views here.

# def index(request):
#     return render(request,'userprofile/index.html')
def feedbackform(request):
    if request.method == 'POST': #True
        enter_username = request.POST['username']
        print(enter_username)
 
        if enter_username == "":
            return render(request,'userprofile/feedback.html',{
                'haserror':True
            })
 
        return HttpResponseRedirect('/form/thankyou/')
 
    return render(request,'userprofile/feedback.html')
 
def thanku(request):
    return render(request,'userprofile/thank_you.html')