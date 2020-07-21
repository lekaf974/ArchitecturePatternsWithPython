


class Batch:
    def __init__(self, reference, sku, quantity):
        self.reference = reference
        self.sku = sku
        self.quantity = quantity


class OrderLine:
    def __init__(self, sku, quantity):
        self.sku = sku
        self.quantity = quantity