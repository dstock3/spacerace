import random

trivia_questions = [
    {
        'question': 'What was the first manned mission of the Mercury program?',
        'answer': 'Mercury-Redstone 3',
        'options': ['Gemini 7', 'Vostok 1', 'Mercury-Redstone 3'],
    },
    {
        'question': 'Who was the first person to walk on the Moon?',
        'answer': 'Neil Armstrong',
        'options': ['Buzz Aldrin', 'Neil Armstrong', 'John Glenn'],
    },
    {
        'question': 'Which spacecraft was used for the first space shuttle mission?',
        'answer': 'Columbia',
        'options': ['Discovery', 'Endeavour', 'Columbia'],
    },
    {
        'question': 'Which NASA spacecraft was the first to orbit another planet?',
        'answer': 'Mariner 2',
        'options': ['Mariner 2', 'Viking 1', 'Galileo'],
    },
    {
        'question': 'What was the first spacecraft to land a rover on Mars?',
        'answer': 'Sojourner',
        'options': ['Sojourner', 'Curiosity', 'Spirit'],
    },
    {
        'question': 'Which spacecraft was the first to carry humans beyond low Earth orbit?',
        'answer': 'Apollo 8',
        'options': ['Gemini 7', 'Apollo 8', 'Skylab'],
    },
    {
        'question': 'What was the first spacecraft to land on an asteroid?',
        'answer': 'Hayabusa',
        'options': ['Hayabusa', 'OSIRIS-REx', 'Dawn'],
    },
    {
        'question': 'What was the first spacecraft to land on a comet?',
        'answer': 'Philae',
        'options': ['Hayabusa', 'Philae', 'Dawn'],
    },
    {
        'question': 'Which country launched the first satellite into space?',
        'answer': 'USSR',
        'options': ['USSR', 'USA', 'China'],
    },
    {
        'question': 'Which country sent the first human into space?',
        'answer': 'USSR',
        'options': ['USSR', 'USA', 'China'],
    }
]

def get_random_question():
    return random.choice(trivia_questions)