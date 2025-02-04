"""
OCP - Open closed principle.

This principle provides secure approach to apply in software applications.
In detail, through the OCP we should do only extension not modification for outer purposes.
Since, modifying it can break other related functions.
We should implement it only as extension.


Services that highly likely could be:
- Email
- SMS
- Cloud notifications
- Payment
"""


# Don't do:
class EmailService:
    """
    Simple Email Service class.
    """

    def __init__(self, username, subject, reciever, message):
        self.username = username
        self.subject = subject
        self.reciever = reciever
        self.message = message

    def process_service(self):
        """
        Logic of service.
        """
        pass


class EmailService:
    """
    Simple Email Service class.
    """

    def __init__(self, username, subject, reciever, message):
        self.username = username
        self.subject = subject
        self.reciever = reciever
        self.message = message

    def process_service(self):
        """
        Logic of service.
        """
        pass


def process_service(service):
    if isinstance(service, (EmailService, PaymentService)):
        service.process_service()


# Instead, do:
from typing import Protocol


# first of all define the protocol class
# that will increase the code consistency
class Service(Protocol):
    def process_service(self) -> None: ...


class EmailService:
    def __init__(self, to_username, from_username, subject, message):
        self.to_username = to_username
        self.from_username = from_username
        self.subject = subject
        self.message = message

    def process_service(self) -> None:
        """
        For now, we can just write message and save it in files.
        """
        # simple template for email messages
        body = f"""
            from: {self.from_username}
            to: {self.to_username}
            subject: {self.subject}
            -----------------------
            {self.message}
        """

        with open("./email.txt", "w") as file:
            file.write(body)


class PaymentService:
    def __init__(self, to_username, from_username, price, organization):
        self.to_username = to_username
        self.from_username = from_username
        self.price = price
        self.organization = organization

    def process_service(self) -> None:
        """
        For now, we can just write message and save it in files.
        """
        # simple template for payment notification message
        body = f"""
            To: {self.to_username}
            From: {self.from_username}
            Organization: {self.organization}
            Price: {self.price}
            -----------------------
        """

        with open("./billing.txt", "w") as file:
            file.write(body)


def perform_service(service: Service) -> None:
    service.process_service()


if __name__ == "__main__":
    # process for email service
    email_service = EmailService(
        "Jack", "Nick", "Task [SM-1030930]", "Hi, Jack! Some issue here..."
    )
    perform_service(email_service)

    payment_service = PaymentService("John", "Nick", "100$", "Google")
    perform_service(payment_service)
