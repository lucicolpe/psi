#populate database
# This code has to be placed in a file within the
# data/management/commands directory in your project.
# If that directory doesn't exist, create it.
# The name of the script is the name of the custom command,
# so let's call it populate.py. Another thing that has to be done
# is creating __init__.py files in both the management and commands
# directories, because these have to be Python packages.
#
# execute python manage.py  populate

import os, django, random
os.environ.setdefault('DJANGO SETTINGS MODULE','data.settings')
django.setup()

from django.core.exceptions import ObjectDoesNotExist

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from data.models import Category, Workflow

from data.management.commands.populate import getJson


#models
CATEGORY = 'category'
USER = 'user'
WORKFLOW = 'workflow'
lista_categories=[]
# The name of this class is not optional must  be Command
# otherwise manage.py will not process it properly
class Command(BaseCommand):
    #  args = '<-no arguments>'
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = 'This scripts populates de workflow database, no arguments needed.' \
           'Execute it with the command line python manage.py populate'

    def getParragraph(self, init, end):
        # getParragraph returns a parragraph, useful for testing
        if end > 445:
            end = 445
        if init < 0:
            init = 0
        return """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum."""[init:end]

    # handle is another compulsory name, This function will be
    # executed by default
    def handle(self, *args, **options):
        self.query1()
        self.query2()
        self.query3()
        self.query4()
        self.query5()
        self.query6()
        self.query7()
        self.query8()

    #Cree una categoria llamada category 1 en caso de que no exista
    def query1(self):
        name = "category 1"
        slug = slugify(name)
        tooltip = ""
        try:
            c = Category.objects.get(slug = slug)
        except ObjectDoesNotExist:
            c = Category.objects.create(name=name, tooltip= tooltip)
            c.save()
            lista_categories.append(c)

    #Cree una categoria llamada category 2 en caso de que no exista
    def query2(self):
        name = "category 2"
        slug = slugify(name)
        tooltip = ""
        try:
            c = Category.objects.get(slug = slug)
        except ObjectDoesNotExist:
            c = Category.objects.create(name=name, tooltip= tooltip)
            c.save()
            lista_categories.append(c)
    # En caso de no existir cree tres workflows llamados workflow 11, workflow 12 y workflow 13que pertenezca a la categoria category 1
    def query3(self):
        names = ["workflow 11", "workflow 12", "workflow 13"]
        slugs = [slugify(names[0]), slugify(names[1]), slugify(names[2])]
        category = Category.objects.get(name = "category 1")
        for i in range(0,3):
            try:
                w = Workflow.objects.get(slug = slugs[i])
                if not category in w.category.all():
                    w.category.add(category)
            except ObjectDoesNotExist:
                w = Workflow.objects.create(name = names[i], client_ip="0.0.0.0", json = getJson())
                w.save()
                w.category.add(category)

    # En caso de no existir cree tres workflows llamados workflow 21, workflow 22 y workflow 23 que pertenezca a la categoria category 2
    def query4(self):
        names = ["workflow 21", "workflow 22", "workflow 23"]
        slugs = [slugify(names[0]), slugify(names[1]), slugify(names[2])]
        category = Category.objects.get(name = "category 2")
        for i in range(0,3):
            try:
                w = Workflow.objects.get(slug = slugs[i])
                if not category in w.category.all():
                    w.category.add(category)
            except ObjectDoesNotExist:
                w = Workflow.objects.create(name = names[i], client_ip="0.0.0.0", json = getJson())
                w.save()
                w.category.add(category)

    #Realice una consulta que devuelva un listado con todos los workflows asociados a la categoria category 1.
    def query5(self):
        category = Category.objects.get(name = "category 1")
        workflows = Workflow.objects.filter(category = category)
        return workflows

    #imprime resultado consulta 5
    def query6(self):
        workflows = self.query5()
        print "Los workflows asociados a la categoria 'category 1' son:"
        for workflow in workflows:
            print workflow

    # Realice una consulta que dado el workflow con slug=workflow-1 nos permita obtener la categoria a la que pertenece el workflow.
    def query7(self):
        w = Workflow.objects.get(slug = "workflow-1")
        # puede haber varias, asique pongo [0]
        return w.category.all()[0]

    #Repite la consulta anterior usando el workflow con nombre workflow 10 (el cual no existe).
    def query8(self):
        slug = "workflow_10"
        try:
            w = Workflow.objects.get(slug = slug)
        except ObjectDoesNotExist:
            print "workflow " + slug + " inexistente"
