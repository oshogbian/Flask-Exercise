from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Get the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Render the template with the current time
    return render_template('index.html', current_time=current_time)

if __name__ == "__main__":
    app.run(debug=True)
