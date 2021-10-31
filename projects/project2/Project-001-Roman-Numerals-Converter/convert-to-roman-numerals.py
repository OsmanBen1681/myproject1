
# convert the given number to the roman numerals
def convert(decimal_num):
    # set the dictionary for roman numerals
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
             50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    # initialize the result variable
    num_to_roman = ''
    # loop the roman numerals, calculate for each symbol and add to the result
    for i in roman.keys():
        num_to_roman += roman[i] * (decimal_num // i)
        decimal_num %= i
    return num_to_roman


from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", developer_name="Ahmet KARA")

@app.route("/calc", methods = ["GET", "POST"])
def calculate():
    if request.method == "POST":
        num1 = request.form.get("number")
        
        return render_template("result.html", number_decimal=num1,  number_roman=convert(int(num1)), developer_name="Ahmet KARA")
    else:
        return render_template("result.html", developer_name="Ahmet KARA")

if __name__== "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
