from flask import Flask
from flask import jsonify
from collections import OrderedDict
import json

app = Flask(__name__)

# a simple flask app to help me study the devnet exam
# this small api returns json data about different topics

@app.route('/iac', methods=['GET'])
def iac_get():
    jsonData = {
        "question":{
            "Q":"Which of the following is a benefit of defining all infrastructure as code?",
            "Answers": ["resilency", "elasticity", "resource pooling", "high availability"],
            "THE_ANSWER": "elasticity"
        }
    }
    return jsonify(jsonData)


@app.route('/py-mods', methods=['GET'])
def py_mods():
    jsonData = {
        "modules": ["pyang", "netmiko", "nornir", "pyats", "napalm"],
        "defnitions": ["a framework for converting YANG modules to other formats", "a library for simplifying SSH connections to network devices", "a pure python automation framework", "a test automation framework for network devices", "a unified API for interacting with routers from multiple vendors"]
    }
    return jsonify(jsonData)

@app.route('/dna-cata', methods=['GET'])
def dna_cata():
    jsonData = OrderedDict([
        ("question", "In the url, which of the following would indicate that the device was added successfully?"),
        ("answer", "if the isError field contained a false value")
    ])
    return jsonify(jsonData)

@app.route('/ucshandle')
def ucshandle():
    jsonData = {
        "code":"handle = UscHandle(10.1.14.32, boson, exsim, port=312, secure=1)",
        "question":"Why will the code fail?",
        "answer":"The code will fail because the secure parameter needs to be a boolean value (True or False)",
        "explanation":"parameters of he UcsHandle() constructor are ip, username, password, port, secure (Boolean True or False), proxy5"
    }
    return jsonify(jsonData)

@app.route('/dict', methods=['GET'])
def dict():
    jsonData = OrderedDict([
        ('name', 'jesse'),
        ('Book', 'The illiad')
    ])
    return jsonify(jsonData)
if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)