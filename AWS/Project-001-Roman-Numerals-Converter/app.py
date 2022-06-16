from flask import Flask, render_template, request  # import Flask, template and request

app = Flask(__name__)

def convert(decimal_num):  # converter function
    roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    num_to_roman = ''

    for i in roman.keys():
        num_to_roman += roman[i]*(decimal_num//i) 
        decimal_num %= i
    return num_to_roman


@app.route('/', methods=['POST', 'GET'])  # post and get methods
def main_post():
    if request.method == 'POST':
        alpha = request.form['number']
        if not alpha.isdecimal():  
            return render_template('index.html', developer_name='Ahmet', not_valid=True)
        number = int(alpha)
        if not 0 < number < 4000:
            return render_template('index.html', developer_name='Ahmet', not_valid=True)
        return render_template('result.html', number_decimal = number , number_roman= convert(number), developer_name='Ahmet')
    else:
        return render_template('index.html', developer_name='Ahmet', not_valid=False)  # hicbirisi degil ise sonucu göster

if __name__ == '__main__':
    app.run(debug=True)  # önce lokalde kontrol et flask standart portu 5000 
    # app.run(host='0.0.0.0', port=80)  # heryerden 80 portunu ac
