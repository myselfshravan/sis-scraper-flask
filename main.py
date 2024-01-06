from flask import Flask, jsonify, request
import os
import asyncio
from small_code import main

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


@app.route('/getdata', methods=['GET'])
def get_data():
    usn = request.args.get('usn')
    dob = request.args.get('dob')

    if not usn or not dob:
        return jsonify({'error': 'Missing USN or DOB'}), 400

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(main(usn, dob))
    loop.close()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
