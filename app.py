from flask import Flask, redirect, url_for, render_template, request
from RRT import gen_image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    image_path = './static/test.png'
    if request.method == 'POST':
        start_x = request.form['inputStartX']
        start_y = request.form['inputStartY']
        end_x = request.form['inputEndX']
        end_y = request.form['inputEndY']
        noObstacles = request.form['noObstacles']
        gen_image.generate_image(start_x,start_y,end_x,end_y,noObstacles)
        image_path = './static/solution.png'
    return render_template('index.html',image_path=image_path)



