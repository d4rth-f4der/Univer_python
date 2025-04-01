from Person import Person

class PartTimeStudent(Person):  # наслідується від класу Person
    def __init__(self, name, age, prac_score, prac_count, exam_scr):
        super().__init__(name,age, prac_score, prac_count, exam_scr)

    def total_score(self):
        S_pr = self.avg_practice_score()
        S_ex = self.exam_scr
        S_res = 0.7 * S_pr + 0.3 * S_ex
        return S_res

    def display_info(self):
        print("Форма навчання - заочна")