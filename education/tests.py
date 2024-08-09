from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Material, Section
from users.models import User


class MaterialTestCase(APITestCase):
    """Testing Materials."""
    def setUp(self) -> None:
        self.user = User.objects.create(email="test@test.ru", is_staff=True)
        self.client.force_authenticate(user=self.user)

        self.section_test = Section.objects.create(
            title="title_test",
            description="description_test"
        )

    def test_create_material(self):
        """Test create material."""
        data = {
            "title": "title_test",
            "description": "description_test",
            "section": 1,
            "owner": 1
        }
        response = self.client.post(
            "/education/materials/create/",
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

        self.assertEqual(
            out_data.get("description"),
            "description_test")

        self.assertEqual(
            out_data.get("section"),
            1)

        self.assertTrue(
            Material.objects.all().exists()
        )

    def test_list_materials(self):
        """Test output list of materials."""

        Material.objects.create(
            title="title_test",
            description="description_test",
            section=self.section_test,
            owner=self.user
        )

        response = self.client.get(
            "/education/materials/"
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
            out_data[0].get("description"),
            "description_test")

    def test_retrieve_material(self):
        """Test output one material."""

        material = Material.objects.create(
            title="title_test",
            description="description_test",
            section=self.section_test,
            owner=self.user
        )

        response = self.client.get(
            f"/education/materials/{material.id}/"
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
            out_data.get("description"),
            "description_test")

        self.assertTrue(
            Material.objects.all().exists()
        )

    def test_update_material(self):
        """Test update material."""

        material = Material.objects.create(
            title="before update test",
            description="before update test",
            section=self.section_test,
            owner=self.user
        )

        data = {
            "title": "after update test",
            "description": "after update test"
        }

        response = self.client.patch(
            f"/education/materials/{material.id}/update/",
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
            out_data.get("description"),
            "after update test")

        self.assertTrue(
            Material.objects.all().exists()
        )

    def test_delete_material(self):
        """Test deleting a material."""

        material = Material.objects.create(
            title="before delete test",
            description="before delete test",
            section=self.section_test,
            owner=self.user
        )

        response = self.client.delete(
            f"/education/materials/{material.id}/delete/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Material.objects.all().exists()
        )
