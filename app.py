from flask import Flask, render_template, jsonify, request, redirect, url_for
from models import db, Flashcard, StudySession, Progress
from datetime import datetime
from sqlalchemy.sql import func
import os
from werkzeug.utils import secure_filename
import json
import sys
from pathlib import Path
import importlib.util
import shutil

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flashcards.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join('instance', 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'json', 'py'}

db.init_app(app)

# Instead, create upload directory only when needed
def ensure_upload_folder():
    """Create upload folder only when needed"""
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Only one index route should exist
@app.route('/')
def index():
    # Get all unique topics and their counts from database
    topics = db.session.query(
        Flashcard.topic,
        db.func.count(Flashcard.id).label('count'),
    ).group_by(Flashcard.topic).all()
    
    # Create a dictionary of topic information
    topic_info = {
        'aws': {'title': 'AWS', 'description': 'Cloud Computing Concepts'},
        'cicd': {'title': 'CI/CD', 'description': 'Continuous Integration/Deployment'},
        'docker': {'title': 'Docker', 'description': 'Container Technology'},
        'git': {'title': 'Git', 'description': 'Version Control System'},
        'kubernetes': {'title': 'Kubernetes', 'description': 'Container Orchestration'},
        'linux': {'title': 'Linux', 'description': 'Operating System Fundamentals'},
        'iac': {'title': 'Infrastructure as Code', 'description': 'IaC Concepts and Tools'},
        'ansible': {'title': 'Ansible', 'description': 'Automation Tool'},
        'database': {'title': 'Database', 'description': 'Database Concepts'},
        'buildtools': {'title': 'Build Tools', 'description': 'Software Build and Package Tools'},
        'scripting': {'title': 'Scripting', 'description': 'Automation Scripting'},
        'monitoring': {'title': 'Monitoring', 'description': 'Application and System Monitoring'},
        # Add any new topics here with their display information
    }
    
    return render_template('index.html', 
                         topics=topics,
                         topic_info=topic_info)

@app.route('/study/<topic>')
def study(topic):
    cards = Flashcard.query.filter_by(topic=topic).all()
    cards_data = [{
        'id': card.id,
        'question': card.question,
        'answer': card.answer,
        'topic': card.topic
    } for card in cards]
    
    return render_template('study.html', 
                         cards=cards_data, 
                         topic=topic)

@app.route('/api/progress', methods=['POST'])
def update_progress():
    data = request.json
    progress = Progress.query.filter_by(
        user_id=1,
        topic=data['topic']
    ).first()
    
    if not progress:
        progress = Progress(topic=data['topic'])
        db.session.add(progress)
    
    progress.cards_reviewed += 1
    if data.get('correct'):
        progress.correct_answers += 1
    
    db.session.commit()
    return jsonify({'status': 'success'})

@app.route('/stats')
def stats():
    progress = Progress.query.filter_by(user_id=1).all()
    return render_template('stats.html', progress=progress)

@app.route('/admin')
def admin():
    # Get count of cards for each topic
    topics = db.session.query(Flashcard.topic, db.func.count(Flashcard.id)).\
        group_by(Flashcard.topic).all()
    topic_counts = dict(topics)
    
    return render_template('admin.html', 
                         topic_counts=topic_counts,
                         message=request.args.get('message'),
                         message_type=request.args.get('type'))

def ensure_topic_directory(topic):
    """Create topic directory if it doesn't exist"""
    questions_dir = Path("questions")
    topic_dir = questions_dir / topic
    if not topic_dir.exists():
        topic_dir.mkdir(parents=True)
    return topic_dir

def save_questions_to_file(questions, topic):
    """Save questions to a Python file in the topic directory"""
    topic_dir = ensure_topic_directory(topic)
    questions_file = topic_dir / "questions.py"
    
    # If file exists, load existing questions
    existing_questions = []
    if questions_file.exists():
        try:
            spec = importlib.util.spec_from_file_location("existing_questions", questions_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, 'questions'):
                existing_questions = module.questions
        except Exception as e:
            print(f"Error loading existing questions: {e}")

    # Combine existing and new questions, avoiding duplicates
    all_questions = existing_questions.copy()
    new_questions = []
    
    for q in questions:
        if q not in existing_questions:
            all_questions.append(q)
            new_questions.append(q)

    # Write all questions to file
    with open(questions_file, 'w', encoding='utf-8') as f:
        f.write("questions = [\n")
        for q in all_questions:
            f.write("    {\n")
            f.write(f'        "question": """{q["question"]}""",\n')
            f.write(f'        "answer": """{q["answer"]}""",\n')
            f.write(f'        "topic": "{q["topic"]}"\n')
            f.write("    },\n")
        f.write("]\n")
    
    return new_questions

@app.route('/upload-questions', methods=['POST'])
def upload_questions():
    if 'questionFile' not in request.files:
        return redirect(url_for('admin', 
                              message='No file uploaded',
                              type='error'))
    
    file = request.files['questionFile']
    if file.filename == '':
        return redirect(url_for('admin', 
                              message='No file selected',
                              type='error'))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        
        # Create upload directory if it doesn't exist
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Process the uploaded file
            if filename.endswith('.json'):
                with open(filepath, 'r') as f:
                    questions = json.load(f)
            elif filename.endswith('.py'):
                # Import the Python file dynamically
                spec = importlib.util.spec_from_file_location("questions", filepath)
                questions_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(questions_module)
                
                # Collect all question lists from the module
                questions = []
                for attr in dir(questions_module):
                    if attr.endswith('_questions') or attr.startswith('new_'):
                        questions.extend(getattr(questions_module, attr))
            
            # Group questions by topic
            questions_by_topic = {}
            for q in questions:
                topic = q['topic']
                if topic not in questions_by_topic:
                    questions_by_topic[topic] = []
                questions_by_topic[topic].append(q)
            
            # Process each topic's questions
            total_added = 0
            total_files_updated = 0
            
            for topic, topic_questions in questions_by_topic.items():
                # Save questions to topic directory
                new_questions = save_questions_to_file(topic_questions, topic)
                
                # Add new questions to database
                for q in new_questions:
                    # Check if question already exists in database
                    existing = Flashcard.query.filter_by(
                        question=q['question'],
                        topic=q['topic']
                    ).first()
                    
                    if not existing:
                        card = Flashcard(
                            question=q['question'],
                            answer=q['answer'],
                            topic=q['topic']
                        )
                        db.session.add(card)
                        total_added += 1
                
                if new_questions:
                    total_files_updated += 1
            
            db.session.commit()
            
            # Clean up uploaded file
            os.remove(filepath)
            
            # Try to remove upload directory if empty
            try:
                os.rmdir(app.config['UPLOAD_FOLDER'])
            except OSError:
                pass
            
            message = (f'Successfully added {total_added} new questions! '
                      f'Updated {total_files_updated} topic files.')
            return redirect(url_for('admin', message=message, type='success'))
            
        except Exception as e:
            return redirect(url_for('admin', 
                                  message=f'Error processing file: {str(e)}',
                                  type='error'))
    
    return redirect(url_for('admin', 
                          message='Invalid file type',
                          type='error'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)