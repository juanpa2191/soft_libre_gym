class AuditLog:
    def __init__(self, id=None, user_id=None, action=None, object_type=None, object_id=None, created_at=None):
        self.id = id
        self.user_id = user_id
        self.action = action
        self.object_type = object_type
        self.object_id = object_id
        self.created_at = created_at

    def __str__(self):
        return f"AuditLog(id={self.id}, user_id={self.user_id}, action={self.action}, object_type={self.object_type})"