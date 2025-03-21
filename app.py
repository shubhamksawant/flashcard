from flask import Flask, render_template, jsonify, request, session, send_from_directory
import json
import os
import random
import importlib.util

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

class FlashcardManager:
    def __init__(self):
        self.questions_dir = "questions"
        print(f"Questions directory: {os.path.abspath(self.questions_dir)}")  # Debug log
    
    def get_topics(self):
        """Get all available topics by scanning the questions directory"""
        try:
            print(f"Scanning directory: {os.path.abspath(self.questions_dir)}")  # Debug log
            # Get all directories in the questions folder
            all_items = os.listdir(self.questions_dir)
            print(f"All items in directory: {all_items}")  # Debug log
            
            topics = []
            for d in all_items:
                full_path = os.path.join(self.questions_dir, d)
                if os.path.isdir(full_path):
                    py_path = os.path.join(full_path, 'questions.py')
                    json_path = os.path.join(full_path, 'questions.json')
                    print(f"Checking directory {d}:")  # Debug log
                    print(f"  Python file exists: {os.path.exists(py_path)}")  # Debug log
                    print(f"  JSON file exists: {os.path.exists(json_path)}")  # Debug log
                    if os.path.exists(py_path) or os.path.exists(json_path):
                        topics.append(d)
            
            print(f"Found topics: {topics}")  # Debug log
            return sorted(topics)  # Sort alphabetically
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")  # Debug log
            return []
        except Exception as e:
            print(f"Unexpected error in get_topics: {e}")  # Debug log
            return []
    
    def get_questions(self, topic):
        try:
            # First try to load from .py file
            py_path = os.path.join(self.questions_dir, topic, 'questions.py')
            if os.path.exists(py_path):
                # Load the Python module dynamically
                spec = importlib.util.spec_from_file_location("questions", py_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                questions = module.questions
            else:
                # Fall back to JSON if .py doesn't exist
                json_path = os.path.join(self.questions_dir, topic, 'questions.json')
                with open(json_path, 'r') as f:
                    data = json.load(f)
                    questions = data["questions"]
            
            # Add index and topic to each question if not present
            for idx, question in enumerate(questions):
                question["id"] = idx + 1
                if "topic" not in question:
                    question["topic"] = topic
            return questions
        except (FileNotFoundError, ImportError, AttributeError) as e:
            print(f"Error loading questions for topic {topic}: {e}")
            return []
    
    def get_flagged_cards(self, topic):
        if 'flagged_cards' not in session:
            session['flagged_cards'] = {}
        return session['flagged_cards'].get(topic, [])

flashcard_manager = FlashcardManager()

@app.route('/')
def home():
    topics = flashcard_manager.get_topics()
    return render_template('index.html', topics=topics)

@app.route('/topic/<topic>')
def topic(topic):
    start_card = request.args.get('card', 1, type=int)
    questions = flashcard_manager.get_questions(topic)
    flagged_cards = flashcard_manager.get_flagged_cards(topic)
    return render_template('flashcards.html', 
                         topic=topic, 
                         questions=questions, 
                         start_card=start_card-1,  # Convert to 0-based index
                         flagged_cards=flagged_cards)

@app.route('/api/questions/<topic>')
def get_questions(topic):
    questions = flashcard_manager.get_questions(topic)
    return jsonify(questions)

@app.route('/api/flag-card', methods=['POST'])
def flag_card():
    data = request.json
    topic = data.get('topic')
    card_id = data.get('cardId')
    
    if 'flagged_cards' not in session:
        session['flagged_cards'] = {}
    
    if topic not in session['flagged_cards']:
        session['flagged_cards'][topic] = []
    
    if card_id in session['flagged_cards'][topic]:
        session['flagged_cards'][topic].remove(card_id)
        is_flagged = False
    else:
        session['flagged_cards'][topic].append(card_id)
        is_flagged = True
    
    session.modified = True
    return jsonify({'success': True, 'is_flagged': is_flagged})

@app.route('/topic/<topic>/flagged')
def flagged_cards(topic):
    questions = flashcard_manager.get_questions(topic)
    flagged_cards = flashcard_manager.get_flagged_cards(topic)
    flagged_questions = [q for q in questions if q['id'] in flagged_cards]
    return render_template('flashcards.html', 
                         topic=topic, 
                         questions=flagged_questions, 
                         start_card=0,
                         flagged_cards=flagged_cards,
                         flagged_mode=True)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run()

app = app.wsgi_app 