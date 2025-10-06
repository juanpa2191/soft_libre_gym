class ClassSchedule:
    def __init__(self, id=None, class_id=None, scheduled_at=None, duration_minutes=None, location=None):
        self.id = id
        self.class_id = class_id
        self.scheduled_at = scheduled_at
        self.duration_minutes = duration_minutes
        self.location = location

    def __str__(self):
        return f"ClassSchedule(id={self.id}, class_id={self.class_id}, scheduled_at={self.scheduled_at})"