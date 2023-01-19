from celery import shared_task


@shared_task
def sample_celery_action():
    return 'success'
