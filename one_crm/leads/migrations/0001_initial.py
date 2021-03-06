# Generated by Django 3.0.8 on 2020-07-11 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名字')),
                ('title', models.CharField(max_length=255, verbose_name='职称')),
                ('contact', models.CharField(max_length=255, verbose_name='联系方式')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('description', models.TextField(verbose_name='描述')),
                ('attachment', models.FileField(upload_to='upload', verbose_name='附件')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='上次更新时间')),
            ],
        ),
    ]
