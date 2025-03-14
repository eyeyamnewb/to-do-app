from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

	class Meta:
		model = Task
		fields = '__all__'

class tasedatedue(forms.ModelForm):
	title= forms.widget

	class Meta:
		model = Task
		fields = ['duedate']


class bdayslect(forms.ModelForm):

    bday = forms.DateField(
    widget=SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),),)

class meta:
   model: extrauserdata
   fields['dob']



