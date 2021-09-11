from django.db import models


class Template(models.Model):
    name = models.CharField(max_length=128, verbose_name='模版名称')
    desc = models.TextField(verbose_name='描述信息')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return f'{self.name}'

