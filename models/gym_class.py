class GymClass:
    def __init__(self, id=None, name=None, description=None, trainer_id=None, capacity=None):
        self.id = id
        self.name = name
        self.description = description
        self.trainer_id = trainer_id
        self.capacity = capacity

    def __str__(self):
        return f"GymClass(id={self.id}, name={self.name}, capacity={self.capacity})"