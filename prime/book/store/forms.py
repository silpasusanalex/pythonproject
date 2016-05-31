from django import forms
from store.models import Table

		
					
class StudentLoginForm(forms.Form):
	admn_no=forms.IntegerField()
	password=forms.CharField(widget=forms.PasswordInput())
class AdminLoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput())

class  RegisterForm(forms.Form):
	name=forms.CharField()
	admn_no=forms.IntegerField()
	password=forms.CharField(widget=forms.PasswordInput())
	branch=forms.CharField()
	year=forms.DateField()
# class RegisterForm(forms.ModelForm):	
# 	class Meta:
# 		model=Table
# 		fields=['name','admn_no','password','branch','year']		

