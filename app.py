from flask import Flask, render_template, request
from missions import get_mission_data
from trivia import trivia_questions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/trivia', methods=['GET', 'POST'])
def trivia():
    if request.method == 'POST':
        answers = request.form

        score = 0
        for question in trivia_questions:
            correct_answer = question['answer']
            user_answer = answers.get(question['question'])
            if user_answer == correct_answer:
                score += 1

        return render_template('trivia_results.html', score=score, total=len(trivia_questions), questions=trivia_questions)
    else:
        return render_template('trivia.html', questions=trivia_questions)

@app.route('/timeline')
def timeline():
    missions = get_mission_data()
    return render_template('timeline.html', missions=missions)

@app.route('/missions')
def missions():
    missions = get_mission_data()
    return render_template('mission_list.html', missions=missions)

@app.route('/mission/<int:id>')
def mission_detail(id):
    mission = get_mission_data(id)
    if mission:
        return render_template('mission_detail.html', mission=mission)
    else:
        return "Mission not found", 404

if __name__ == '__main__':
    app.run(debug=True)
