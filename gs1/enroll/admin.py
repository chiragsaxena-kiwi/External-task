from django.contrib import admin
from .models import Employee, Signup, img_table
from .models import multi_file,img_table
# Register your models here.

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ['id','username','password','email','dob']

admin.site.register(multi_file)
admin.site.register(img_table)
admin.site.register(Employee)
