from django.shortcuts import render,redirect
from rms.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.


def Base(request):
  
  language = Language.objects.all()
  hr_fm_data = HR_Interview_Declaration.objects.filter(hr_employ_id=request.session['hr_employ_id'])
     
  user_id = request.session.get('user_id')
  username = request.session.get('username')
  profile_pic = request.session.get('profile_pic')

  context = {
        'user_id': user_id,
        'username': username,
        'profile_pic': profile_pic,
          }
  
  
  return render(request, 'base.html',{'udata':request.session['hr_employ_id'],'context':context,'hr_fm_data':hr_fm_data})

def HR_Home(request):
    language = Language.objects.all()
    if request.session.has_key('hr_employ_id'):
      
      hr_fm_data = HR_Interview_Declaration.objects.filter(hr_employ_id=request.session['hr_employ_id'])
     
      user_id = request.session.get('user_id')
      username = request.session.get('username')
      profile_pic = request.session.get('profile_pic')

      context = {
          'user_id': user_id,
          'username': username,
          'profile_pic': profile_pic,
      }
      
      return render(request, 'index.html', {'udata':request.session['hr_employ_id'],'context':context, 'hr_fm_data':hr_fm_data, 'language':language})
    
    
    else:
      return redirect('hr_login')
 
def hr_registration(request):
    if request.method == 'POST':
        hr_employ_id = request.POST.get('hr_employ_id')
        hr_name = request.POST.get('hr_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image') 
        
        
    # ...
 
        # Assuming 'image' is the field name for the profile picture

        if HR_Registration.objects.filter(hr_employ_id = hr_employ_id).exists():
          messages.error(request, 'employee_id already exists')
          return redirect('hr_registration')
        
        if HR_Registration.objects.filter(hr_name = hr_name).exists():
          messages.error(request, 'hr name already exists')
          return redirect('hr_registration')
        
        if HR_Registration.objects.filter(email = email).exists():
          messages.error(request, 'user email already exists')
          return redirect('hr_registration')
        
        if HR_Registration.objects.filter(password = password).exists():
          messages.error(request, 'user password already exists')
          return redirect('hr_registration')
        if email:
          hr_data = HR_Registration(
              hr_employ_id=hr_employ_id,
              hr_name=hr_name,
              phone_number=phone_number,
              email=email,
              password=password,
              image=image  # Assuming 'image' is the field name for the profile picture
          )

          hr_data.save()

          request.session['profile_pic'] = hr_data.image.url
          request.session['username'] = hr_data.hr_name
          return redirect('hr_login')
        else:
          pass
    else:
        form = HR_Registration_Form()

    return render(request, 'hr/hr_registration.html', {'form': form})

def HR_Login(request):
    if request.method == 'POST':
        form = HR_Login_Form(request.POST)
        if form.is_valid():
            hr_employ_id = form.cleaned_data['hr_employ_id']
            password = form.cleaned_data['password']
            try:
                user = HR_Registration.objects.get(hr_employ_id=hr_employ_id)
                if user.password == password:
                    request.session['hr_employ_id'] = hr_employ_id
                    request.session['user_id'] = user.id
                    request.session['username'] = user.hr_name
                    # No image field associated with login form, so no need to set 'profile_pic'
                    return redirect('home')
                else:
                    messages.error(request, 'Login failed. Please check your credentials.')
            except HR_Registration.DoesNotExist:
                messages.error(request, 'User does not exist. Please check your credentials.')
    else:
        form = HR_Login_Form()

    return render(request, 'hr/hr_login.html', {'form': form})

def hr_interview_declaration(request):
      if request.method == 'POST':
        hr_employ_id = request.POST.get('hr_employ_id')
        student_name = request.POST.get('student_name')
        father_name = request.POST.get('father_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        qualifications = request.POST.get('qualifications') 
        year_of_passout = request.POST.get('year_of_passout')
        resume = request.POST.get('resume')
        
        hr_form_data = HR_Interview_Declaration(hr_employ_id=hr_employ_id,student_name=student_name, father_name=father_name, date_of_birth=date_of_birth, gender=gender, email= email, qualifications=qualifications, year_of_passout=year_of_passout, resume=resume)
        
        hr_form_data.save()
        
        return redirect('home')
      else:
          form = HR_Interview_Form()
          
      return render(request, 'hr/hr_interview_declaration.html', locals())

def LogOut(request):
  
  
  if 'hr_employ_id' in request.session:
      del request.session['hr_employ_id']
 

  return render(request, 'hr/hr_login.html')



class Update_Student(UpdateView):
   
    model = HR_Interview_Declaration
    form_class = Student_Updata_Form
    template_name = 'hr/hr_interview_update.html'
    success_url = reverse_lazy('home')
      
class Student_Delete(DeleteView):
      model = HR_Interview_Declaration
      template_name= 'hr/hr_interview_delete.html'
      success_url = reverse_lazy('home')

def HR_Admin(request):
  
  return render(request,'hr/hr_admin.html')

def Interview_Questions(request, language_id):
    language = Language.objects.all()
    interview_question = Interview_Question.objects.filter(language=language_id)
    print(interview_question)
    return render(request, 'hr/interview_question.html', locals())


def hr_password_reset(request):
    if request.method == 'POST':
        form = HR_Password_Reset_Form(request.POST)
        if form.is_valid():
            hr_employ_id = form.cleaned_data['hr_employ_id']
            new_password = form.cleaned_data['new_password']
            confirm_new_password = form.cleaned_data['confirm_new_password']
            print(hr_employ_id,new_password,confirm_new_password)
            try:
                user = HR_Registration.objects.get(hr_employ_id=hr_employ_id)
                if new_password == confirm_new_password:
                    user.password = new_password
                    user.save()
                    messages.success(request, 'Password reset successful.')
                    
                    request.session['hr_employ_id'] = hr_employ_id
                    request.session['user_id'] = user.id
                    request.session['username'] = user.hr_name
                    return redirect('hr_login')  # Assuming 'hr_login' is the URL pattern for your HR login page
                else:
                    messages.error(request, 'Passwords do not match.')
            except HR_Registration.DoesNotExist:
                messages.error(request, 'User does not exist. Please check your credentials.')
    else:
        form = HR_Password_Reset_Form()

    return render(request, 'hr/hr_password_reset.html', {'form': form})


#marketing views 

def Marketing_Home(request):
   
    if request.session.has_key('employ_id'):
      
      marketing_stu_data = Marketing_Student_Data.objects.filter(employ_id=request.session['employ_id'])
     
      user_id = request.session.get('user_id')
      username = request.session.get('username')
      profile_pic = request.session.get('profile_pic')

      context = {
          'user_id': user_id,
          'username': username,
          'profile_pic': profile_pic,
          'marketing_stu_data':marketing_stu_data,
      }
      
      return render(request, 'marketing/marketing_home.html', {'udata':request.session['employ_id'],'context':context,'marketing_stu_data':marketing_stu_data})
    
    
    else:
      return redirect('marketing_login')
 
def marketing_registration(request):
    if request.method == 'POST':
        employ_id = request.POST.get('employ_id')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image') 
        
 
        # Assuming 'image' is the field name for the profile picture

        if Marketing_Registration.objects.filter(employ_id = employ_id).exists():
          messages.error(request, 'employee_id already exists')
          return redirect('marketing_registration')
        
        if Marketing_Registration.objects.filter(name = name).exists():
          messages.error(request, 'name already exists')
          return redirect('marketing_registration')
        
        if Marketing_Registration.objects.filter(email = email).exists():
          messages.error(request, 'user email already exists')
          return redirect('marketing_registration')
        
        if Marketing_Registration.objects.filter(password = password).exists():
          messages.error(request, 'user password already exists')
          return redirect('marketing_registration')
        if email:
          marketing_data = Marketing_Registration(
              employ_id=employ_id,
              name=name,
              phone_number=phone_number,
              email=email,
              password=password,
              image=image  
          )

          marketing_data.save()

          request.session['profile_pic'] = marketing_data.image.url
          request.session['username'] = marketing_data.name
          return redirect('marketing_login')
        else:
          pass
    else:
        form = Marketing_Registration_Form()

    return render(request, 'marketing/marketing_registration.html', {'form': form})

def Marketing_Login(request):
    if request.method == 'POST':
        form = Marketing_Login_Form(request.POST)
        if form.is_valid():
            employ_id = form.cleaned_data['employ_id']
            password = form.cleaned_data['password']
            try:
                user = Marketing_Registration.objects.get(employ_id=employ_id)
                if user.password == password:
                    request.session['employ_id'] = employ_id
                    request.session['user_id'] = user.id
                    request.session['username'] = user.name
                    # No image field associated with login form, so no need to set 'profile_pic'
                    return redirect('marketing_home')
                else:
                    messages.error(request, 'Login failed. Please check your credentials.')
            except Marketing_Registration.DoesNotExist:
                messages.error(request, 'User does not exist. Please check your credentials.')
    else:
        form = Marketing_Login_Form()

    return render(request, 'marketing/marketing_login.html', {'form': form})

def marketing_student_data(request):
      if request.method == 'POST':
        employ_id = request.POST.get('employ_id')
        student_name = request.POST.get('student_name')
        father_name = request.POST.get('father_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        qualifications = request.POST.get('qualifications') 
        year_of_passout = request.POST.get('year_of_passout')
        resume = request.POST.get('resume')
        
        marketing_stu_data = Marketing_Student_Data(employ_id=employ_id,student_name=student_name, father_name=father_name, date_of_birth=date_of_birth, gender=gender, email= email, qualifications=qualifications, year_of_passout=year_of_passout, resume=resume)
        
        marketing_stu_data.save()
        print(marketing_stu_data)
        return redirect('marketing_home')
      else:
          form = Marketing_Student_Data_Form()
          
      return render(request, 'marketing/marketing_student_data.html', locals())

def Marketing_LogOut(request):
  
  if 'employ_id' in request.session:
      del request.session['employ_id']
 
      return redirect('marketing_login')
  return render(request, 'marketing/marketing_login.html')

def marketing_password_reset(request):
    if request.method == 'POST':
        form = Marketing_Password_Reset_Form(request.POST)
        if form.is_valid():
            employ_id = form.cleaned_data['employ_id']
            new_password = form.cleaned_data['new_password']
            confirm_new_password = form.cleaned_data['confirm_new_password']
            print(employ_id,new_password,confirm_new_password)
            try:
                user = Marketing_Registration.objects.get(employ_id=employ_id)
                if new_password == confirm_new_password:
                    user.password = new_password
                    user.save()
                    messages.success(request, 'Password reset successful.')
                    
                    request.session['employ_id'] = employ_id
                    request.session['user_id'] = user.id
                    request.session['username'] = user.name
                    return redirect('marketing_login')  # Assuming 'hr_login' is the URL pattern for your HR login page
                else:
                    messages.error(request, 'Passwords do not match.')
            except Marketing_Registration.DoesNotExist:
                messages.error(request, 'User does not exist. Please check your credentials.')
    else:
        form = Marketing_Password_Reset_Form()

    return render(request, 'marketing/marketing_password_reset.html', {'form': form})
  
class Marketing_Student_Update(UpdateView):
   
  model = Marketing_Student_Data
  form_class = Marketing_Student_Update_Form
  template_name = 'marketing/marketing_student_update_form.html'
  success_url = reverse_lazy('marketing_home')
      
class Marketing_Student_Delete(DeleteView):
      model = Marketing_Student_Data
      template_name= 'marketing/marketing_student_delete_form.html'
      success_url = reverse_lazy('marketing_home')