class DiaryStatistics:
    @staticmethod
    def print_statistics(diary):
        count = len(diary.entries)
        if count == 0:
            print("Sissekandeid pole, statistikat ei saa arvutada.")
            return

        total_chr = sum(len(entry) for entry in diary.entries)
        avg_chr = total_chr / count

        print(f"Sissekannete arv: {count}")
        print(f"Keskmine tähemärkide arv sissekandes: {avg_chr:.2f}")