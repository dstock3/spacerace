let questions = document.querySelectorAll('.trivia-question');

for (let i = 1; i < questions.length; i++) {
    questions[i].style.display = "none";
}

let triviaOptions = document.querySelectorAll('.trivia-option');

for (let i = 0; i < triviaOptions.length; i++) {
    let lineItem = triviaOptions[i]
    let radio = lineItem.firstChild

    lineItem.addEventListener('click', function(event) {
        radio.checked = true;
        lineItem.style.backgroundColor = "#555"

        for (let x = 0; x < triviaOptions.length; x++) {
            if (lineItem.textContent !== triviaOptions[x].textContent) {
                triviaOptions[x].style.backgroundColor = "rgba(44, 44, 44, 0.605)"
            }
        }
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