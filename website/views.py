# Anything that's not related to authentication that the user can go to, will go here (login page, home page, etc.)
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, send_file
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import urllib.request

# from main import app
from .models import Event, Image
from . import db, app
import json
from datetime import datetime, timedelta
from sqlalchemy import desc
from os import path

views = Blueprint('views', __name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


# Whenever we go on URL and type in /, this will show
@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user, editEvents = False, events=Event.query.filter_by(visibility=True)
                           .filter(Event.date < Event.endDate).order_by(Event.date).all())

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@views.route('/add-event', methods=['GET', 'POST'])
@login_required
def add_event():
    if request.method == 'POST':

        # Upload photo of food
        if 'file' not in request.files:
            flash('No file part', category='error')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No image selected for uploading', category='error')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            ending = '.' in file.filename and file.filename.rsplit('.', 1)[1].lower()
            new_image = Image(ending=ending)
            db.session.add(new_image)
            db.session.commit()
            filename = new_image.id  # secure_filename(file.filename)
            # print(app.config['UPLOAD_FOLDER'])
            file.save(path.join(app.instance_path, app.config['UPLOAD_FOLDER'], (str(filename) + '.' + ending)))

            eventLocation = request.form.get('eventLocation')
            eventName = request.form.get('eventName')
            eventFood = request.form.get('eventFood')
            new_event = Event(name=eventName, location=eventLocation, foods=eventFood, user_id=current_user.id,
                              image_id=new_image.id)
            db.session.add(new_event)
            db.session.commit()

            flash('Photo successfully uploaded', category='success')
            return redirect(url_for('views.home'))
        else:
            flash('Allowed image types are: png, jpg, jpeg, gif', category='error')
            return redirect(request.url)
        flash('Event added!', category='success')
    return render_template("add_event.html", user=current_user)


@views.route('/img/<filename>')
def display_image(filename):
    return send_file(path.join(app.instance_path, app.config['UPLOAD_FOLDER'], filename), mimetype='image/gif')


@views.route('/delete-event', methods=['POST'])
def delete_event():
    event = json.loads(request.data)
    eventId = event['eventId']
    event = Event.query.get(eventId)
    if event:
        if event.user_id == current_user.id:
            event.visibility = False
            db.session.commit()

    return jsonify({})


@views.route('/all-events', methods=['GET', 'Post'])
@login_required
def all_events():
    return home()


@views.route('/user-events', methods=['GET', 'POST'])
@login_required
def user_events():
    return render_template("home.html", user=current_user, editEvents = True, events=Event.query.filter_by(user_id=current_user.id, visibility=True).filter(Event.date<Event.endDate).order_by(Event.date).all())
