
from flask import Flask, jsonify, request

kisumu_app = Flask(__name__)

user1 =  'abraham'
pass1  =  'abraham'


@kisumu_app.route('/', methods=['POST'])
def login():
    user2 = request.get_json(force=True)['user']
    pass2 = request.get_json(force=True)['pass']
    valid = 0

    if (user2 == ""):
      status = 000000
      valid = 1
      return jsonify({'message' : 'Username cannot be blank', 'status' : status})
    

    if (valid == 0):
            if (user1 == str(user2)):
                if (pass1 == pass2):
                    status = 200
                    return jsonify({'message' : 'Login successful', 'status' : status})
                else:
                    status = 401
                    return jsonify({'message' : 'Username and password do not match', 'status' : status})

            else:
                status = 501
                return jsonify({'message' : 'No such user', 'status' : status})


if __name__ == '__main__':
    kisumu_app.run(debug=True, port=8090)
