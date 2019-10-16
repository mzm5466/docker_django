# Generated by Django 2.2.3 on 2019-08-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('code', models.IntegerField(blank=True, null=True, verbose_name='验证码')),
                ('createTime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='验证码创建时间')),
            ],
            options={
                'verbose_name': '邮件验证码',
                'verbose_name_plural': '邮件验证码',
            },
        ),
    ]
