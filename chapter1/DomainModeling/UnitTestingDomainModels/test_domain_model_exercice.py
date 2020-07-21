import pytest
from models import Batch, OrderLine
from allocation import allocate


def test_allocated_order_line_updating_batch_stock():
    STOCK_BEFORE_ORDER = 100
    in_stock_batch = Batch('in-stock-batch', 'SSD 256G', STOCK_BEFORE_ORDER)
    order_line = OrderLine('SSD 256G', 25)

    allocate(order_line, [in_stock_batch])

    assert in_stock_batch.quantity == STOCK_BEFORE_ORDER - order_line.quantity


def test_allocation_reference_first_batch_matching_order_line_request():
    STOCK_BEFORE_ORDER = 100
    in_stock_batch_first = Batch('in-stock-batch-first', 'SSD 256G', STOCK_BEFORE_ORDER)
    in_stock_batch_second = Batch('in-stock-batch-second', 'SSD 256G', STOCK_BEFORE_ORDER)
    
    order_line = OrderLine('SSD 256G', 25)

    allocation = allocate(order_line, [in_stock_batch_first, in_stock_batch_second])

    assert allocation == in_stock_batch_first.reference
    assert in_stock_batch_first.quantity == STOCK_BEFORE_ORDER - order_line.quantity
    assert in_stock_batch_second.quantity == STOCK_BEFORE_ORDER


def test_not_able_to_allocate_when_batch_quantity_lower_than_order_line_quantity():
    STOCK_BEFORE_ORDER = 100
    
    in_stock_batch_first = Batch('in-stock-batch-first', 'SSD 256G', STOCK_BEFORE_ORDER)
    in_stock_batch_second = Batch('in-stock-batch-second', 'SSD 256G', STOCK_BEFORE_ORDER)

    order_line = OrderLine('SSD 256G', STOCK_BEFORE_ORDER * 2)

    allocation = allocate(order_line, [in_stock_batch_first, in_stock_batch_second])

    assert allocation is None
    assert in_stock_batch_first.quantity == STOCK_BEFORE_ORDER and in_stock_batch_second.quantity == STOCK_BEFORE_ORDER

