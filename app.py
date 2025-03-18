from flask import Flask, render_template, jsonify, request, session, send_from_directory
import json
import os
import random

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

class FlashcardManager:
    def __init__(self):
        self.questions_dir = "questions"
    
    def get_topics(self):
        """Get all available topics by scanning the questions directory"""
        try:
            # Get all directories in the questions folder
            topics = [d for d in os.listdir(self.questions_dir) 
                     if os.path.isdir(os.path.join(self.questions_dir, d))
                     and os.path.exists(os.path.join(self.questions_dir, d, 'questions.json'))]
            return sorted(topics)  # Sort alphabetically
        except FileNotFoundError:
            return []
    
    def get_questions(self, topic):
        try:
            with open(os.path.join(self.questions_dir, topic, 'questions.json'), 'r') as f:
                data = json.load(f)
                # Add index to each question
                for idx, question in enumerate(data["questions"]):
                    question["id"] = idx + 1
                return data["questions"]
        except FileNotFoundError:
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