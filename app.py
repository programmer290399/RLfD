from flask import Flask, render_template
from file_read_backwards import FileReadBackwards

app = Flask(__name__, template_folder="templates")



@app.route('/', methods=["GET", "POST"])
def index():
    with FileReadBackwards("/home/saahil/rps/dffml/server.log") as f:
        b_lines = [ row for row in f ]
    return render_template('index.html', b_lines=b_lines)

if __name__ == "__main__":
    app.run(debug=True)