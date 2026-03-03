class Material:
def __init__(self, name, price_per_meter):
    self.name=name
    self.price_per_meter = price_per_meter

    def __str__(self):
        return f"{self.name} - {self.price_per_meter} E/m"