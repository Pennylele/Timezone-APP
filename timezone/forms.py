from django import forms
from .models import DateTime

class DateTimeForm(forms.ModelForm):

	# User_Date_Time = forms.CharField(input_formats=['%Y-%m-%d %H:%M'])

	class Meta:
		model = DateTime
		fields = ['User_Time_Zone', 'User_Date_Time']