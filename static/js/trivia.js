let questions = document.querySelectorAll('.trivia-question');

for (let i = 1; i < questions.length; i++) {
    questions[i].style.display = "none";
}

let submitButton = document.querySelector('button[type="submit"]');

document.querySelector('.trivia-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let currentQuestion = document.querySelector('.trivia-question:not([style*="display: none"])');
    let nextQuestion = currentQuestion.nextElementSibling;
    if (nextQuestion) {
        currentQuestion.style.display = "none";
        nextQuestion.style.display = "block";
        submitButton.innerHTML = nextQuestion.dataset.next ? "Next Question" : "Submit";
    }
});