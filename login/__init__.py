
# 登陆页面

import flask
from flask import request
from flask import Blueprint

login_in=Blueprint("login_in",__name__)

@login_in.route("/login",methods=["post"])
def login():
    data=request.get_json()

    account=data.get("account")
    password=data.get("password")
    login_type=data.get("password")
