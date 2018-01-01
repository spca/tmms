from django.contrib import admin

# Register your models here.

from .models import Material
from .models import Grade
from .models import Student
from .models import Teacher
from .models import Course

class MaterialAdmin(admin.ModelAdmin):
    fields = ['mName','mSNum','mMaxCount','mMinCount','mPrice']
    list_display = ['id','mName','mCurCount','totalPrice']
    list_display_links = ['mName']
    list_per_page = 20

class GradeAdmin(admin.ModelAdmin):
    fields = ['gName','gMaxNum','gCourse']
    list_display = ['id','gName','gCurNum']
    list_display_links = ['gName']
    list_per_page = 20

class TeacherAdmin(admin.ModelAdmin):
    fields = ['tName','tAge','tGrade','tOther']
    list_display = ['id','tName','tGrade']
    list_display_links = ['tName']
    list_per_page = 20

class StudentAdmin(admin.ModelAdmin):
    fields = ['sName','sId','sAge','sHobby','sGrade','sOther']
    list_display = ('sName', 'sId','gradeName')
    list_filter = ['sAge']
    list_per_page = 20

class CourseAdimin(admin.ModelAdmin):
    fields = ['cName','cMaterials']
    list_display = ['id','cName','MaterialsNum']
    list_display_links = ['MaterialsNum']
    list_per_page = 20


admin.site.register(Material, MaterialAdmin)
admin.site.register(Course,CourseAdimin)
admin.site.register(Grade,GradeAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)




