# -*- coding:utf-8 -*-
# Flasks minimal entry app
# flask refresher
# ref: https://pythonise.com/series/learning-flask/application-factory-pattern-|-learning-flask-ep.-30


from flask import Flask

app = Flask(__name__)

from app import  views

"""To avoid circular dependency issues,
we must import views after creating the app variable,
along with any other objects we need to
import that reference the app object.
"""
if __name__ == '__main__':
    app.run()