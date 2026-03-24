from Interfaces import Printer, Scanner

class MyPrinter(Printer):
    def print(self, document):
        print(f"Printer printing: {document}")

class Photocopier(Printer, Scanner):
    def print(self, document):
        print(f"Photocopier printing: {document}")

    def scan(self, document):
        print(f"Photocopier scanning: {document}")

class MultiFunctionMachine(Printer, Scanner):
    def __init__(self, printer: Printer, scanner: Scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)