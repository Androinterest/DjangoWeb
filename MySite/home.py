#Created by Ajay Patel

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #Get the Text
    formtext = request.POST.get('text','default')
    formpunc = request.POST.get('removepunc','off')
    formupper = request.POST.get('uppercase','off')
    analyzedtxt = " "
    entext = " "
    if formpunc == "on" and formupper == "off":
        #analyze the Text
        punchuations = '''()[],.$#%*&+-|?/'''
        for char in formtext:
            if  char not in punchuations:
                analyzedtxt = analyzedtxt + char
        params = {'analyzed_text':analyzedtxt}
        return render(request,'analyze.html',params)
    elif formupper == "on" and formpunc == "off":
        for char in formtext:
            analyzedtxt = analyzedtxt + char.upper()
            params = {'analyzed_text':analyzedtxt}
        return render(request,'analyze.html',params)
    elif formpunc == "on" and formupper == "on":
        punchuations = '''()[],.$#%*&+-|?/'''
        for char in formtext:
            if  char not in punchuations:
                analyzedtxt = analyzedtxt + char
        for char in analyzedtxt:
            entext = entext + char.upper()
        params = {'analyzed_text':entext}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse('No Selection Found')
