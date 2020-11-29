from PIL import Image
from flask import Flask, request, jsonify, render_template, url_for, send_file
import numpy as np

app = Flask(__name__)


@app.route('/status')
def status():
    """
    This is a status route endpoint.
    :param: GET /status
    :return: 'Alive!'
    """
    return 'Alive!'


@app.route("/login", methods=['POST', 'GET'])
def login():
    """
        This is a login route endpoint.

        :param: POST /login
        :return: json data ,Login Success for User  {USER_NAME_HERE} with password length  {PASSWORD_LENGTH_HERE}!"
    """
    if request.method == 'POST':
        req = request.get_json()
        username = req['Username']
        password = req['Password']
        response_data = 'Login Success for User {} with password length: {}!'.format(username, len(password))
        return jsonify(response_data)


@app.route('/predict')
def predict():
    """
        This is a  predict route endpoint.

        :param: GET /predict
        :return:Prediction (int between 2000 and 5000)
    """

    data = request.get_json()
    month = data['month']
    customer_visiting_website = data['customer_visiting_website']
    seller_available = data['seller_available']

    return jsonify(np.random.randint(2000, 5000))


@app.route("/image", methods=['POST'])
def image():
    """
           This is a  image route endpoint.

           :param: POST /image
           :return: uploaded image is saved in the server
    """
    file = request.files['image']
    img = Image.open(file)
    img = img.resize((100, 100), Image.ANTIALIAS)
    img.save("images/output.png")
    return send_file("images/output.png", mimetype="image/png")


@app.route('/login1', methods=['POST', 'GET'])
def login1():
    """
               This is a  login1 route endpoint.

               :param: POST /username, password
               :return: receive form data and print message "Login Success for User with password length: !"
    """
    error = None

    message = ''
    if request.method == 'POST':
        user = request.form["Username"]

        passd = request.form["Password"]

        if user == "" or passd == "":
            message = ''
        else:
            message = 'Login Success for User {} with password length: {}!'.format(user, len(passd))

    # return render_template('login.html', message=message)
    return message


if __name__ == '__main__':
    app.run(debug=True, port=5000)
