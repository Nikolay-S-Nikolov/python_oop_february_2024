from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Nikolay", {'Basics': ['Y'], "Fundamentals": ['Y']})

    def test_constructor_correct_init(self):
        self.assertEqual("Nikolay", self.student.name)
        self.assertEqual({'Basics': ['Y'], "Fundamentals": ['Y']}, self.student.courses)
        new_student = Student("Test")
        self.assertEqual({}, new_student.courses)

    def test_enrol_method_with_existing_course_raise_message(self):
        expected = self.student.enroll('Basics', [0, 1, 2, 3], '')
        self.assertEqual("Course already added. Notes have been updated.", expected)

    def test_enrol_method_with_existing_course_correct_values(self):
        self.student.enroll('Basics', [0, 1, 2, 3], '')
        self.assertEqual(['Y', 0, 1, 2, 3], self.student.courses['Basics'])

    def test_enrol_method_with_new_course_and_notes_raise_message(self):
        expected = self.student.enroll('OOP', [0, 1, 2, 3], '')
        self.assertEqual("Course and course notes have been added.", expected)

    def test_enrol_method_with_new_course_and_notes_correct_values(self):
        self.student.enroll('OOP', [0, 1, 2, 3], '')
        self.assertEqual([0, 1, 2, 3], self.student.courses['OOP'])
        self.student.enroll('Advanced', [4, 5, 6], 'Y')
        self.assertEqual([4, 5, 6], self.student.courses['Advanced'])

    def test_enrol_method_with_new_course_without_notes_raise_message(self):
        expected = self.student.enroll('OOP', [None], 'N')
        self.assertEqual("Course has been added.", expected)

    def test_enrol_method_with_new_course_without_notes_correct_values(self):
        self.student.enroll('OOP', [None], 'N')
        self.assertEqual([], self.student.courses['OOP'])

    def test_add_notes_method_with_existing_course_return_massage(self):
        expected = self.student.add_notes('Basics', [1, 2, 3])
        self.assertEqual("Notes have been updated", expected)

    def test_add_notes_method_with_existing_course_correct_value(self):
        self.student.add_notes('Basics', [1, 2, 3])
        self.assertEqual(['Y', [1, 2, 3]], self.student.courses['Basics'])

    def test_add_notes_method_with_not_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Advanced', [1, 2, 3])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_method_with_existing_course_return_message_and_correct_value(self):
        expected = self.student.leave_course('Basics')
        self.assertEqual("Course has been removed", expected)
        self.assertEqual({"Fundamentals": ['Y'], }, self.student.courses)

    def test_leave_course_method_with_not_existing_course_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Advanced')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
