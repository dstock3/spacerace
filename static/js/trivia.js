let questions = document.querySelectorAll('.trivia-question');

for (let i = 1; i < questions.length; i++) {
    questions[i].style.display = "none";
}

let triviaOptions = document.querySelectorAll('.trivia-option');

for (let i = 0; i < triviaOptions.length; i++) {
    let radio = triviaOptions[i].firstChild
    triviaOptions[i].addEventListener('click', function(event) {
        radio.checked = true;
    });
}



let submitButton = document.querySelector('button[type="submit"]');
submitButton.innerHTML = "Next Question";

document.querySelector('.trivia-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let currentQuestion = document.querySelector('.trivia-question:not([style*="display: none"])');
    let nextQuestion = currentQuestion.nextElementSibling;
       
    if (currentQuestion.id !== 10) {
        currentQuestion.style.display = "none";
        nextQuestion.style.display = "block";
    }

    if (nextQuestion.id == 10) submitButton.innerHTML = "Submit";

    if (currentQuestion.id == 10) document.querySelector('.trivia-form').submit();
});