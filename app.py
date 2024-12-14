from flask import Flask, render_template, request, redirect, url_for
import random
import os

app = Flask(__name__)

# Global variable to store the secret number
secret_number = random.randint(1, 100)
attempts = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global attempts
    if request.method == 'POST':
        guess = int(request.form['guess'])
        attempts += 1
        if guess < secret_number:
            message = "Too low! Try again."
        elif guess > secret_number:
            message = "Too high! Try again."
        else:
            message = f"Congratulations! You guessed it in {attempts} attempts."
            reset_game()
        return render_template('index.html', message=message, attempts=attempts)
    return render_template('index.html', message="Guess the number between 1 and 100!", attempts=attempts)

def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0

if __name__ == '__main__':
    # Use the port provided by Render or default to 5000 for local testing
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
