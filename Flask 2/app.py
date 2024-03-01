from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form.get('number', None)
        if number is not None:
            try:
                number = int(number)
                if number % 2 == 0:
                    result = "Even number"
                else:
                    result = "Odd number"
            except ValueError:
                result = "Not an integer"
        else:
            result = "No input provided"
        return render_template('result.html', result=result)
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
