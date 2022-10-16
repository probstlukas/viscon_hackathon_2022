# Anything that's not related to authentication that the user can go to, will go here (login page, home page, etc.)
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, send_file
from flask_login import login_required, current_user

# from main import app
from .models import Events, Images, Foods, Ehfht, Tags
from . import db, app
import json
from os import path

views = Blueprint('views', __name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def generate_home_data(events):
    for event in events:
        row = [event, [], [], [], []]
        # TODO I have a feeling something here does not work correctly
        for link in Ehfht.query.filter_by(eventsId=event.id).all():
            if link.portions == 0:
                continue

            row[1].append(link.interest)
            row[2].append(Foods.query.filter_by(id=link.foodsId).first().name)
            row[3].append(link.portions)
            row[4].append(Tags.query.filter_by(id=link.tagsId).first().name)

        yield row

# Whenever we go on URL and type in /, this will show
@views.route('/all-events', methods=['GET', 'Post'])
@views.route('/', methods=['GET', 'POST'])
def home():
    # if request.method == 'POST':
    #     eventID = request.form.get('eventID')
    #     newLeftOverCount = request.form.get('newLeftOverCount')
    #     interest = request.form.get('interest')
    #     if newLeftOverCount is not None:
    #         db.session.query(current_user).filter_by(id=eventID).update({""})
    #         pass
    #     if interest is not None:
    #         # Increase interest by one
    #         pass
    data = list(generate_home_data(Events.query.filter_by(visibility=True).filter(Events.creationDate < Events.expirationDate).order_by(Events.creationDate).all()))
    print(data)

    return render_template("home.html", base_url=(url_for('views.home')+'img'+'/'), user=current_user, editEvents=False, processed_data=data, images=Images)

@views.route('/user-events', methods=['GET', 'POST'])
@login_required
def user_events():
    data = list(generate_home_data(Events.query.filter_by(user=current_user.id, visibility=True).filter(Events.creationDate<Events.expirationDate).order_by(Events.creationDate).all()))

    return render_template("home.html", user=current_user, editEvents=True, base_url=(url_for('views.home')+'img'+'/'), processed_data=data, images=Images)

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
            new_imageN = Images(suffix=ending)
            db.session.add(new_imageN)
            db.session.commit()

            filename = new_imageN.id
            file.save(path.join(app.instance_path, app.config['UPLOAD_FOLDER'], (str(filename) + '.' + ending)))

            eventLocation = request.form.get('eventLocation')
            eventName = request.form.get('eventName')
            eventFood = [str.strip(s) for s in str.split(request.form.get('eventFood'), ",")]
            eventFoodIds = []
            count = [5,2]
            tags = ['vegan', 'vegetarian']
            tagIds = []
            expirationDate = request.form.get('availableUntil')
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
            new_eventN = Events(name=eventName, location=eventLocation, expirationDate=expirationDate, user=current_user.id, imageId=new_imageN.id)
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
    print(eventId)
    eventN = Events.query.get(eventId);
    if eventN:
        if eventN.user == current_user.id:
            print(eventId)
            eventN.visibility = False
            db.session.commit()
    return jsonify({})

@views.route('/add-interest', methods=['POST'])
def add_interest():
    rdata = json.loads(request.data)
    eventId = rdata['eventId']
    foodName = rdata['foodName']
    print('arrived ad /add-interest')
    #record = Ehfht.query.filter_by(eventsId=eventId).all()
    record2 = Ehfht.query.filter_by(eventsId=eventId).join(Foods, Foods.id == Ehfht.foodsId).add_columns(Foods.name).filter(Foods.name == foodName).first()
    record2[0].interest += 1
    db.session.commit()
    return jsonify({})