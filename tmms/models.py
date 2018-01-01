from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Material(models.Model):
    mSNum = models.CharField(max_length=10,unique=True,verbose_name="书号")
    mName = models.CharField(max_length=20,verbose_name="书名")
    mCurCount = models.IntegerField(default=0,verbose_name="当前数量")
    mMaxCount = models.IntegerField(default=50,verbose_name="最大库存")
    mMinCount = models.IntegerField(default=0,verbose_name="最小库存")
    mPrice = models.IntegerField(blank=True,verbose_name="价格")
    class Meta:
        verbose_name = "教学材料"
        verbose_name_plural = "教学材料"
    def totalPrice(self):
        return self.mCurCount*self.mPrice
    totalPrice.short_description = "总价值"

class Course(models.Model):
    cName = models.CharField(max_length=12,verbose_name="课程名")
    cMaterials = models.ManyToManyField(Material,verbose_name="教学材料")
    class Meta:
        verbose_name = "课程"
        verbose_name_plural = "课程"
    def MaterialsNum(self):
        return self.cMaterials.count()
    MaterialsNum.short_description = "教材数量"

class Grade(models.Model):
    gName = models.CharField(max_length=10,verbose_name="班级")
    gMaxNum = models.IntegerField(default=50,verbose_name="班级最大人数")
    gCurNum = models.IntegerField(default=0,verbose_name="当前人数")
    gCourse = models.ManyToManyField(Course,verbose_name="课程")
    class Meta:
        verbose_name = "班级信息"
        verbose_name_plural = "班级信息"
    def __str__(self):
        return self.gName


class Student(models.Model):
    sId = models.CharField(max_length=10,primary_key=True,verbose_name="学号")
    sName = models.CharField(max_length=10,verbose_name="姓名")
    sAge = models.IntegerField(blank=True,verbose_name="年龄")
    sHobby = models.CharField(max_length=200,blank=True,verbose_name="爱好")
    sOther= models.CharField(max_length=200,blank=True,verbose_name="备注")
    sGrade = models.ForeignKey(Grade,on_delete=models.CASCADE,verbose_name="班级")
    class Meta:
        verbose_name = "学生信息"
        verbose_name_plural = "学生信息"
    def gradeName(self):
        return self.sGrade.gName
    gradeName.short_description = "班级"

class Teacher(models.Model):
    tName = models.CharField(max_length=12,verbose_name="姓名")
    tAge = models.IntegerField(blank=True,verbose_name="年龄")
    tGrade = models.ForeignKey(Grade,on_delete=models.CASCADE,verbose_name="班级")
    tOther = models.CharField(max_length=200,blank=True,verbose_name="备注")
    class Meta:
        verbose_name = "教师信息"
        verbose_name_plural = "教师信息"


class News(models.Model):
    nMaterial = models.ForeignKey(Material,on_delete=models.CASCADE,verbose_name="教学材料")
    nType = models.IntegerField(default=0,verbose_name="类型")
    nDate = models.DateField(verbose_name="时间")
    nCount = models.IntegerField(verbose_name="数量")
    class Meta:
        verbose_name = "news"
        verbose_name_plural = "news"