from flask import Flask, render_template, request
from data.scraper import scrape_fighters
from flask_socketio import SocketIO

app = Flask(__name__, template_folder='templates')
socketio = SocketIO(app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["POST","GET"])
async def result():
    fighter1 = request.json['fighter1']
    fighter2 = request.json['fighter2']
    print(f"fighter1 Value is {fighter1}")
    print(f"fighter2 Value is {fighter2}")
    fighter1_list = await scrape_fighters(fighter1)
    fighter2_list = await scrape_fighters(fighter2)
    print(f"fighter1_list Value is {fighter1_list}")
    print(f"fighter2 list is {fighter2_list}")
    return render_template('results.html', fighter1_list=fighter1_list, fighter2_list = fighter2_list)

if __name__ == '__main__':
    app.run(debug=True)