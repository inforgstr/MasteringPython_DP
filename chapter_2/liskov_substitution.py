"""
Liskov Substitution Principle:
- all subclasses should work after altering their super/base class
"""


class BaseOS:
    def shut_down(self):
        print("Proccessing to close all applications...")


class LinuxOS(BaseOS):
    def shut_down(self):
        print("Shut down...")


class WindowsOS(BaseOS):
    def shut_down(self):
        print("Warning: program is running...")
