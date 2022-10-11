# I have created this file- Rajneesh
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check Checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~='''
        analyzed = ""
        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremover != "on" and newlineremover != "on" and fullcaps != "on" and removepunc != "on":
        return HttpResponse("<h1>You have not choosen any text analyzer option</h1>")
    return render(request, 'analyze.html', params)
