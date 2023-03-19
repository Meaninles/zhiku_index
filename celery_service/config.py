from kombu import Exchange, Queue


BROKER_URL = 'redis://:@127.0.0.1:6379/2'  # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://:@127.0.0.1:6379/2'  # 指定 Backend

CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，默认是 UTC

CELERY_IMPORTS = (  # 指定导入的任务模块
    'celery_service.kb_index',
)

CELERY_QUEUES = (
    Queue("for_kbindex_task",
          Exchange("for_kbindex_task"),
          routing_key="for_kbindex_task",
          ),
    # Queue("for_generate_task",
    #       Exchange("for_generate_task"),
    #       routing_key="for_generate_task",
    #       ),

)

CELERY_ROUTES = {
    'celery_service.kb_index.kbindex_task': {
        "queue": "for_kbindex_task",
        "routing_key": "for_kbindex_task"
    },
    # 'celery_service.pixray.generate_task': {
    #     "queue": "for_generate_task",
    #     "routing_key": "for_generate_task"
    # },

}
