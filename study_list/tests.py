from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import StudyList

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='password')
        testuser1.save()

        testpost = StudyList.objects.create(
            student=testuser1,
            notes='blah blah blah i hate studying',
            structure='Array',
        )
        testpost.save()

    def test_blog_content(self):
        studylist = StudyList.objects.get(id=1)
        actual_student = str(studylist.student)
        actual_notes = str(studylist.notes)
        actual_structure = str(studylist.structure)
        self.assertEqual(actual_student, 'testuser1')
        self.assertEqual(actual_notes, 'blah blah blah i hate studying')
        self.assertEqual(actual_structure, 'Array')