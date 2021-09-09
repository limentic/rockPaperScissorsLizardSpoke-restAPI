from flask import Flask, request, jsonify
from flask_restx import Resource, Api
from random import choice

app = Flask(__name__)
api = Api(app)

# Ce tableau à deux dimentions est la table de verité du jeu.
# 0: Perdu
# 1: Gagné
# 2: Egalité
# En le parcourant sur x,y cela permet de retrouver la valeur de cette combinaison.
#                Lizard            Paper            Rock           Scissors           Spock
test_case = [[2, 1, 0, 0, 1], [0, 2, 1, 0, 1], [1, 0, 2, 0, 1], [1, 1, 0, 2, 0], [0, 0, 1, 1, 2]]

# Tableau de noms pour l'affichage.
# Cela permet d'éviter de devoir faire une boucle for alors que ces noms sont constants.
names = ['Lizard', 'Paper', 'Rock', 'Scissors', 'Spock']

# Définission de notre route
@api.route('/play')
class RockPaperScissorsLizardSpoke(Resource):
    # On utilise une methode get
    def get(self):
        try:
            user_input = int(request.args.get('choice'))

            if user_input < 0 or user_input > 4:
                raise ValueError('The value should be in between 0 and 4')

            # On génére un nombre aléatoire qui ne sera pas le même que celui de l'utilisateur.
            algorithm_choice = choice([i for i in range(0, 4) if i not in [user_input]])

            user_play = names[user_input]
            computer_play = names[algorithm_choice]
            result = ""

            # C'est ici que nous décidons si le joueur à gagné ou non.
            # Nous utilisons la table de verité définie précedement.
            if test_case[user_input][algorithm_choice] == 0:
                result = 'You loosed! (sad)'
            elif test_case[user_input][algorithm_choice] == 1:
                result = 'You won! (wow)'
            else:
                result = 'Draw'

            return jsonify(
                userPlay=user_play,
                computerPlay=computer_play,
                result=result
            )
        except ValueError as err:
            return err.args


if __name__ == '__main__':
    app.run(debug=True)
