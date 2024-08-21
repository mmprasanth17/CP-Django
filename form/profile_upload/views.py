from django.shortcuts import render
from .forms import Profileform
from django.http import HttpResponseRedirect
from django.views import View
from .models import Profileimage


# Create your views here.
# from django.http import HttpResponseRedirect

# def home(request):
#     return render(request,'profile_upload/upload.html')

# # def store_file(file):
# #     with open('temp/userimage.jpg','+wb') as dest:
# #         for chunk in file.chunks():
# #             dest.write(chunk)
 
# class CreateProfileView(View):
#     def get(self, request):
#         form = Profileform()
 
#         return render(request,'profile_upload/upload.html',{
#             'form':form
#         })
 
#     def post(self, request):
#         submittedform = Profileform(request.POST,request.FILES)
 
#         if submittedform.is_valid():
#             # store_file(request.FILES['userimage'])
#             profile = Profileimage(userimage=request.FILES['userimage'])
#             profile.save()
#             return HttpResponseRedirect('/profile')
#         return render(request,'profile_upload/upload.html',{
#             'form':submittedform
#         })

from django.views.generic.edit import CreateView
class CreateProfileView(CreateView):
    model = Profileimage
    template_name = "profile_upload/upload.html"
    success_url ='/profile/'
    fields ="__all__"