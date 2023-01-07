// hide all questions except for the first one
let questions = document.querySelectorAll('.trivia-question');

for (let i = 1; i < questions.length; i++) {
    questions[i].style.display = "none";
}

// show the next question when the user submits an answer
document.querySelector('.trivia-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let currentQuestion = document.querySelector('.trivia-question:not([style*="display: none"])');
    let nextQuestion = currentQuestion.nextElementSibling;
    if (nextQuestion) {
        currentQuestion.style.display = "none";
        nextQuestion.style.display = "block";
    }
});