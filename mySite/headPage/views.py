from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.db.models.query_utils import DeferredAttribute
from django.views.generic.list import ListView
from django.http import Http404

from .forms import UserForm, BookForm

from .models import Section, Article

import datetime
import random

class MyView(View):
    model = Article
    userForm = UserForm
    bookForm = BookForm
    template_name = 'headPage.html'
    context_object_name = 'articles'

    def get(self, request, *args, **kwargs):
        #body = 'Hello, World!' + MyView.current_datetime()
        #return HttpResponse(body)        
        randomNum1 = random.randint(0, 30)
        randomNum2 = random.randint(0, 100) 
        randomNum3 = random.randint(0, 100)  
        try:
            articles = self.model.objects.all()
        except Exception:
            raise Http404("ЭТО ЧТО ТО ЗА НАДПИСЬ")
            #raise RuntimeError('RuntimeError')
        rend = self.model.objects.count()
        context = {"latest_firstPage": randomNum2, "var_1" : randomNum3, "range": range(randomNum1), "rend" : rend, 'articles':articles, 'userForm':self.userForm, 'bookForm':self.bookForm,}
        return render(request, self.template_name, context=context)

    def my_view(self, request):
        if request:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        else:
            return HttpResponse('<h1>Page was found</h1>')
        
        return HttpResponse(status=201)

    @staticmethod
    def current_datetime():
        now = datetime.datetime.today()
        html = "<html><body><br> It is now: %s.</body></html>" % now
        return html

class MyIndexView(View):
    model = Section
    form = UserForm
    template_name = 'index.html'
    context_object_name = 'sections'
 
    def get(self, request, *args, **kwargs):
        sections = self.model.objects.all()
        count = self.model.objects.count()
        context = {'sections':sections,'count':count,'form':self.form} 
        return render(request, self.template_name, context=context)
 
class MySectionView(View):
    template_name = 'headPage/section.html'
 
    def get(self, request, *args, **kwargs):
        context = {}
        section = get_object_or_404(Section, section_url=self.kwargs['section'])
        
        context['section'] = section
 
        return render(request, template_name=self.template_name, context=context)
  
class MyArticleView(View):
    template_name = 'headPage/article.html'
 
    def get(self, request, *args, **kwargs):
        context = {}
        article = get_object_or_404(Article, id=self.kwargs['article_id'])
        
        context['article'] = article
 
        return render(request, template_name=self.template_name, context=context)

def index(request):
    if request.POST:
        #name = request.POST.get("name")
        # age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("if")
    else:
        return HttpResponse("else")