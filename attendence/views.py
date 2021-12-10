from django.db.models import query
from django.db.models.fields import BLANK_CHOICE_DASH
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import User
from attendence.my_scripts import *
# Create your views here.
def test_can(request):
    return render(request, "attendence.html", {})

def search_database(request):
    return render(request, "search_result.html", {})

class DisplayResultView (ListView):
    model = User
    template_name= 'display_result.html'

# class SearchResultView(ListView , )

def search_user_info(request):
    search = request.GET.get('search')
    blank = User.objects.filter(name=search).values_list()
    return render (request, 'attendence.html' , {'q':blank})


# class SearchResultView(ListView):
#     model = User
#     template_name="search_result.html"

#     def get_queryset (self):
#         #this query is the input from user that needs to be compared with the names in database
#         query = self.request.GET.get('q')
#         idx =1

#         while (idx < 5):
#             data_object= User.objects.filter(filedname=query)
            
#             idx+=1
      