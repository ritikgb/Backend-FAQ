# Backend-FAQ

# FAQ Project

This is a simple Django-based FAQ system that supports multiple languages for questions and answers. It uses Django REST framework to expose an API to fetch FAQ data. Additionally, the FAQ model automatically translates the questions and answers into multiple languages (Hindi, Bengali) if not already provided.

## Features
- **Multi-language Support**: Fetch FAQs in English, Hindi, and Bengali.
- **API Endpoint**: `GET /api/faqs/` to retrieve the list of FAQs.
- **Database Caching**: Frequently fetched data is cached to improve performance.

## Installation
Follow these steps to get the project up and running locally.

### Prerequisites
- Python 3.x
- Django 5.1+
- Django REST framework
- Google Translate API or `googletrans` library (you may need to install this manually)
- Redis (for caching)

### Steps to Run Locally

#### 1. Clone the repository:
```sh
git clone https://github.com/ritikgb/Backend-FAQ.git
cd faq_project
```

#### 2. Create a virtual environment:
```sh
python -m venv env
```

#### 3. Activate the virtual environment:
- On Windows:
  ```sh
  .\env\Scripts\activate
  ```
- On macOS/Linux:
  ```sh
  source env/bin/activate
  ```

#### 4. Install the dependencies:
```sh
pip install -r requirements.txt
```

#### 5. Apply database migrations:
```sh
python manage.py migrate
```

#### 6. Create a superuser for admin access:
```sh
python manage.py createsuperuser
```

#### 7. Run the development server:
```sh
python manage.py runserver
```

#### 8. Visit the API at:
```
http://127.0.0.1:8000/api/faqs/
```

#### 9. Access the Django admin panel at:
```
http://127.0.0.1:8000/admin/
```

## API Endpoints
### Fetch FAQs in Different Languages
- **GET `/api/faqs/?lang=hi`**: Fetches all the FAQs in the requested language (`lang` query parameter, defaults to English).

#### Example Requests:
```sh
# Fetch FAQs in English (default)
curl http://127.0.0.1:8000/api/faqs/

# Fetch FAQs in Hindi
curl http://127.0.0.1:8000/api/faqs/?lang=hi

# Fetch FAQs in Bengali
curl http://127.0.0.1:8000/api/faqs/?lang=bn
```

## Contribution Guidelines
1. Fork the repository and clone it locally.
2. Create a new branch with a descriptive name.
3. Make your changes following PEP8 guidelines.
4. Test your changes before committing.
5. Use clear and meaningful commit messages.
6. Push your changes and create a pull request.

## License
This project is licensed under the MIT License.

