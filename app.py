from flask import Flask, render_template, request, url_for
from missions import get_mission_data
from trivia import trivia_questions
from glob import glob as my_glob
import os

app = Flask(__name__)

@app.route('/')
def home():
    mission_data = get_mission_data()
    images = {}
    for image in my_glob("static/images/*"):
        filename, file_extension = os.path.splitext(os.path.basename(image))
        images[filename] = image

    final_images = []
    for mission in mission_data:
        final_images.append({'url': images[str(mission['id'])], 'alt': mission['meta']})
    
    return render_template('index.html', images=final_images)

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
    images = my_glob("static/images/*")
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
            image_path = my_glob(f'static/images/{id}.*')[0]
            image = image_path.split("/")[-1]
            return render_template('mission_detail.html', mission=mission, keywords=keywords, total_missions=total_missions, image=image)
        else:
            return render_template('error.html',error_message="Mission not found"),404
    except Exception as e:
        return render_template('error.html',error_message=str(e)), 500


if __name__ == '__main__':
    app.run(debug=True)
