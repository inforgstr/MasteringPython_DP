"""
SRP - Signle responsiblity principle.
To understand the SRP. We can imagine the management tools for any file generation.
For the start, we can write the initial version of this functionality.
Let's consider this overall naming of tool as FileSys.
"""


class FileSys:
    """
    A class to manage tools of files.
    """

    def __init__(self, content):
        self.content = content

    def generate(self):
        print(f"File content: \n{self.content}")

    def save_to_file(self, file_name):
        try:
            with open(file_name, mode="w", encoding="utf-8") as file:
                file.write(self.content)
            print("Successfully saved!")

        except FileNotFoundError as err:
            print(f"Provided wrong path to file: {err}")


"""
As we can see, the code actually fine. But to work as SRP, we should consider its rules.
Since, program can grow and be more complex, the SRP stands on separating the functionalities.
To achieve more efficient, opmitized solutions for the future.
Here, how can implement it:
"""


# Firstly we define the one class that provides only one functionality, to keep it efficienty soon...
class FileSys:
    def __init__(self, content):
        self.content = content

    def generate(self):
        print(f"File content: {self.content}")


# Then we can create one more class to be able to save in file
# NOTE: it is another functionality
class FileSysSaver:
    def __init__(self, file_sys: FileSys):
        self.file_sys: FileSys = file_sys

    def save_to_file(self, file_name):
        try:
            with open(file_name, mode="w", encoding="utf-8") as file:
                content = self.file_sys.content
                file.write(content)
        except FileNotFoundError as err:
            print(f"Provided wrong path to file: {err}")


"""
As you noticed there become more classes. But don't panic, by growing the application itself the functionality will grow as well.
Consequently, this approach is more flexible in the term of optimization, when there are a lot of functionalities.
For instance, we can consider the generation, checker, and more of content the current file.
And saver, and other utilities to mantain the app in overall for file saving class.
"""

if __name__ == "__main__":
    file_sys = FileSys("A lot of content here.")
    file_sys.generate()
    saver = FileSysSaver(file_sys)
    saver.save_to_file("generated_file.txt")
