function setMode(mode) {
    // Remove active class from all buttons
    document.querySelectorAll('.mode-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Add active class to selected mode
    document.querySelector(`.mode-btn[onclick*="${mode}"]`).classList.add('active');
    
    // Store selected mode
    localStorage.setItem('studyMode', mode);
}

// Initialize with stored mode or default to standard
document.addEventListener('DOMContentLoaded', () => {
    const storedMode = localStorage.getItem('studyMode') || 'standard';
    setMode(storedMode);
});

let currentCardIndex = 0;
const cardsData = {{ cards|tojson|safe }};
let studyMode = '{{ mode }}';

// Initialize the study session
function initStudySession() {
    showCard(0);
    updateProgress();
    
    // Show mode-specific instructions
    const modeInstructions = {
        'standard': 'Review cards in order. Click card to see answer.',
        'spaced': 'Difficult cards will appear more frequently.',
        'quiz': 'Test your knowledge - try to answer before flipping!'
    };
    
    alert(modeInstructions[studyMode] || modeInstructions['standard']);
}

// Show explanation of study modes
function explainModes() {
    const explanation = `
Study Modes:
- Standard: Review cards in sequence
- Spaced: Focus on cards you find difficult
- Quiz: Test mode with scoring
    `;
    alert(explanation);
}

// Rate card and handle spaced repetition
function rateCard(difficulty) {
    // Store the card's difficulty for spaced repetition
    localStorage.setItem(`card-${cardsData[currentCardIndex].id}`, difficulty);
    
    // In spaced mode, move difficult cards to appear sooner
    if (studyMode === 'spaced' && difficulty < 3) {
        // Implementation for spaced repetition
        const currentCard = cardsData[currentCardIndex];
        cardsData.splice(currentCardIndex + 2, 0, currentCard);
    }
    
    nextCard();
}

// Call initStudySession when the page loads
document.addEventListener('DOMContentLoaded', initStudySession);