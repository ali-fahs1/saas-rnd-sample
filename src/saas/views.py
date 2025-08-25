from django.http import HttpResponse
from visits.models import PageVisit


from django.shortcuts import render
def home_page_view(request,*arg,**kwargs):
    page_visits_nb=PageVisit.objects.filter(path=request.path).count
    total_visits_nb=PageVisit.objects.all().count
    PageVisit.objects.create(path=request.path)
    path=request.path
    return  render(request,'home.html',context={'name':'ali',"page_visits_nb":page_visits_nb,"total_visits_nb":total_visits_nb})