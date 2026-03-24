class Machine:
    def print(self, document):
        raise NotImplementedError("Method print() not implemented!")

    def fax(self, document):
        raise NotImplementedError("Method fax() not implemented!")

    def scan(self, document):
        raise NotImplementedError("Method scan() not implemented!")

class MultiFunctionPrinter(Machine):
    def print(self, document):
        print(f"Printing: {document}")

    def fax(self, document):
        print(f"Faxing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")

class OldFashionedPrinter(Machine):
    def print(self, document):
        print(f"Printing: {document}")

    def fax(self, document):
        pass

    def scan(self, document):
        raise NotImplementedError("Printer cannot scan!")