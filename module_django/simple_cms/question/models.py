from django.db import models


class Question(models.Model):
    question_id = models.IntegerField(primary_key=True, verbose_name='主键')
    activity_id = models.CharField(max_length=128, verbose_name='活动ID')
    seq = models.IntegerField(verbose_name='序号，步长100')
    question_type = models.SmallIntegerField(verbose_name='问题类型')
    show_type = models.SmallIntegerField(verbose_name='题目形式')
    content = models.CharField(max_length=512, verbose_name='问题内容')
    answer_explain = models.CharField(max_length=512, verbose_name='答案解释 含讲解视频等')
    answer = models.CharField(max_length=1, verbose_name='问题的答案 A B C D等')
    enable = models.SmallIntegerField(verbose_name='0 未启用 1 未启用')
    show_day = models.DateField(verbose_name='展示日期')
    close_time = models.DateTimeField(verbose_name='答题截止日期')
    answer_time = models.DateTimeField(verbose_name='答案公布时间')
    answer_status = models.SmallIntegerField(verbose_name='答案公布状态 0 未公布 1 已公布')
    extra = models.CharField(max_length=512, verbose_name='json 扩展字段')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')


class AnswerRecord(models.Model):
    activity_id = models.CharField(max_length=20, verbose_name='活动ID', db_index=True)
    question_id = models.IntegerField(verbose_name='问题ID', db_index=True)
    user_id = models.IntegerField(verbose_name='用户ID', db_index=True)
    select_answer = models.CharField(max_length=10, verbose_name='用户选择的答案')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        unique_together = ('user_id', 'question_id', 'activity_id')
        index_together = [['question_id', 'user_id']]


class AnswerCoinRecord(models.Model):
    user_id = models.IntegerField(verbose_name='user id', unique=True)
    num = models.IntegerField(verbose_name='total num')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

