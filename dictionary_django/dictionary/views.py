from django.http import HttpResponse
from django.template import loader
from .models import dictionary

def vocabulary(request):
    allvocabulary = dictionary.objects.all().values()
    template = loader.get_template('vocabulary.html')
    context= {
        'vocabulary':allvocabulary
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    idvocabulary= dictionary.objects.get(id=id)
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
