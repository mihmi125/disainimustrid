class CodeBuilder:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def add_field(self, name, value):
        self.fields.append((name, value))
        return self

    def __str__(self):
        lines = [
            f"class {self.name}:",
            "  def __init__(self):"
        ]
        for name, value in self.fields:
            lines.append(f"    self.{name} = {value}")

        return "\n".join(lines)

if __name__ == "__main__":
    cb = (CodeBuilder('Person')
          .add_field('name', '""')
          .add_field('age', '0')
          )
    print(cb)