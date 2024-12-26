from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Animal  # Replace with your actual model


class YourModelTests(APITestCase):
    def setUp(self):
        self.model_instance = Animal.objects.create(
            # Add your model fields here
        )
        self.valid_payload = {
            # Add valid payload for your model
        }
        self.invalid_payload = {
            # Add invalid payload for your model
        }

    def test_create_model(self):
        response = self.client.post(
            reverse("yourmodel-list"), self.valid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_model_invalid(self):
        response = self.client.post(
            reverse("yourmodel-list"), self.invalid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_model(self):
        response = self.client.get(
            reverse("yourmodel-detail", args=[self.model_instance.id]), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.model_instance.id)

    def test_update_model(self):
        response = self.client.put(
            reverse("yourmodel-detail", args=[self.model_instance.id]),
            self.valid_payload,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_model(self):
        response = self.client.delete(
            reverse("yourmodel-detail", args=[self.model_instance.id]), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
