from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

week_schedule = {
    'sun':'This is Sunday',
    'mon':'This is Monday',
    'tues':'This is Tuesday',
    'wed':'This is Wednesday',
    'thur':'This is Thursday',
    'fri':'This is Friday',
    'sat':'This is Saturday',
}

def week(request,day):
    days = list(week_schedule.keys())

    if(day>len(week_schedule)):
        return HttpResponseNotFound('Enter 1-7')
    redirect_day = days[day-1]
    redirect_day = reverse('Days',args=[redirect_day])
    return HttpResponseRedirect(redirect_day)

def week_display(request,day):
    try:
        DAYS=week_schedule[day]
        return HttpResponse(DAYS)
    except:
        return HttpResponse('Not Found')