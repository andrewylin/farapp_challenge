# adapted from Docker tutorial at "https://github.com/docker/labs/blob/master/
#   beginner/chapters/webapps.md"

from flask import Flask, render_template
from flask_oauthlib.provider import OAuth2Provider

app = Flask(__name__)
oauth = OAuth2Provider(app)


def create_app():
    app = Flask(__name__)
    oauth.init_app(app)
    return app


@app.route('/')
def index():
    url = "https://api.linkedin.com/v1/people/~?format=json"
    return render_template('index.html', url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
