from django.contrib import admin
from rms.models import *
# Register your models here.

admin.site.register(HR_Registration)
admin.site.register(HR_Interview_Declaration)
admin.site.register(Language)
admin.site.register(Interview_Question)
admin.site.register(Interview_Question_Answer)


#marketing models 
admin.site.register(Marketing_Registration)
admin.site.register(Marketing_Student_Data)