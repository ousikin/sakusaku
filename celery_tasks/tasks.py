from celery import Celery

# 创建一个Celery的实例
app = Celery('celery_task.task', broker='redis://172.0.0.1:6879/8')


# 定义任务函数
def send_register_active_email(to_email, username, token):
    '''发送激活邮件'''

