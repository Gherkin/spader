from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room
from collections import defaultdict
from blackjack import Deck, Player, Card


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


count = 0
rooms = defaultdict(dict)

@app.route('/')
def hello_world():
    return render_template('main.html')

@socketio.on('declare')
def declare(data):
    print(data)
    room = rooms[data['room']]
    declaring_ = room['declaring']
    player = room['players'][declaring_]['player']
    if request.sid != room['players'][declaring_]['sid']:
        return
    player.declare(data['n'])

    if declaring_ == 3:
        emit('play', True, room=room['players'][room['starter']]['sid'])
        return


    room['declaring'] = declaring_ + 1

    emit('declare', True, room=room['players'][room['declaring']]['sid'])

def start_game(room):
    deck = Deck()
    deck.shuffle()
    print('starting game for room ' + room)

    starter = -1

    club = Card(Card.CLUBS, 2)
    print(rooms[room])
    for i in range(0, len(rooms[room]['players'])):
        rooms[room]['players'][i]['player'] = Player(rooms[room]['players'][i]['user'])
        player_ = rooms[room]['players'][i]
        player_['player'].draw_n(deck, 13)
        if player_['player'].has(club):
            starter = i

        emit('hand', player_['player'].serialize(), room=player_['sid'])

    print('starting player is ' + str(starter))
    rooms[room]['starter'] = starter

    emit('declare', True, room=rooms[room]['players'][0]['sid'])
    rooms[room]['declaring'] = 0

@socketio.on('join')
def on_join(data):
    global rooms
    print(data)
    room = data['room']
    if 'players' not in rooms[room]:
        rooms[room]['players'] = []

    if len(rooms[room]['players']) > 3:
        return

    rooms[room]['players'].append(
        {
            'user': data['user'],
            'sid': request.sid
        }
    )
    join_room(room)
    print('sid! ' + request.sid)
    emit('new_user', data['user'], room=room)
    print('new user in room "' + room + '", name "' + data['user'] + '"')
    if len(rooms[room]['players']) > 3:
        start_game(room)

if __name__ == '__main__':
    socketio.run(app)