# coding: utf-8
from . import app
from flask import render_template


@app.errorhandler(404)
def page_not_found(erro):
    return render_template('/erros/404.html'), 404
