from django.db import models

# Create your models here.
# 用户表
class BasicUser(models.Model):
    password = models.CharField(verbose_name=u'密码*', max_length=200, default=0, blank=True, null=True)
    name = models.CharField(verbose_name=u'真实姓名*', max_length=200, default=0, blank=True, null=True)
    phone = models.CharField(verbose_name=u'电话号码*', max_length=200, default=0, blank=True, null=True)
    is_active = models.BooleanField(verbose_name=u'是否可用*', default=True)
    is_admin=models.BooleanField(verbose_name=u'是管理员吗*1是0不是', default=False)
    email = models.EmailField(verbose_name=u'邮箱*')
    createTime = models.DateTimeField(verbose_name=u'账户创建时间', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = '1.基本信息表'
        verbose_name_plural = '1.基本信息表'
# Create your models here.
class BasicEmail(models.Model):
    email=models.EmailField()
    code=models.IntegerField(verbose_name="验证码",blank=True, null=True)
    createTime = models.DateTimeField(verbose_name=u'验证码创建时间', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = '邮件验证码'
        verbose_name_plural = '邮件验证码'
