class School:
    def __init__(self, name=None, roster={}):
        self.name = name
        self.roster = roster

    def add_student(self, name, grade):
        list_of_students_in_grade = self.roster.get(str(grade), [])
        list_of_students_in_grade.append(name)
        self.roster[str(grade)] = list_of_students_in_grade

    def grade(self, grade):
        return self.roster.get(str(grade), [])

    def sort_roster(self):
        sorted_roster = {}
        for s_grade, list_of_students_in_grade in self.roster.items():
            sorted_roster[s_grade] = sorted(list_of_students_in_grade)
        return sorted_roster
