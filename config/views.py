from django.shortcuts import render
from .models import StudyRecord

def today_study_view(request):
    record = StudyRecord.objects.last()

    context = {
        'study_time': "00:00:00",
        'goal_percent': "0",
        'feedback_list': [
            "공부 기록이 아직 없습니다. 오늘부터 시작해볼까요?"
        ]
    }

    if record:
        hours = record.study_time // 3600
        minutes = (record.study_time % 3600) // 60
        seconds = record.study_time % 60
        time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        context = {
            'study_time': time_string,
            'goal_percent': record.goal_percent,
            'feedback_list': record.feedback.split("\n")
        }

    return render(request, 'study/today.html', context)
