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

    def get_item_by_id(self, item_id):
            for item in self.catalog:
             if int(item['ID']) == item_id:
                return item
            return None       
     
    def update_stock(self, item_id, new_stock):
        for item in self.catalog:
            if int(item['ID']) == item_id:
                item['stock'] = new_stock
                self.save()
                return item
        return None

    def update_cost(self, item_id, new_cost):
        for item in self.catalog:
            if int(item['ID']) == item_id:
                item['cost'] = new_cost
                self.save()
                return item
        return None

    def update_stock_and_cost(self, item_id, new_stock, new_cost):
        for item in self.catalog:
            if int(item['ID']) == item_id:
                item['stock'] = new_stock
                item['cost'] = new_cost
                self.save()
                return item
        return None
