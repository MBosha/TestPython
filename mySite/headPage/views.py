from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.db.models.query_utils import DeferredAttribute
from django.views.generic.list import ListView

from .models import Section, Article

import datetime
import random

class MyView(View):
    model = Article
    template_name = 'headPage.html'
    context_object_name = 'articles'

    def get(self, request, *args, **kwargs):
        #body = 'Hello, World!' + MyView.current_datetime()
        #return HttpResponse(body)        
        randomNum1 = random.randint(0, 30)
        randomNum2 = random.randint(0, 100) 
        randomNum3 = random.randint(0, 100)        
        articles = self.model.objects.all()
        rend = self.model.objects.count()
        context = {"latest_firstPage": randomNum2, "var_1" : randomNum3, "range": range(randomNum1), "rend" : rend, 'articles':articles}
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
    template_name = 'index.html'
    context_object_name = 'sections'
 
    def get(self, request, *args, **kwargs):
        """
        the_data={}
        the_data1={}        
        all_lessons= self.model.objects.all()
        for lesson in all_lessons:
            the_data1[lesson]=all_lessons.all()
            for section in the_data1[lesson]:
                the_data[lesson][section]=section
                context={'the_data':the_data,}
        """
        sections = self.model.objects.all()
        count = self.model.objects.count()
        context = {'sections':sections,'count':count,}
        
        #context += str(self.model.section_title)
        #context += self.model.section_url
        #context += self.model.section_description
        #context = {Section.section_description, Section.section_title, Section.section_url}
        #context['section_list'] = Section.Meta.db_table.__getitem__#.Meta.db_table.objects.all().order_by('section_title')
        #body = 'Hello, Index!<br>'
        #body1 = context[0]
        #body2 = body1.blank
        #body += body2
        #body = render_to_string('index.html', {'section_list' : context})
 
        return render(request, self.template_name, context=context)
        #return HttpResponse(context)
 
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