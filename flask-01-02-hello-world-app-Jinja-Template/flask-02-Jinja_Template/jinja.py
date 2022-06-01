from flask import Flask, render_template 
# render template bir fonksiyon, birazdan ekleyecegimiz html dosyalarini cagirmak icin 

app = Flask(__name__) # nesne tanimliyoruz

@app.route("/") # ana sayfa
def head():
    return render_template('index.html', number1 = 20, number2 = 40)

@app.route("/mult")
def number():
    var1, var2 = 30, 70
    return render_template('body.html', num1=var1, num2=var2, mul=var1*var2)


if __name__ == "__main__":
    
    # app.run(host='0.0.0.0', port=80)
    app.run(debug=True)