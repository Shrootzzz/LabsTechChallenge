from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/ww2472')
def me():
	return render_template('ww2472.html')

if __name__ == '__main__':
    app.run()
