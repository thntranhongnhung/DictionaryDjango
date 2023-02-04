from django.http import HttpResponse
from django.template import loader
from .models import dictionary
from django.shortcuts import render,redirect

from django.views.decorators.csrf import csrf_exempt



def vocabulary(request):
    allvocabulary = dictionary.objects.all().values()
    template = loader.get_template('vocabulary.html')
    context= {
        'vocabulary':allvocabulary
    }
    return HttpResponse(template.render(context,request))

def details(request,slug):
    idvocabulary= dictionary.objects.filter(slug__contains=slug)
    
    template = loader.get_template('details.html')
  
    context ={
        'vocabulary' : idvocabulary
    }
  
    return HttpResponse(template.render(context,request))

def home(request):
    voca = dictionary.objects.all().order_by('word').values()
    template= loader.get_template('home.html')
    context ={ 
        'vocabulary':voca,
    }
    return HttpResponse(template.render(context,request))

def testing(request):
    voca = dictionary.objects.all().order_by('word').values()
    template= loader.get_template('template.html')
    context ={ 
        'vocabulary':voca,
    }
    return HttpResponse(template.render(context,request))
def redirect_home(request):
    response = redirect('/home/')
    return response
@csrf_exempt
def search(request):
    if request.method == "POST":
        search = request.POST.get('search_text')
        language= request.POST.get('option_language')
        wordSearch = dictionary.objects.filter(word__contains=search).filter(language__contains=language)
        
        return render(request,
        'search.html',
        {'search':search,
        'language':language,
        'wordSearch':wordSearch,

        })
    else:
        return render(request,
        'search.html',
        {})       

    
   
