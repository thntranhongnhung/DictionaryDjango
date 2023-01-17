from django.http import HttpResponse
from django.template import loader
from .models import dictionary
from django.shortcuts import render,redirect
from dictionary.models import Layout 
from django.views.generic.list import ListView
from newspaper import Article
from django.views.decorators.csrf import csrf_exempt



def vocabulary(request):
    allvocabulary = dictionary.objects.all().values()
    template = loader.get_template('vocabulary.html')
    context= {
        'vocabulary':allvocabulary
    }
    return HttpResponse(template.render(context,request))

def details(request,word):
    idvocabulary= dictionary.objects.get(word=word)
    template = loader.get_template('details.html')
    context ={
        'vocabulary' : idvocabulary
    }
    return HttpResponse(template.render(context,request))

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def testing(request):
    voca = dictionary.objects.all().order_by('word').values()
    template= loader.get_template('template.html')
    context ={ 
        'vocabulary':voca,
    }
    return HttpResponse(template.render(context,request))

@csrf_exempt
def search(request):
    if request.method == "POST":
        search = request.POST['search']
        wordSearch = dictionary.objects.filter(word__contains=search)
       
        return render(request,
        'search.html',
        {'search':search,
        'wordSearch':wordSearch})
    else:
        return render(request,
        'search.html',
        {})       

    
   
