from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')    

def analyze(request):
    djtext = request.POST.get('textfield', 'default')
    checkcapitalize = request.POST.get('capitalize', 'off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcounter=request.POST.get('charcounter','off')

    if checkcapitalize == "on":
        capitalized = djtext.upper()  # Use the upper() method on the entire string
        params = {'purpose':'Capitalized',
              'analyzed_text': capitalized}
        return render(request, 'analyzer.html', params)
    elif(newlineremover=="on"):
        analyzed=''
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed=analyzed+char
        params={'purpose':'New line removed',
                'analyzed_text': analyzed
                }
        return render(request,'analyzer.html', params)
    elif(extraspaceremover == "on"):
        # analyzed=''
        analyzed=' '.join(djtext.split())
        params={'purpose':'Extra Space Removed',
                'analyzed_text': analyzed
                }
        return render(request,'analyzer.html', params)
    elif(charcounter == "on"):
        analyzed=0
        for char in djtext:
            if char !=' ':
                analyzed+=1
        params={'purpose':'Characters in the text are:',
                'analyzed_text': analyzed
                }
        return render(request,'analyzer.html', params)

    else:
        return HttpResponse('please go back and tick the capitalize box') # retain original text if not capitalizing
    
    


