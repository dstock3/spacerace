from flask import Flask, render_template, request, url_for
from missions import get_mission_data
from trivia import trivia_questions
from glob import glob
import os

app = Flask(__name__)

@app.route('/')
def home():
    images = [
        {'url': url_for('static', filename='images/image1.jpg'), 'alt': 'image 1'},
        {'url': url_for('static', filename='images/image2.jpg'), 'alt': 'image 2'},
        {'url': url_for('static', filename='images/image3.jpg'), 'alt': 'image 3'}
    ]
    return render_template('index.html', images=images)

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
    mission_data = get_mission_data()
    images = glob("static/images/*")
    for mission in mission_data:
        for image in images:
            filename, file_extension = os.path.splitext(os.path.basename(image))
            if filename == str(mission['id']):
                mission['image'] = image
                break
    return render_template('timeline.html', missions=mission_data)



@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/mission/<int:id>')
def mission_detail(id):
    try:
        mission = get_mission_data(id)
        if mission:
            total_missions = len(get_mission_data())
            keywords = ', '.join(mission['keywords'])
            image_path = glob.glob(f'static/images/{id}.*')[0]
            image = image_path.split("/")[-1]
            return render_template('mission_detail.html', mission=mission, keywords=keywords, total_missions=total_missions, image=image)
        else:
            return render_template('error.html',error_message="Mission not found"),404
    except Exception as e:
        return render_template('error.html',error_message=str(e)), 500


if __name__ == '__main__':
    app.run(debug=True)
