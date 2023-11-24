import csv

class CatalogManager:
    def __init__(self, filename='data.csv'):
        self.filename = filename
        self.catalog = self.read()

    def read(self):
        with open(self.filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)

    def save(self):
        with open(self.filename, 'w', newline='') as csvfile:
            fieldnames = ['ID','Title','stock','cost','topic']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.catalog)
