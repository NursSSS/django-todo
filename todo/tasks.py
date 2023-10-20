from django.core.mail import send_mail
from server import settings
from todo.models import Task
from celery import shared_task
from django.utils import timezone


@shared_task
def send_email_task():
    # current_time = timezone.now()
    # fifteen_minutes_less_from_now = current_time - timezone.timedelta(minutes=15)

    # tasks = Task.objects.filter(
    #     is_completed=False,
    #     is_notific=False,
    #     # deadline_date__gt=current_time,
    #     # deadline_date__lte=fifteen_minutes_less_from_now
    # )

    # for task in tasks:
    #         minutes_left = time_difference = task.deadline_date - current_time
    #         minutes_left = int(time_difference.total_seconds() / 60)
    #         send_mail('Notification Todo List',
    #                   f'Привет! {task.user.name}\n У вас осталось {minutes_left} минут, чтобы успеть выполнить задание'
    #                   f'\n <<{task.title}>>', settings.EMAIL_HOST_USER,
    #                   [task.user], fail_silently=False)
    #         task.is_notific = True
    #         task.save()
    print("bg task in progress")
    task = Task.objects.get(pk=4)

    task.is_notific = True
    task.save