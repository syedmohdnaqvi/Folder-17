from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def registration_form():
    return render_template('registration_form.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    # Here you can add code to store the registration details in a database or perform other actions
    
    return "Registration successful!"

if __name__ == '__main__':
    app.run(debug=True)
