import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <link rel="stylesheet" type="text/css" href="static/css/style.css" />
                                <link rel="stylesheet" 
                                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                                        crossorigin="anonymous">
                                <title>Привет, Марс!</title>
                              </head>
                              <body>
                                <h1>УРА!</h1>
                                <img src=static/img/MARS.jpg>
                                <div class="p-3 mb-2 bg-dark">
                                <font size="5" color="#FFFFFF">Привет всем, парни.</font>
                                </div>
                                <div class="p-3 mb-2 bg-success">
                                <font size="5" color="#FF0000">Я обещал немного покрасивее сделать.</font>
                                </div>
                                <div class="p-3 mb-2 bg-secondary">
                                <font size="5" color="#333333">И не придумал ничего лучше.</font>
                                </div>
                                <div class="p-3 mb-2 bg-warning">
                                <font size="5" color="#0000FF">Обычного Bootstrap</font>
                                </div>
                                <div class="p-3 mb-2 bg-danger">
                                <font size="5" color="#008000">Проверяйте! если что пишите</font>
                                </div>
                              </body>
                            </html>"""


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)