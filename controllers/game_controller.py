from flask import Flask, render_template, request, redirect, Blueprint

games_blueprint = Blueprint("games", __name__)