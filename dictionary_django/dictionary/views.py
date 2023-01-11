from django.http import HttpResponse
from django.template import loader
from .models import dictionary
from django.shortcuts import render,redirect
from dictionary.models import Layout 
from django.views.generic.list import ListView
from newspaper import Article
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

class SearchView(ListView):
    model = Article
    template_name = 'search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Article.objects.filter(title__contains=query)
          result = postresult
       else:
           result = None
       return result
   
