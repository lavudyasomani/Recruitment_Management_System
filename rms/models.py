from django.db import models

# Create your models here.

from django.db import models

class HR_Registration(models.Model):
    hr_employ_id = models.CharField(max_length=10)
    hr_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/hr_images/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.hr_name}"


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Interview_Question(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.question}"
    
class Interview_Question_Answer(models.Model):
    interview_question = models.ForeignKey(Interview_Question, on_delete=models.CASCADE)
    answer = models.TextField(max_length=500)
    
    def __str__(self):
        return f"{self.answer}"


class HR_Interview_Declaration(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    hr_employ_id= models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=100, null=True)
    qualifications = models.CharField(max_length=200)
    year_of_passout = models.PositiveIntegerField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.student_name

#marketing registrations

class Marketing_Registration(models.Model):
    employ_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/hr_images/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"

class Marketing_Student_Data(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    employ_id= models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=100, null=True)
    qualifications = models.CharField(max_length=200)
    year_of_passout = models.PositiveIntegerField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.student_name
