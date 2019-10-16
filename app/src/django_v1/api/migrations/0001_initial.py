# Generated by Django 2.2.3 on 2019-08-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='密码*')),
                ('name', models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='真实姓名*')),
                ('phone', models.CharField(blank=True, default=0, max_length=200, null=True, verbose_name='电话号码*')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用*')),
                ('is_admin', models.BooleanField(default=False, verbose_name='是管理员吗*1是0不是')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱*')),
                ('createTime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='账户创建时间')),
            ],
            options={
                'verbose_name': '1.基本信息表',
                'verbose_name_plural': '1.基本信息表',
            },
        ),
    ]