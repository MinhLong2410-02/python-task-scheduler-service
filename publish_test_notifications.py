import redis
from datetime import datetime, timedelta

def publish_test_notification(user_id, schedule_time):
    """
    Publish a notification schedule to Redis.

    Args:
    user_id (str): The user ID to notify.
    schedule_time (datetime): The datetime when the user should be notified.
    """
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    schedule_time_str = schedule_time.strftime("%Y-%m-%d %H:%M:%S")
    message = f"{user_id}_{schedule_time_str}"
    redis_client.publish('notification_schedule', message)
    print(f"Published notification for user {user_id} at {schedule_time_str}")

if __name__ == "__main__":
    # Example usage: Schedule a notification for 30 minutes from now
    user_id = "1234"
    current_time = datetime.now()
    schedule_time = current_time + timedelta(minutes=31)
    
    publish_test_notification(user_id, schedule_time)
