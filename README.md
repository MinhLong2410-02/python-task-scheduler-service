# python-task-scheduler-service
A basic Task Scheduler service to schedule task with pub/sub method and Redis.
- Use `apscheduler` for background processing (can be a problem for CPU Usage increase)
- Deploy with docker
- Communicate with backend via Redis

## How to run
- git clone this repo
- docker-compose up -d --build

## Testing
Modify `publish_test_notifications.py` for schedule task testing (line 20 - 22)

## Best use case:
- `apscheduler`: Periodic tasks that need to run on a strict schedule
- `redis`: core technology for pub/sub method, communicatable with backend serivce

