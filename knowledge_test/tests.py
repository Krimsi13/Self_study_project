from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Section
from knowledge_test.models import Test, Question
from users.models import User


class TestingTestCase(APITestCase):
    """Testing Tests."""
    def setUp(self) -> None:
        self.user = User.objects.create(email="test@test.ru", is_staff=True)
        self.client.force_authenticate(user=self.user)

        self.section_test = Section.objects.create(
            title="title_test",
            description="description_test",
            owner=self.user
        )

    def test_create_Test(self):
        """Testing create Test."""
        data = {
            "title": "title_test"
        }

        response = self.client.post(
            "/tests/create/",
            data=data
        )

        # print(response.json())

        out_data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            out_data.get("title"),
            "title_test")

        self.assertTrue(
            Test.objects.all().exists()
        )

    def test_list_Tests(self):
        """Testing output list of Tests."""

        Test.objects.create(
            title="title_test",
            section=self.section_test
        )

        response = self.client.get(
            "/tests/"
        )

        # print(response.json())

        out_data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.json()),
            1
        )

        self.assertEqual(
            out_data[0].get("title"),
            "title_test")

        self.assertEqual(
            out_data[0].get("section"),
            self.section_test.pk)

    def test_retrieve_Test(self):
        """Testing output one Test."""

        test = Test.objects.create(
            title="title_test",
            section=self.section_test
        )

        response = self.client.get(
            f"/tests/{test.id}/"
        )

        # print(response.json())

        out_data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            out_data.get("title"),
            "title_test")

        self.assertEqual(
            out_data.get("section"),
            self.section_test.pk)

        self.assertTrue(
            Test.objects.all().exists()
        )

    def test_update_Test(self):
        """Testing update Test."""

        test = Test.objects.create(
            title="before update test",
            section=self.section_test
        )

        data = {
            "title": "after update test"
        }

        response = self.client.patch(
            f"/tests/{test.id}/update/",
            data
        )

        # print(response.json())

        out_data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            out_data.get("title"),
            "after update test")

        self.assertEqual(
            out_data.get("section"),
            self.section_test.pk)

        self.assertTrue(
            Test.objects.all().exists()
        )

    def test_delete_Test(self):
        """Testing delete a Test."""

        test = Test.objects.create(
            title="before delete test",
            section=self.section_test
        )

        response = self.client.delete(
            f"/tests/{test.id}/delete/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Test.objects.all().exists()
        )


class QuestionTestCase(APITestCase):
    """Testing Questions."""

    def setUp(self) -> None:
        self.user = User.objects.create(email="test@test.ru", is_staff=True)
        self.client.force_authenticate(user=self.user)

        self.section_test = Section.objects.create(
            title="title_test",
            description="description_test",
            owner=self.user
        )

        self.testing_test = Test.objects.create(
            title="title_test",
            section=self.section_test
        )

    def test_create_question(self):
        """Test create Question."""

        data = {
            "question_number": "A",
            "question_text": "test_text"
        }

        response = self.client.post(
            "/tests/questions/create/",
            data=data
        )

        # print(response.json())

        out_data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            out_data.get("question_number"),
            "A")

        self.assertEqual(
            out_data.get("question_text"),
            "test_text")

        self.assertTrue(
            Question.objects.all().exists()
        )

    def test_list_questions(self):
        """Test output list of questions."""

        Question.objects.create(
            question_number="A",
            question_text="test_text",
            test=self.testing_test
        )

        response = self.client.get(
            "/tests/questions/"
        )

        # print(response.json())

        out_data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.json()),
            1
        )

        self.assertEqual(
            out_data[0].get("question_number"),
            "A")

        self.assertEqual(
            out_data[0].get("question_text"),
            "test_text")

        self.assertEqual(
            out_data[0].get("test"),
            self.testing_test.pk)

        self.assertTrue(
            Question.objects.all().exists()
        )

    def test_retrieve_question(self):
        """Test output one question."""

        question = Question.objects.create(
            question_number="A",
            question_text="test_text",
            test=self.testing_test
        )

        response = self.client.get(
            f"/tests/questions/{question.id}/"
        )

        # print(response.json())

        out_data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            out_data.get("question_number"),
            "A")

        self.assertEqual(
            out_data.get("question_text"),
            "test_text")

        self.assertEqual(
            out_data.get("test"),
            self.testing_test.pk)

        self.assertTrue(
            Question.objects.all().exists()
        )

    def test_update_question(self):
        """Test update question."""

        question = Question.objects.create(
            question_number="A",
            question_text="before update test",
            test=self.testing_test
        )

        data = {
            "question_number": "B",
            "question_text": "after update test"
        }

        response = self.client.patch(
            f"/tests/questions/{question.id}/update/",
            data
        )

        # print(response.json())

        out_data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            out_data.get("question_number"),
            "B")

        self.assertEqual(
            out_data.get("question_text"),
            "after update test")

        self.assertEqual(
            out_data.get("test"),
            self.testing_test.pk)

        self.assertTrue(
            Question.objects.all().exists()
        )

    def test_delete_question(self):
        """Test deleting a question."""

        question = Question.objects.create(
            question_number="A",
            question_text="before delete test",
            test=self.testing_test
        )

        response = self.client.delete(
            f"/tests/questions/{question.id}/delete/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Question.objects.all().exists()
        )
