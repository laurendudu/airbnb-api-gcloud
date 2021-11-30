from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

app = Flask(__name__)



@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    model = tf.keras.models.load_model('model_boston')
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    #model = tf.keras.models.load_model('model_boston')
    app.run(debug=True, host='0.0.0.0')