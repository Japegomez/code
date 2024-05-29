

class User:
    def __init__(self, id, name, isActive):
        self.id = id
        self.name = name
        self.isActive = isActive

class Session:
    def __init__(self, id, assigned_time, user):
        self.id = id
        self.assigned_time = assigned_time
        self.user = user

class Measurements:
    def __init__(self, id, current, voltage):
        self.id = id
        self.current = current
        self.voltage = voltage