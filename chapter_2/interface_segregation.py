"""
ISP - Interface Segregation Principle.
- Small and more focused interfaces
- One class/functions should have one purpose not multiple
"""


class AllInOnePrinter:
    def print_doc(self):
        print("Document printing...")

    def scan_doc(self):
        print("Document scanning...")

    def fax_doc(self):
        print("Document faxing...")


# NOTE: if we want to implement SimplePrinter subclasses, we will have
# unnecessary methods: scan_doc() and fax_doc()

# Suggest: Do like this
# NOTE: it is important to use Protocol to represent typing more readable
from typing import Protocol


class Scanner(Protocol):
    def scan_doc(self): ...


class Fax(Protocol):
    def fax_doc(self): ...


class Printer(Protocol):
    def print_doc(self): ...


# implement all classes
class SimplePrinter:
    def print_doc(self):
        print("Simply printing...")


# Ensure to use right protocol to know that SimplePrinter has right method
def do_the_print(printer: Printer):
    printer.print_doc()


if __name__ == "__main__":
    all_in_one_printer = AllInOnePrinter()
    all_in_one_printer.fax_doc()
    all_in_one_printer.print_doc()
    all_in_one_printer.scan_doc()
    do_the_print(all_in_one_printer)

    simple = SimplePrinter()
    do_the_print(simple)
