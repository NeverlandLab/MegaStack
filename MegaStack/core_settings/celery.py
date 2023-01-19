import os
from datetime import timedelta

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', '')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', '')
CELERY_TIMEZONE = 'Asia/Shanghai'
# CELERY_BEAT_SCHEDULE = {
#     '设备状态扫描': {
#         'task': 'apps.node_manager.tasks.scan_device_status',
#         "schedule": timedelta(seconds=300),
#         "args": (),
#     }
# }
