import unittest
from class_definitions import student as t

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = t('Duck', 'Daisy', 'Computer Science', 3.9)

    def tearDown(self) :
        del self.student

    def test_inital_all_attributes(self):
        Student = t('Duck', 'Daisy', 'Computer Science') # this is not self.person from setUp, but local
        assert Student.last_name == 'Duck' # note no self here on person or assert
        assert Student.first_name == 'Daisy'
        assert Student.major == 'Computer Science'

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Duck')
        self.assertEqual(self.student.first_name, 'Daisy')
        self.assertEqual(self.student.major, 'Computer Science')

    def test_person_str(self):
        self.assertEqual(str(self.student),('Duck, Daisy has major Computer Science with gpa: 3.9'))

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            student = t('123', 'Daisy', 'Computer Science')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            student = t('Duck', '123', 'Computer Science')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            student = t('Duck', 'Daisy', '123')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            student = t('Duck', 'Daisy', 'abc', 8.0)

if __name__ == '__main__':
    unittest.main()