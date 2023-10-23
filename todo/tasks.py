from django.core.mail import send_mail
from server import settings
from todo.models import Task
from celery import shared_task
from django.utils import timezone
from .serializers import TaskSerializer


@shared_task
def send_email_task():
    current_time = timezone.now()
    fifteen_minutes_after_from_now = current_time + timezone.timedelta(minutes=15)

    tasks = Task.objects.filter(
        is_completed=False,
        is_notific=False,
        deadline_date__gt=current_time,
        deadline_date__lte=fifteen_minutes_after_from_now
    )
    print(TaskSerializer(tasks, many=True).data)
    for task in tasks:
            minutes_left = task.deadline_date - current_time
            minutes_left = int(minutes_left.total_seconds() / 60)
            send_mail('Notification Todo List',
                      f'Привет! {task.user.name}\n У вас осталось {minutes_left} минут, чтобы успеть выполнить задание'
                      f'\n <<{task.title}>>', settings.EMAIL_HOST_USER,
                      [task.user], fail_silently=False)
            task.is_notific = True
            task.save()