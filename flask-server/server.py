from flask import Flask, request, jsonify

from flask_cors import CORS

from dotenv import load_dotenv

import os

load_dotenv()

app = Flask(__name__) 

CORS(app)

app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

@app.route("/dialog")
def dialog():
    text = """
    No, not 'may be'. I am. When the mugger or the thief stop to think twice, that is fear. That is what I am. 
    That is why they hired assassins - because I am the reason the criminals breathe easier when the sun rises. 
    So no, Alfred, I am NOT in over my head. Tonight will not be my end. 
    But it will be theirs.
    """

    return jsonify({"text": text})


if __name__ == "__main__":
    app.run()