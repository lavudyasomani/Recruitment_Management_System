
from django import forms
from rms.models import *

class HR_Registration_Form(forms.Form):
    hr_employ_id = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    hr_name = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    image = forms.ImageField(required=False)  # Add this line for the image field

    def save(self):
        # Create and save a new HR_Registration object
        hr_registration = HR_Registration(
           
            hr_name=self.cleaned_data['hr_name'],
            hr_employ_id=self.cleaned_data['hr_employ_id'],
            phone_number=self.cleaned_data['phone_number'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            image=self.cleaned_data['image']
        )
        hr_registration.save()


    class Meta:
        model = HR_Registration
        fields = ['hr_name', 'hr_employ_id', 'phone_number', 'email', 'password', 'image']
        widgets = {
            'password': forms.PasswordInput(),
        }

class HR_Login_Form(forms.Form):
    hr_employ_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class HR_Interview_Form(forms.Form):
    hr_employ_id = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))

    student_name = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    
    father_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], widget=forms.Select(attrs={'class': 'form-control'}))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'autofocus': True}))
    
    qualifications = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   
    year_of_passout = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    resume = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    
    class Meta:
        model = HR_Interview_Declaration
        fields = ['name', 'father_name', 'date_of_birth', 'gender', 'qualifications', 'year_of_passout', 'resume']
        

class Student_Updata_Form(forms.ModelForm):
    class Meta: 
        model = HR_Interview_Declaration
        fields = ['student_name', 'email', 'qualifications', 'year_of_passout', 'resume']
        widgets = {
            'student_name': forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'autofocus': True}),
            'qualifications': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_passout': forms.NumberInput(attrs={'class': 'form-control'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }



class HR_Password_Reset_Form(forms.Form):
    hr_employ_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}), max_length=20 ,label='HR Employee ID')
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='New Password')
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Confirm New Password')


#marketing forms

class Marketing_Registration_Form(forms.Form):
    employ_id = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    image = forms.ImageField(required=False)  # Add this line for the image field

    def save(self):
        # Create and save a new HR_Registration object
        mr = Marketing_Registration(
           
            hr_name=self.cleaned_data['name'],
            hr_employ_id=self.cleaned_data['employ_id'],
            phone_number=self.cleaned_data['phone_number'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            image=self.cleaned_data['image']
        )
        mr.save()


    class Meta:
        model = Marketing_Registration
        fields = ['name', 'employ_id', 'phone_number', 'email', 'password', 'image']
        widgets = {
            'password': forms.PasswordInput(),
        }

class Marketing_Login_Form(forms.Form):
    employ_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    

class Marketing_Student_Data_Form(forms.Form):
    employ_id = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))

    student_name = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    
    father_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], widget=forms.Select(attrs={'class': 'form-control'}))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'autofocus': True}))
    
    qualifications = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   
    year_of_passout = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    resume = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    
    class Meta:
        model = Marketing_Student_Data
        fields = ['name', 'father_name', 'date_of_birth', 'gender', 'qualifications', 'year_of_passout', 'resume']


class Marketing_Student_Update_Form(forms.ModelForm):
    class Meta: 
        model = Marketing_Student_Data
        fields = ['student_name', 'email', 'qualifications', 'year_of_passout', 'resume']
        widgets = {
            'student_name': forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'autofocus': True}),
            'qualifications': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_passout': forms.NumberInput(attrs={'class': 'form-control'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }



class Marketing_Password_Reset_Form(forms.Form):
    employ_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}), max_length=20 ,label='HR Employee ID')
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='New Password')
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Confirm New Password')
    