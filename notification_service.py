import os
import redis
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from logger import setup_logging, logging

# Setup logging configuration
setup_logging()

def send_notification(user_id):
    logging.info(f"Sending notification to user {user_id}.")

def schedule_notification(user_id, schedule_time_str):
    schedule_time = datetime.strptime(schedule_time_str, "%Y-%m-%d %H:%M:%S")
    notification_time = schedule_time - timedelta(minutes=30)
    scheduler.add_job(send_notification, 'date', run_date=notification_time, args=[user_id])
    logging.info(f"Scheduled notification for user {user_id} at {notification_time}.")

def listen_for_notifications():
    # Use environment variables for Redis configuration
    redis_host = os.getenv('REDIS_HOST', 'localhost')
    redis_port = int(os.getenv('REDIS_PORT', 6379))
    redis_db = int(os.getenv('REDIS_DB', 0))

    redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)
    pubsub = redis_client.pubsub()
    pubsub.subscribe('notification_schedule')

    logging.info("Listening for new notifications...")
    try:
        for message in pubsub.listen():
            if message['type'] == 'message':
                data = message['data'].decode('utf-8')
                logging.info(f"Received data: {data}")
                user_id, schedule_time_str = data.split('_')
                schedule_notification(user_id, schedule_time_str)
    except KeyboardInterrupt:
        logging.info("Shutting down...")
        scheduler.shutdown()
        redis_client.close()

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.start()
    listen_for_notifications()
