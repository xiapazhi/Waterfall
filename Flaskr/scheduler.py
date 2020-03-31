from flask_apscheduler import APScheduler
# 注册APScheduler
scheduler = APScheduler()


def init_scheduler(app):
    # it is also possible to enable the API directly
    # scheduler.api_enabled = True
    scheduler.init_app(app)
    # 添加任务
    scheduler.add_job(
        func='Flaskr.utils'+':'+'check_picture',
        id='check_picture',
        # args=(1,2,3),
        # trigger='interval',
        # seconds=3
        trigger='cron',
        hour=4,
        # second=10,
    )
    scheduler.start()
