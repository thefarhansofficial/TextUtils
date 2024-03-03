# I have created this file  -farhan

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    #return HttpResponse("hello farhan")


def analyze(request):
    djtext = request.GET.get('text',"default")
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    charcount = request.GET.get('charcount','off')

    if removepunc == 'on':
        punctuations = ''' !()-[]{}::'"\,<>./?@ '''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'changed to uppercase','analyzed_text': analyzed}
        return render(request, 'analyze.html',params)
    elif(fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
    elif(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose': 'removed newlines','analyzed_text': analyzed}
        return render(request, 'analyze.html',params)
    elif(charcount=='on'):
        analyzed = len(djtext)
        params = {'purpose': 'count characters','analyzed_text': analyzed}
        return render(request, 'analyze.html',params)
    else:
        return HttpResponse("Error")