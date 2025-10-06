class MemberSubscription:
    def __init__(self, id=None, member_id=None, membership_id=None, start_date=None, end_date=None, status=None):
        self.id = id
        self.member_id = member_id
        self.membership_id = membership_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def __str__(self):
        return f"MemberSubscription(id={self.id}, member_id={self.member_id}, status={self.status})"