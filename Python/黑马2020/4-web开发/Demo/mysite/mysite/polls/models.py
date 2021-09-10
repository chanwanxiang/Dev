from django.db import models

# Create your models here.

class Question(models.Model):
    # 问题描述
    questionText = models.CharField(max_length=200)
    # 问题发布时间
    pubData = models.DateTimeField('data published')

    def __str__(self):
        return self.questionText

class Choice(models.Model):
    # ForeignKey定义了一个关系,每个Choice对象都关联到一个Question对象
    question =models.ForeignKey(Question,on_delete=models.CASCADE)
    # 选项描述
    choiceText = models.CharField(max_length=200)
    # 当前的得票数
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choiceText

## TODO: 改变模型需要步骤
#     编辑modules.py文件,改变模型
#     运行python manage.py makemigrations为模型改变生成迁移文件
#     运行python manage.py migrate来应用数据库迁移