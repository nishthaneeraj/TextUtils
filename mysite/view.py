# I have Created this file my self!
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    
def analyze(request):
    # get the text
    djtext = request.POST.get('text','default')
    #check checkboxes value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremove','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    #check which checkbox is on
    if removepunc == "on":
    # analyze the text
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed+char
        params = {'purpose':'Removed Punctuation', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed To UPPERCASE', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'Removed New Lines', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(extraspaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]== " "):
                analyzed = analyzed + char
        params = {'purpose':'Removed Extra Spaces', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(charcount=='on'):
        analyzed = ""
        counted = len(djtext)
        analyzed = f"Number Of Characters In your text is : {counted}"
        params = {'purpose':'Character Counted', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(removepunc != "on" and fullcaps !='on' and newlineremove != "on" and extraspaceremover !='on'):
        return HttpResponse('Please Select any of the operations and try again')


    # else:
    #     return HttpResponse('Error')

    return render(request, 'analyze.html', params)

