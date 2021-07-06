# Generated by Django 3.2.3 on 2021-05-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('writer', models.CharField(default='닉네임을 입력해주세요', max_length=15)),
                ('body', models.TextField()),
            ],
        ),
    ]