from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room
from collections import defaultdict
from .blackjack import Deck, Player


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


count = 0
rooms = defaultdict(list)

@app.route('/')
def hello_world():
    return render_template('main.html')

@socketio.on('my event')
def handle_message(data):
    print('received message: ' + data['data'])
    emit('count', count)

@socketio.on('click')
def apa(clicks):
    global count
    count = count + 1
    emit('count', count, broadcast=True)

def start_game(room):
    deck = Deck()
    deck.shuffle()

    for i in range(0, len(rooms[room])):
        rooms[room][i]['player'] = Player(rooms[room][i]['user'])
        rooms[room][i]['player'].draw_n(deck, 13)


@socketio.on('join')
def on_join(data):
    global rooms
    print(data)
    if len(rooms[data['room']]) > 3:
        return
    rooms[data['room']].append(
        {
            'user': data['user'],
            'sid': request.sid
        }
    )
    join_room(data['room'])
    emit('new_user', data['user'], room=data['room'])
    print('new user in room "' + data['room'] + '", name "' + data['user'] + '"')
    if len(rooms[data['room']]) > 3:
        start_game(data['room'])

if __name__ == '__main__':
    socketio.run(app)