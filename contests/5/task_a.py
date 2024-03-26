import sys


class Student:
    def __init__(self, name: str, age: int, course: int):
        self.name = name
        self.age = age
        self.course = course


class University:
    def __init__(self):
        self._students: dict[str, Student] = {}

    def enroll_student(self, name: str, age: int, course: int) -> None:
        if name in self._students:
            raise RuntimeError(f'Student with name {name} is already enrolled')
        student = Student(name, age, course)
        self._students[name] = student

    def expell_student(self, name: str) -> None:
        if name not in self._students:
            raise KeyError(f'Student with name {name} is not enrolled')
        self._students.pop(name)

    def get_students(self) -> list[Student]:
        return sorted(self._students.values(), key=lambda x: x.name)

    @staticmethod
    def print_students(student_list: list[Student]) -> None:
        for student in student_list:
            print(f'Name: {student.name}, age: {student.age},'
                  f' course: {student.course}')

    @staticmethod
    def average_age(student_list: list[Student]) -> float:
        if not student_list:
            return 0
        total_age = sum(student.age for student in student_list)
        return total_age / len(student_list)


if __name__ == '__main__':
    exec(sys.stdin.read())
