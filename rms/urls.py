#main Urls


from django.urls import path,include
from rms.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('base/', Base, name='dashboard.html'),
    path('home/', HR_Home, name='home'),
   
    #hr paths
    path('', HR_Admin, name='hr_admin'),
    path('hr_registration', hr_registration, name='hr_registration'),
    path('hr_login/', HR_Login, name='hr_login'),
    path('hr_student_form/', hr_interview_declaration, name='hr_student_form'),
    path('logout/', LogOut, name='logout'),

    #password reset path
     path('hr_password_reset/', hr_password_reset, name='hr_password_reset'),

    
    path('student_update/<int:pk>/', Update_Student.as_view(), name="student_update"),
    path('student_delete/<int:pk>/',Student_Delete.as_view(), name="student_delete"),
    path('interview_question/<int:language_id>/', Interview_Questions, name='interview_question'),

    #marketing path links
    path('marketing_home/', Marketing_Home, name='marketing_home'),
    path('marketing_registration/', marketing_registration, name='marketing_registration'),
    path('marketing_login/', Marketing_Login, name='marketing_login'),
    path('marketing_student_data/', marketing_student_data, name='marketing_student_data'),
    path('marketing_logOut/', Marketing_LogOut, name='marketing_logOut'),
    path('marketing_password_reset/', marketing_password_reset, name='marketing_password_reset'),
   
    path('marketing_student_update/<int:pk>/', Marketing_Student_Update.as_view(), name="marketing_student_update"),
    
    path('marketing_student_delete/<int:pk>/',Marketing_Student_Delete.as_view(), name="marketing_student_delete"),
    



    
]   

