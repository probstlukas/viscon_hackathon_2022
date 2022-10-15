# Anything that's not related to authentication that the user can go to, will go here (login page, home page, etc.)
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Event
from . import db
import json
from datetime import datetime, timedelta
from sqlalchemy import desc

views = Blueprint('views', __name__)

# Whenever we go on URL and type in /, this will show
@views.route('/', methods=['GET', 'POST'])
def home():
    if current_user.is_authenticated:
        return render_template("home.html", user=current_user, events=Event.query.filter_by(user_id=current_user.id, visibility=True).filter(Event.date<Event.endDate).order_by(Event.date).all())
    else:
        return render_template("home.html", user=current_user, events=Event.query.filter_by(visibility=True).filter(Event.date<Event.endDate).order_by(Event.date).all())

@views.route('/add-event', methods=['GET', 'POST'])
@login_required
def add_event():
    if request.method == 'POST':
        eventLocation = request.form.get('eventLocation')
        eventName = request.form.get('eventName')
        eventFoods = request.form.get('eventFoods')

        '''if len(note) < 1:
            flash('Note is too short!', category='error')
        else:'''
        new_event = Event(name=eventName, location=eventLocation, foods=eventFoods, user_id=current_user.id)
        db.session.add(new_event)
        db.session.commit()
        flash('Event added!', category='success')

    return render_template("add_event.html", user=current_user)

@views.route('/delete-event', methods=['POST'])
def delete_note():
    event = json.loads(request.data)
    eventId = event['eventId']
    event = Event.query.get(eventId)
    if event:
        if event.user_id == current_user.id:
            event.visibility = False
            db.session.commit()

    return jsonify({})