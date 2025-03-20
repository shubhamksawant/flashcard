import os
import sys
from pathlib import Path

# Add parent directory to Python path to find app module
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.insert(0, str(parent_dir))

try:
    from app import app, db
    from models import Flashcard
except ImportError as e:
    print(f"Error importing required modules. Make sure you're running from the project root directory.")
    print(f"Error details: {e}")
    sys.exit(1)

import importlib.util

def load_module_from_file(file_path):
    """Dynamically load a Python module from file path"""
    try:
        spec = importlib.util.spec_from_file_location("questions", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def is_duplicate_question(question, topic):
    """Check if a question already exists in the database"""
    existing = Flashcard.query.filter_by(
        question=question,
        topic=topic
    ).first()
    return existing is not None

def load_questions():
    with app.app_context():
        # Use the directory where this script is located
        questions_dir = Path(__file__).parent
        total_added = 0
        total_skipped = 0
        topics_summary = {}

        # List of directories to ignore
        ignore_dirs = {'__pycache__', '.pytest_cache', '__init__'}

        # Only process existing topic directories
        for topic_dir in questions_dir.iterdir():
            # Skip files and ignored directories
            if not topic_dir.is_dir() or topic_dir.name in ignore_dirs:
                continue
                
            topic = topic_dir.name
            questions_file = topic_dir / "questions.py"
            
            if questions_file.exists():
                print(f"\nProcessing topic: {topic}")
                
                # Load questions from the file
                module = load_module_from_file(questions_file)
                if module and hasattr(module, 'questions'):
                    topic_added = 0
                    topic_skipped = 0
                    
                    for q in module.questions:
                        # Verify question has required fields
                        if all(key in q for key in ["question", "answer", "topic"]):
                            # Check for duplicates
                            if not is_duplicate_question(q["question"], q["topic"]):
                                card = Flashcard(
                                    question=q["question"],
                                    answer=q["answer"],
                                    topic=q["topic"]
                                )
                                db.session.add(card)
                                topic_added += 1
                            else:
                                topic_skipped += 1
                        else:
                            print(f"Skipping invalid question format in {topic}")
                    
                    # Update counters
                    total_added += topic_added
                    total_skipped += topic_skipped
                    topics_summary[topic] = {
                        'added': topic_added,
                        'skipped': topic_skipped
                    }
                    
                    print(f"- Added {topic_added} new questions")
                    print(f"- Skipped {topic_skipped} duplicate questions")
                else:
                    print(f"No questions found in {questions_file}")

        # Commit all changes
        db.session.commit()

        # Print final summary
        print("\n=== Final Summary ===")
        print(f"Total new questions added: {total_added}")
        print(f"Total duplicate questions skipped: {total_skipped}")
        print("\nBreakdown by topic:")
        for topic, stats in topics_summary.items():
            print(f"{topic}:")
            print(f"  - Added: {stats['added']}")
            print(f"  - Skipped: {stats['skipped']}")
            print(f"  - Total in DB: {Flashcard.query.filter_by(topic=topic).count()}")

if __name__ == "__main__":
    # Print current working directory for debugging
    print("Current working directory:", os.getcwd())
    print("Script location:", Path(__file__).resolve())
    
    try:
        load_questions()
    except Exception as e:
        print(f"Error running load_questions: {e}")
        sys.exit(1) 