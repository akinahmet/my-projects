from flask import Flask 
# flask localhost:5000 portunda calisir
app = Flask(__name__) # app nesnesi olusturuyoruz

@app.route("/")  # decorator, ana sayfada yazilacak olan yaziyi tanimliyoruz
def head():
    return "Hello world from flask"

@app.route("/second") # ikinci sayfaya
def second():
    return "This is my second page"

@app.route("/third/subthird") 
def third():
    return "<h2>This is the subpath  of third page </h2>"

@app.route("/forth/<string:id>") 
def forth(id):
    return f'Id of this page is {id}'






if __name__ == "__main__": 
    #app.run(host='0.0.0.0', port=80)
    #app.run(debug=True, port=80) 
    app.run(debug=True)  # default olarak port 5000, ama bir üst satirlardaki gibi farkli port yapabilirsin