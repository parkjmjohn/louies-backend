from enum import Enum


class Status(str, Enum):
    received = "Order Received"
    progress = "Order in Progress"
    pickedup = "Order Picked Up"
