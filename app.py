from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk halaman form
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return render_template('submit.html', name=name, email=email)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
