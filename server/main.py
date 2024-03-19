from flask import Flask, request
import controller.game_controller as gc

app = Flask(__name__)


@app.route('/game/<uuid:game_id>', methods=['GET'])
def get_game(uuid: str):
    gc.get_game(uuid)


@app.route('/game', methods=['POST'])
def create_game():
    data = request.json
    gc.create_game()
