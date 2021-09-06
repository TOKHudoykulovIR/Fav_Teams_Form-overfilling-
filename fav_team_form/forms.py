from django import forms
from .models import FormInfo

class RawFavTeamForm(forms.ModelForm):
	class Meta:
		model = FormInfo
		fields = '__all__'



