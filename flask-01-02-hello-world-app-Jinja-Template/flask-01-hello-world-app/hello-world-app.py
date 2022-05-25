from flask import Flask 

app = Flask(__name__) # app nesnesi olusturuyoruz

@app.route("/")  # decorator
def head():
    return "Hello world from flask"

@app.route("/second")
def second():
    return "This is my second page"

@app.route("/third/subthird")
def third():
    return "<h2>This is the subpath of third page</h2>"

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    #app.run(debug=True, port=3000)