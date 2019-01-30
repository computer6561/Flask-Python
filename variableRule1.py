#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 23:54:09 2019

@author: sunil
"""

from flask import Flask
app = Flask(__name__)

@app.route("/roll/<int:roll>")
def studentid(roll):
    return "Hello World %d!" % roll
@app.route("/price/<float:p>")
def food(p):
    return "Hello World %f!" % p

if __name__ == "__main__":
    app.run()  