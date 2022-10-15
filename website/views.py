# Anything that's not related to authentication that the user can go to, will go here (login page, home page, etc.)
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, send_file
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime, timedelta

# from main import app
from .models import Events, Images, Foods, Ehfht, Tags
from . import db, app#, mysql
import json
from datetime import datetime, timedelta
from sqlalchemy import desc
from os import path

views = Blueprint('views', __name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


# Whenever we go on URL and type in /, this will show
@views.route('/', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        return render_template("home.html", base_url=(url_for('views.home')+'img'+'/'), images=Images, user=current_user, ehfht=Ehfht, foods=Foods, events=Events.query.filter_by(user=current_user.id, visibility=True).filter(Events.creationDate < Events.expirationDate).order_by(Events.creationDate).all())
    else:
        return render_template("home.html", base_url=(url_for('views.home')+'img'+'/'), images=Images, user=current_user, ehfht=Ehfht, foods=Foods, events=Events.query.filter_by(visibility=True).filter(Events.creationDate < Events.expirationDate).order_by(Events.creationDate).all())

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
            ### OLD DATABASE
            #new_image = Image(ending=ending)
            #db.session.add(new_image)
            #db.session.commit()
            ### NEW DATABASE
            new_imageN = Images(suffix=ending)
            db.session.add(new_imageN)
            db.session.commit()

            filename = new_imageN.id  # secure_filename(file.filename)
            # print(app.config['UPLOAD_FOLDER'])
            file.save(path.join(app.instance_path, app.config['UPLOAD_FOLDER'], (str(filename) + '.' + ending)))

            eventLocation = request.form.get('eventLocation')
            eventName = request.form.get('eventName')
            eventFood = ["pasta", "pizza"]#request.form.get('eventFood')
            eventFoodIds = []
            count = [5,2]
            tags = ['vegan', 'vegetarian']
            tagIds = []
            ### OLD DATABASE
            #new_event = Event(name=eventName, location=eventLocation, foods=0, user_id=current_user.id,
            #                  image_id=new_image.id)
            #db.session.add(new_event)
            #db.session.commit()
            ### NEW DATABASE
            for i in eventFood:
                new = Foods(name=i)
                db.session.add(new)
                db.session.commit()
                eventFoodIds.append(new.id)
            for i in tags:
                new = Tags(name=i)
                db.session.add(new)
                db.session.commit()
                tagIds.append(new.id)

            new_eventN = Events(name=eventName, location=eventLocation, user=current_user.id, imageId=new_imageN.id)
            db.session.add(new_eventN)
            db.session.commit()
            eventId = new_eventN.id

            for i in range(len(eventFood)):
                new = Ehfht(eventsId=eventId, tagsId=tagIds[i], foodsId=eventFoodIds[i], portions=count[i], interest=0)
                db.session.add(new)
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

    eventN = Events.query.get(eventId);
    if eventN:
        if eventN.userId == current_user.id:
            eventN.visibility = False
            db.session.commit()

    return jsonify({})

@views.route('/all-events', methods=['GET', 'Post'])
@login_required
def all_events():
    return home()

@views.route('/user-events', methods=['GET', 'POST'])
@login_required
def user_events():
    return render_template("user_events.html", user=current_user, ehfht=Ehfht, foods=Foods, events=Events.query.filter_by(user=current_user.id, visibility=True).filter(Events.creationDate<Events.expirationDate).order_by(Events.creationDate).all())
