from django.shortcuts import render
from store.forms import StudentLoginForm
from store.forms import AdminLoginForm
from store.forms import RegisterForm
from store.models import Table
from django.contrib.auth.models import User

def studentlogin_view(request):
	d={}
	form=StudentLoginForm()
	d['form']=form
	if request.method=='POST':
		form=StudentLoginForm(request.POST)
		if form.is_valid():	
			#form.save()
			admn_no=form.cleaned_data['username']
			password=form.cleaned_data['password']
			#user=authenticate(admn_no=admn_no,password=password)
			#if user is not None:
			#	login
			#	return redirect('students_details')
			#else:
			#	return render(request,'Error.html')
	return render(request,'index.html',d) 



#admin login
def adminlogin_view(request):
	d={}
	form=AdminLoginForm()
	d['form']=form
	if request.method=='POST':
		form=AdminLoginForm(request.POST)
		if form.is_valid():	
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			#user=authenticate(admn_no=admn_no,password=password)
			#if user is not None:
			#	login
			#	return redirect('students_details')
			#else:
			#	return render(request,'Error.html')
	return render(request,'index.html',d) 



#register
def register_view(request):
	d={}
	form=RegisterForm()
	d['form']=form
	if request.method=='POST':
		form=RegisterForm(request.POST)
		if form.is_valid():	
			name=form.cleaned_data['name']
			password=form.cleaned_data['password']
			branch=form.cleaned_data['branch']
			year=form.cleaned_data['year']
			admn_no=form.cleaned_data['admn_no']
			
	return render(request,'index.html',d) 


# def log_p(request):
# 	print 'hello'
