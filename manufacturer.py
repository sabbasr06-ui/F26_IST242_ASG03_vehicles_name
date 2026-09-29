class manufacturer:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    @property
    def name(self):
        return self._name
    @property
    def country(self):
        return self._country

    def __str__(self):
        return f"Manufacturer: {self.name}, Country: {self.country}"

    
