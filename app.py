from flask import Flask, render_template
from missions import get_mission_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/missions')
def mission_list():
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