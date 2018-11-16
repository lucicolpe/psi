# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from data.models import Category, Workflow
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json
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
    paginator = Paginator(workflows_aux, 8)

    try:
        workflows = paginator.page(page)
    except PageNotAnInteger:
        workflows = paginator.page(1)
    except EmptyPage:
        workflows = paginator.page(paginator.num_pages)

    _dict = {'category': category, # category associated to category_slug
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
    workflows = Workflow.objects.filter(id = id, slug=slug)
    workflow = None
    result = False
    error = 'No existe workflow con id = '+id
    if workflow != []:
        workflow=workflows[0]
        result = True
        error = ''

    _dict={
        'result': result,
        'workflow': workflow,
        'error':error
    }
    return render(request, 'data/detail.html', _dict)
