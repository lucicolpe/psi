from django import forms
from data.models import Workflow, Category

class WorkflowForm(forms.ModelForm):
    #name,category, keywords, description y versionInit
    name = forms.CharField(max_length=128,help_text="Please enter the workflow name.")
    category = forms.ManyToManyField(Category, blank=False)
    keywords = forms.CharField(max_length=256, help_text="Please enter the workflow keywords.")
    description = forms.CharField(max_length=512, help_text="Please enter the workflow description.")
    versionInit = forms.CharField(max_length=512, help_text="Please enter the workflow versionInit.")

    slug = forms.SlugField(widget=forms.HiddenInput(),required=False)
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	downloads = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	client_ip = forms.GenericIPAddressField(widget=forms.HiddenInput())
	json = forms.TextField(widget=forms.HiddenInput(),max_length=512)
	created = forms.DateField(widget=forms.HiddenInput(),auto_now=True)

    class Meta:
		# Provide an association between the ModelForm and a model
		model = Workflow
		fields = ('name','category', 'keywords', 'description','versionInit',)
