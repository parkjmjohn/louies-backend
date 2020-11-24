from enum import Enum


class Status(str, Enum):
    received = "Order Received"
    progress = "Order In Progress"
    pickedup = "Order Picked Up"
