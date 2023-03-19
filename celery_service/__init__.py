from celery import Celery

celery_service = Celery("kbindex_tasks")
celery_service.config_from_object('celery_service.config')
