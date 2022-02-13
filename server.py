from flask import Flask, render_template
from random import randint

app = Flask(__name__)

word_list = ['apple', 'house', 'title']
currentWord = list(word_list[randint(0, len(word_list) - 1)])
guessWord = list('-' * len(currentWord))

@app.route('/')
@app.route('/hello')
def index():
    return ''.join(guessWord)


@app.route('/letter/<string:letter>')
def get_params(letter):
    print(letter)
    print(currentWord)
    if letter in currentWord:
        for i in range (len(currentWord)):
            if currentWord[i] == letter:
                guessWord[i] = letter
                print(guessWord)
    return ''.join(guessWord)



if __name__ == '__main__':
    app.run(debug=True)