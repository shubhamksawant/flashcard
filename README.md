# DevOps Flashcard Application

A Flask-based flashcard application designed to help users learn DevOps concepts through spaced repetition.

## Features

- Multiple DevOps topics (AWS, Docker, Kubernetes, etc.)
- Spaced repetition learning
- Admin interface for managing questions
- Topic-based organization
- Progress tracking

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/flashcard.git
cd flashcard
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
```

5. Load questions:
```bash
python questions/load_questions.py
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Access the application at `http://localhost:5000`

## Directory Structure

```
flashcard/
├── app.py                 # Main application file
├── models.py             
└── questions/
    ├── aws/
    ├── docker/
    ├── kubernetes/
    └── ...            # Other topic directories
```

## Technologies Used

- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- Storage: JSON files, Flask sessions

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## Adding Questions

To contribute new questions:
1. Choose the appropriate topic directory
2. Edit the questions.json file
3. Ensure proper JSON formatting
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask web framework
- DevOps community
- All contributors

## Future Enhancements

- User authentication
- Progress saving
- Spaced repetition
- Search functionality
- Question categories
- Difficulty levels
- Study statistics 