#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 23:44:54 2019

@author: sunil
"""


from flask import Flask
app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return "Hello World %s!" % name

if __name__ == "__main__":
    app.run()  