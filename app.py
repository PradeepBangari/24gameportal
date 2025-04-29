from flask import Flask, render_template
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/puzzle')
def puzzle():
    return render_template('puzzle.html')

# Add this to your existing imports and app configuration
ads = {
    'left': {'title': 'Left Ad Space', 'content': 'Advertisement Space Left'},
    'right': {'title': 'Right Ad Space', 'content': 'Advertisement Space Right'}
}

@app.route('/ads')
def manage_ads():
    return render_template('ads.html')

@app.route('/save_ad', methods=['POST'])
def save_ad():
    title = request.form.get('title')
    content = request.form.get('content')
    position = request.form.get('position')
    ads[position] = {'title': title, 'content': content}
    return redirect(url_for('manage_ads'))

@app.route('/tetris')
def tetris():
    return render_template('tetris.html', ads=ads)

if __name__ == '__main__':
    app.run(debug=True)