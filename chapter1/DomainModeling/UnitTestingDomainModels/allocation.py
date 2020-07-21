

def allocate(order_line, batches):
    used_batch_reference = None
    for batch in batches:
        if batch.sku == order_line.sku and batch.quantity >= order_line.quantity:
            used_batch_reference = batch.reference
            batch.quantity -= order_line.quantity
            break
    return used_batch_reference
