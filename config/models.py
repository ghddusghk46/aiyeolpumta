from django.db import models
from django.contrib.auth.models import User  # 사용자 모델 가져오기

class StudyRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 사용자 정보 연결
    study_time = models.IntegerField()  # 공부 시간 (초)
    goal_percent = models.PositiveIntegerField()  # 목표 달성률 (%)
    feedback = models.TextField()  # 피드백 내용
    date = models.DateField(auto_now_add=True)  # 자동 생성 날짜

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.study_time}초"
