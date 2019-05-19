from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.TextField()
    attach1 = models.FileField(upload_to ="docs//" ,null=True, blank=True)
    ask_date = models.DateTimeField(auto_now_add = True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    ask_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='new' , choices=(('new','new'), ('answered','answered')))
    def __str__(self):
        que =  self.question
        if len(que)>30:
           que = que[:27] + "..." 
        return que

class Answer(models.Model):
    answer = models.TextField()
    attach1 = models.FileField(upload_to ="docs//" ,null=True, blank=True)
    ans_date = models.DateTimeField(auto_now_add = True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    ans_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        ans =  self.answer
        if len(ans)>30:
           ans = ans[:27] + "..." 
        return ans
    
class Like(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='likes')
    like_by = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.like_by)
