from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task, Label

class TaskLabelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.label = Label.objects.create(name='Work', owner=self.user)
        self.task = Task.objects.create(title='Test Task', description='Test Description', completion_status=False, owner=self.user)
        self.task.labels.add(self.label)

    def test_create_label(self):
        response = self.client.post('/api/labels/', {'name': 'Personal'}, format='json')
        print(response.data)  # Print the response content for debugging
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Label.objects.count(), 2)
        self.assertEqual(Label.objects.get(id=2).name, 'Personal')

    def test_create_task(self):
        response = self.client.post('/api/tasks/', {
            'title': 'New Task',
            'description': 'New Description',
            'completion_status': False,
            'labels': [self.label.id]
        }, format='json')
        print(response.data)  # Print the response content for debugging
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.get(id=2).title, 'New Task')

    def test_list_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Task')

    def test_list_labels(self):
        response = self.client.get('/api/labels/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Work')
