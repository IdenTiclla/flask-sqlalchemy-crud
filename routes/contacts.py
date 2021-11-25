from flask import Blueprint, render_template, request, redirect
from models.contact import Contact
from utils.db import db

contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def home():
    return render_template("index.html")


@contacts.route("/new", methods=["POST"])
def add_contact():
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]

    contact = Contact(fullname, email, phone)
    db.session.add(contact)
    db.session.commit()

    return redirect('/')


@contacts.route("/update")
def update():
    return "update a contact"


@contacts.route("/delete")
def delete():
    return "delete contact"


@contacts.route("/about")
def about():
    return render_template("about.html")
