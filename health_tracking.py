```python
import datetime
import json

class HealthTracker:
    def __init__(self):
        self.userProfile = self.load_user_profile()
        self.activity_log = self.load_activity_log()

    def load_user_profile(self):
        with open('user_profile.py', 'r') as file:
            return json.load(file)

    def load_activity_log(self):
        try:
            with open('activity_log.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_activity_log(self):
        with open('activity_log.json', 'w') as file:
            json.dump(self.activity_log, file)

    def track_activity(self, activity_type, duration):
        activity = {
            'type': activity_type,
            'duration': duration,
            'date': str(datetime.datetime.now())
        }
        self.activity_log.append(activity)
        self.save_activity_log()

    def get_daily_activity(self, date):
        daily_activity = [activity for activity in self.activity_log if activity['date'].startswith(date)]
        return daily_activity

    def get_weekly_activity(self, start_date, end_date):
        weekly_activity = [activity for activity in self.activity_log if start_date <= activity['date'] <= end_date]
        return weekly_activity

    def get_monthly_activity(self, month):
        monthly_activity = [activity for activity in self.activity_log if activity['date'].split('-')[1] == month]
        return monthly_activity
```