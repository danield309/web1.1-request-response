
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
from flask import Flask

app = Flask(__name__)

# home page route
@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

# penguin route
@app.route('/penguins')
def penguins():    
    return 'Penguins are cute!'

# user favorite animal route
@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

# user favorite dessert route
@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

# mad libs route
@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f'This coming election is like {noun} and {adjective} had a baby.'

# multiply route *** NEED HELP ON THIS ***
@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Display a message to the user that changes when 2 numbers are placed in the url"""

    if number1.isdigit() and number2.isdigit():
        return f'{int(number1)} times {int(number2)} is {int(number1) * int(number2)}.'

    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"
if __name__ == '__main__':
    app.run(debug=True)
