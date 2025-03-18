# DevOps Flashcards Application

An interactive web-based flashcard application for studying DevOps-related topics. Built with Flask and modern web technologies.

## Features

- Multiple DevOps topics (AWS, Docker, Kubernetes, etc.)
- Interactive flashcards with flip animation
- Card flagging system for difficult questions
- Progress tracking
- Topic-wise organization
- Numbered navigation
- Flagged cards review mode

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/devops-flashcards.git
cd devops-flashcards
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Adding New Topics

1. Create a new directory in the `questions` folder:
```bash
mkdir questions/your_topic_name
```

2. Create a `questions.json` file in the new directory with the following format:
```json
{
    "questions": [
        {
            "question": "Your question here?",
            "answer": "Your detailed answer here."
        }
    ]
}
```

## Project Structure

```
flashcard/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css      # Application styles
├── templates/
│   ├── index.html     # Home page template
│   └── flashcards.html # Flashcard view template
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