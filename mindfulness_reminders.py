```python
import time
from plyer import notification

def set_mindfulness_reminder(reminder_time, reminder_message):
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == reminder_time:
            notification.notify(
                title="Mindfulness Reminder",
                message=reminder_message,
                timeout=10
            )
            time.sleep(60)
```