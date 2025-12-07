# Part 1

class Student:
    def __init__(self, name, student_id, courses_and_grades):
        self.name = name
        self.student_id = student_id

        if type(courses_and_grades) == dict:
            self.courses_and_grades = courses_and_grades
        else:
            self.courses_and_grades = dict(courses_and_grades)

    def get_average_grade(self):
        grades = list(self.courses_and_grades.values())

        if len(grades) == 0:
            return 0
        else:
            total = sum(grades)
            average = total / len(grades)
            return average

    def add_course_and_grade(self, course_name, grade):
        self.courses_and_grades[course_name] = grade

    def get_honors_courses(self, threshold=90):
        honors = []
        for course_name, grade in self.courses_and_grades.items():
            if grade >= threshold:
                honors.append(course_name)
        return honors

    def get_unique_grades(self):
        unique_grades = set()
        for grade in self.courses_and_grades.values():
            unique_grades.add(grade)
        return unique_grades



# Part 2

student1 = Student("Ronaldo", 1, {"Math": 90, "Science": 85, "History": 78})
student2 = Student("Messi", 2, {"Math": 75, "Biology": 70, "English": 82})

s3_courses = [("Art", 95), ("PE", 88), ("Music", 91)]
student3 = Student("Zidane", 3, s3_courses)

all_students = [student1, student2, student3]

for st in all_students:
    avg = st.get_average_grade()
    honors = st.get_honors_courses()

    if avg > 80:
        print(f"{st.name} has an excellent average of {avg:.1f} and honor courses: {honors}")
    else:
        st.add_course_and_grade("Study Skills", 100)
        print(f"Added Study Skills (100) for {st.name}.")
