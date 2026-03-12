class Diary:
    def __init__(self):
        self.entries = []
        self.counter = 0

    def add_entry(self, text):
        self.counter += 1
        entry = f"{self.counter}: {text}"
        self.entries.append(entry)

    def remove_entry(self, index):
        self.entries.pop(index)

    def save(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for entry in self.entries:
                f.write(entry + '\n')

    def load(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            self.entries = [line.strip() for line in f.readlines()]
            self.counter = len(self.entries)

    def print_statistics(self):
        count = len(self.entries)
        if count == 0:
            print("Sissekandeid pole, statistikat ei saa arvutada.")
            return

        total_chr = sum(len(entry) for entry in self.entries)
        avg_chr = total_chr / count

        print(f"Sissekannete arv: {count}")
        print(f"Keskmine tähemärkide arv sissekandes: {avg_chr:.2f}")

    def __str__(self):
        return "\n".join(self.entries)