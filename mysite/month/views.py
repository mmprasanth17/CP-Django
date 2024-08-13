from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
# def index(request):
#     return HttpResponse("This Works!")

# def name(request):
#     return HttpResponse("My name is prasanth")

   #Another Method

month_schedule = {
    'january': 'Learning Python',
    'february': 'Learning .Net',
    'march': 'Learning Adv Python',
    'april': 'Learning Git',
}

def monthly_details_by_number(request, month):

    # return HttpResponse(month)

    months = list(month_schedule.keys())    #['january', 'february',.....]
    # redirect_month = months[month]
    # return HttpResponseRedirect('/month/'+redirect_month)
  


    if(month>len(months)):
        return HttpResponseNotFound('Invalid Month')
   
    redirect_month = months[month-1]
    redirect_path = reverse('month-details', args=[redirect_month])

    return HttpResponseRedirect(redirect_path)

    # return HttpResponseRedirect('/month/'+redirect_month)


def monthly_details(request, month):
    try:
        month_text = month_schedule[month]
        # responce_data = render_to_string('month_details/month.html') # or
        responce_data =render(request,'month_details/month.html',
        {
            "text" : month_text

        })

        return HttpResponse(responce_data)
    except:
        return HttpResponseNotFound('<h1>This is not mentioned<h1>')
    
def index(request):
    month = list(month_schedule.keys())
    render_responce = render(request,'month_details/index.html',{
            'month':month})
    return HttpResponse(render_responce)

    
