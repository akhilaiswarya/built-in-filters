from django.shortcuts import render

# Create your views here.
import datetime
def filters(request):
    dt=datetime.datetime.now()
    d={'data':'myslef AkhilAiSWarya','dt':dt,'c':10}
    
    
    return render(request,'filters.html',d)