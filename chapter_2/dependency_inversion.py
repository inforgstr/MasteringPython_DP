"""
Dependency Inversion Principle:
- make the extended classes dynamic
"""

from typing import Protocol


class Sender(Protocol):
    def send(self, message): ...


class Email:
    def send(self, message):
        print("Sending email:", message)


class Notification:
    def __init__(self, sender):
        self.sender: Sender = sender

    def send(self, message):
        self.sender.send(message)
