from Diary import Diary

class DiaryPersistence:
    @staticmethod
    def save_to_file(diary, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for entry in diary.entries:
                f.write(entry + '\n')

    @staticmethod
    def load_from_file(filename):
        new_diary = Diary()
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f.readlines()]
                new_diary.entries = lines
                new_diary.counter = len(lines)
        except FileNotFoundError:
            print(f"Viga: Faili {filename} ei leitud.")
        return new_diary