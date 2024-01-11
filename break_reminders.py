```python
import time
import threading
from plyer import notification

class BreakReminder:
    def __init__(self, break_interval_minutes=60, break_duration_seconds=300):
        self.break_interval_minutes = break_interval_minutes
        self.break_duration_seconds = break_duration_seconds
        self.break_thread = threading.Thread(target=self.run_break_reminder, daemon=True)

    def start(self):
        self.break_thread.start()

    def run_break_reminder(self):
        while True:
            time.sleep(self.break_interval_minutes * 60)
            self.notify_break_start()
            time.sleep(self.break_duration_seconds)
            self.notify_break_end()

    def notify_break_start(self):
        notification.notify(
            title="Break Reminder",
            message="Time for a break! Please take a 5-minute break.",
            timeout=10
        )

    def notify_break_end(self):
        notification.notify(
            title="Break Reminder",
            message="Break time is over. You can now resume your work.",
            timeout=10
        )

if __name__ == "__main__":
    break_reminder = BreakReminder()
    break_reminder.start()
```