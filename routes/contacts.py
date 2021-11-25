from flask import Blueprint

contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def home():
    return "contact lsit."


@contacts.route("/new")
def add_contact():
    return "saving a contact."
