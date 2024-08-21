from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from .form import Feedbackform
from .models import Review
from django.views  import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView



# # Create your views here.

# # def index(request):
# #     return render(request,'userprofile/index.html')
# class FeedbackformView(View):
#     def feedbackform(request):
#         if request.method == 'POST': #True
#             # print("fhdfgj")
#             # enter_username = request.POST['username']
#             # print("fhdfgj")
#             # print(enter_username)
#             form = Feedbackform(request.POST)
    
#             # if enter_username == "":
#             #     return render(request,'userprofile/feedback.html',{
#             #         'haserror':True
#             #     })
#             if form.is_valid():
#                 review = Review(
#                     user_name = form.cleaned_data['user_name'],
#                     text = form.cleaned_data['text'],
#                     rating = form.cleaned_data['rating']
#                 )
#                 review.save()
#                 print(form.cleaned_data)
#                 return HttpResponseRedirect('thankyou')
#         else:    
#             form = Feedbackform()
    
#         return render(request,'userprofile/feedback.html',{
#             'form':form
#         })
 
class feedbackform(View):

    def get(self,request):
        form =Feedbackform()
        return render(request, "userprofile/feedback.html", {"form":form})

    def post(self,request):
        form =Feedbackform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("feedback")
        return render(request,"userprofile/feedback.html", {"form":form  })
        

 
#Thank_you

# def thanku(request):
#     return render(request,'userprofile/thank_you.html')
class ThankyouView (TemplateView):
    template_name = "userprofile/thank_you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = 'This works'
        return context


# Feedlist
class feedbacklistView(ListView):
    model = Review
    context_object_name = "reviews"
    template_name = "userprofile/feedlist.html"