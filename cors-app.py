from flask import Flask, request, jsonify, make_response
import numpy as np
import tensorflow as tf

app = Flask(__name__)

@app.route("/api/", methods=["POST", "OPTIONS"])
def makecalc():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    elif request.method == "POST": # The actual request following the preflight
        data = request.get_json()
        model = tf.keras.models.load_model('model_boston')
        prediction = np.array2string(model.predict(data))
        return _corsify_actual_response(jsonify(prediction))
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')