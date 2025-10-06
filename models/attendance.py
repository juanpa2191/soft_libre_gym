class Attendance:
    def __init__(self, id=None, schedule_id=None, member_id=None, attended_at=None, status=None):
        self.id = id
        self.schedule_id = schedule_id
        self.member_id = member_id
        self.attended_at = attended_at
        self.status = status

    def __str__(self):
        return f"Attendance(id={self.id}, schedule_id={self.schedule_id}, member_id={self.member_id}, status={self.status})"