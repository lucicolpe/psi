# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from data.models import Category, Workflow
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.defaultfilters import slugify

import json

import urllib
import urllib2

from django.conf import settings
from django.contrib import messages


# Create your views here.

def index(request):
    return workflow_list(request)

def base(request):
    return render(request, 'data/base.html')

def workflow_list(request, category_slug=None):
    # YOUR CODE GOES HERE
    # queries that fill, category, categories, workflows
    # and error
    categories = Category.objects.all()
    found = True
    error = ''
    if category_slug==None:
        category = None
        workflows_aux = Workflow.objects.all()

        if workflows_aux == None:
            found = False
            error = 'No hay workflows'
    else:
        category = Category.objects.get(slug = category_slug)
        workflows_aux = Workflow.objects.filter(category = category)
        if workflows_aux == []:
            found = False
            error = 'No hay workflows para la categoria ' + category['name']

    page = request.GET.get('page', 1)
    paginator = Paginator(workflows_aux, 13)

    try:
        workflows = paginator.page(page)
    except PageNotAnInteger:
        workflows = paginator.page(1)
    except EmptyPage:
        workflows = paginator.page(paginator.num_pages)

    list_categories = list(Category.objects.all())
    _dict = {
        'list_categories':list_categories,
        'category': category, # category associated to category_slug
        'categories': categories, # list with all categories
                                    # usefull to repaint the category
                                    # menu
        'workflows': workflows, # all workflows associated to category
                                    # category_slug
        'result': found, # False if no workflow satisfices the query
        'error': error # message to display if results == False
    }
    return render(request, 'data/list.html', _dict)

def workflow_detail(request, id, slug):
    workflows = list(Workflow.objects.filter(id = id, slug=slug))
    workflow = None
    result = False
    error = 'No existe workflow con id = '+id
    if workflows != []:
        workflow=workflows[0]
        result = True
        error = ''

    _dict={
        'result': result,
        'workflow': workflow,
        'categories': list(workflow.category.all()),
        'error':error
    }
    return render(request, 'data/detail.html', _dict)

def workflow_search(request):
    if request.method == 'POST':
        name=str(request.POST.get('key'))
        workflows = list(Workflow.objects.filter(slug=slugify(name)))
        workflow = None
        categories = None
        result = False
        error = 'No existe workflow con nombre '+ name
        if workflows != []:
            workflow=workflows[0]
            result = True
            error = ''
            categories=list(workflow.category.all())
        _dict={
            'result': result,
            'workflow': workflow,
            'error':error,
            'categories': categories ,
        }
        return render(request, 'data/detail.html', _dict)

def workflow_download (request,id,slug,count = True) :

    ''' Begin reCAPTCHA validation '''
    recaptcha_response = request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    result = json.load(response)
    ''' End reCAPTCHA validation '''

    if result['success']:
        messages.success(request, 'New comment added with success!')
    else:
        messages.error(request, 'Invalid reCAPTCHA. Please try again.')
        workflow=list(Workflow.objects.filter(id = id, slug=slug))[0]
        _dict={
            'workflow' : workflow,
            'categories': list(workflow.category.all()),
            'result': False,
            'error': 'Invalid reCAPTCHA. Please try again.'
        }
        return render(request, 'data/detail.html', _dict)


    workflow = list(Workflow.objects.filter(id = id))[0]
    workflow.downloads +=1
    workflow.views +=1
    workflow.save()

    response = HttpResponse ( workflow.json ,content_type="application/octet−stream")
    fileName = workflow.slug + '_file'
    response['Content-Disposition'] = 'inline; filename= %s'  %fileName
    return response


def workflow_download_json(request, id, slug):
    # SEARCH FOR THE WORKFLOW
    workflow = list(Workflow.objects.filter(id = id))[0]
    # with  workflow . id = id
    return HttpResponse(workflow.json ,content_type="application/octet-stream")
