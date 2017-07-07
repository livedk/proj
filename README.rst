Django中使用Celery

proj/celery.py

This module contains the Celery application instance for this project,
we take configuration from Django settings and use autodiscover_tasks to find task modules
inside all packages listed in INSTALLED_APPS.

app1/tasks.py

异步任务定义


启动worker
参考http://docs.celeryproject.org/en/latest/userguide/workers.html
$ celery -A proj worker -l info

启动定时
参考http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
$ celery -A proj beat -l info