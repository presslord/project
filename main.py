from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/login')
def login():
    return render_template('sign-up.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/logged')
def logg():
    return render_template('base-log.html')


@app.route('/logab')
def logab():
    return render_template('logged-about.html')


@app.route('/hogwards_legacy')
def hogwards():
    return render_template('hogwards-legacy.html')


@app.route('/loghog')
def hoglog():
    return render_template('loghog.html')


@app.route('/dead_space')
def dead():
    return render_template('dead_space.html')


@app.route('/deadlog')
def loded():
    return render_template('logspace.html')


@app.route('/atomic_heart')
def atomic():
    return render_template('atomic_heart.html')


@app.route('/logamic')
def heart():
    return render_template('logamic.html')


if __name__ == '__main__':
    app.run()
