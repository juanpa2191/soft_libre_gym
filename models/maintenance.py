class Maintenance:
    def __init__(self, id=None, equipment=None, description=None, maintenance_date=None, cost=None):
        self.id = id
        self.equipment = equipment
        self.description = description
        self.maintenance_date = maintenance_date
        self.cost = cost

    def __str__(self):
        return f"Maintenance(id={self.id}, equipment={self.equipment}, cost={self.cost})"