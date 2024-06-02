# Task Management

This is a Django-based Task Management API that allows users to create, update, delete, and retrieve tasks and labels. The API supports user-specific data access, ensuring that users only see their own tasks and labels.

### Installation

1. **Clone the repository:**

   ```sh
   git clone <Link>
   Change the directory to the respective folder using cd command
   ```

2. **Install dependencies:**

   ```sh
   Install the requirements using the below command
   pip install -r requirements.txt
   ```

3. **Apply migrations:**

   ```sh
   Run migrations to set the database
   python manage.py migrate
   ```

4. **Create a superuser:**

   ```sh
   python manage.py createsuperuser
   ```

5. **Run the development server:**

   ```sh
   To run the server use this command
   python manage.py runserver
   ```

### Testing

#### Running Tests

To run the unit tests, use the following command:

```sh
python manage.py test
```

### Using Postman

#### Setting Up Postman

1. **Download and install Postman:** [Postman Download](https://www.postman.com/downloads/)

**Start the Django development server:**

```sh
python manage.py runserver
```

2. **Open Postman and create a new request:**

   **URL:** `http://127.0.0.1:8000/api-token-auth/`

In the Body tab, select raw and set the format to JSON.

Enter your login credentials as JSON:
{
"username": "yourusername",
"password": "yourpassword"
}
Click Send.

Copy the token from the response.

3. **Create a new request:**

   **For Authorization**

   In the Headers tab, add a new header:

   Key: Authorization

   Value: Token YOUR_TOKEN (replace YOUR_TOKEN with the token obtained)

   - **Method:** Choose the appropriate HTTP method (GET, POST, PUT, DELETE) based on the action you want to perform.

   - **For creating a label:** Set the method to POST and the URL to http://127.0.0.1:8000/api/labels/.
   - **For listing labels:** Set the method to GET and the URL to http://127.0.0.1:8000/api/labels/.
   - **For creating a task:** Set the method to POST and the URL to http://127.0.0.1:8000/api/tasks/.
   - **For listing tasks:** Set the method to GET and the URL to http://127.0.0.1:8000/api/tasks/.
   - **For updating a task:** Set the method to PUT and the URL to http://127.0.0.1:8000/api/tasks/{id}/ (replace {id} with the task ID).
   - **For deleting a task:** Set the method to DELETE and the URL to http://127.0.0.1:8000/api/tasks/{id}/ (replace {id} with the task ID).

#### Example JSON data

1. **For label:**

   ```json
   {
     "name": "Work"
   }
   ```

2. **For task:**

   ```json
   {
     "title": "New Task",
     "description": "Task Description",
     "completion_status": false,
     "labels": [1] // Use the ID of the label you created
   }
   ```
