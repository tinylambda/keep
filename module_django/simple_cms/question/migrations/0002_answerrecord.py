# Generated by Django 3.2.3 on 2021-06-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_id', models.CharField(max_length=20, verbose_name='活动ID')),
                ('question_id', models.IntegerField(verbose_name='问题ID')),
                ('user_id', models.IntegerField(verbose_name='用户ID')),
                ('select_answer', models.CharField(max_length=10, verbose_name='用户选择的答案')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'unique_together': {('user_id', 'question_id', 'activity_id')},
            },
        ),
    ]