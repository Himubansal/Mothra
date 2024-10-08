from flask import render_template, request, Blueprint, redirect, url_for, flash, abort
from flask_login import current_user, login_required
from mothra import db
from mothra.models import User, Submission, Attempts, Answer, Notification, Announcement, Stats
from mothra.forms import SubmissionForm
from mothra.views import classify
from datetime import datetime



challenges = Blueprint('challenges', __name__)

# SUBMISSION HANDLING

def sub(form, attemp):
    att=Attempts.query.filter_by(of=current_user.id, stage= current_user.level+1).first()
    if att:
        if att.atmpts>=attemp:
            flash("You have exhausted your number of attempts at this problem.")
            abort(403)
        else:
            att.atmpts+=1
    else:
        atmpt=Attempts()
        db.session.add(atmpt)
    ans=form.ans.data
    corans=Answer.query.filter_by(stage=current_user.level+1).first()
    if ans!=corans.ans:
        correct=0
        message = "Oops! Your Submission for the "+classify[current_user.level+1] + " upgrade on "+now.strftime("%d %b %Y at %I:%M %p")+" has been auto rejected because your answer was incorrect."
    else:
        correct=1
        message = "Your Submission for the "+classify[current_user.level+1] + " upgrade on "+now.strftime("%d %b %Y at %I:%M %p")+" has been sent for review. Please wait for some time."
    sub=form.sub.data
    submission=Submission(ans=ans, sub=sub, correct=correct)
    notification=Notification(uid=current_user.id, message=message)
    flash(message)
    db.session.add(submission)
    db.session.add(notification)
    db.session.commit()


# MESSAGING

@challenges.route('/notifications')
@login_required
def notifications():
    notifs=Notification.query.filter_by(uid=current_user.id).all()
    notifs.reverse()
    count=Notification.query.filter_by(uid=current_user.id).count()
    current_user.notif_count=count
    db.session.commit()
    return render_template('notifications.html', notifs=notifs)


@challenges.route('/announcements')
@login_required
def announcements():
    ancmts=Announcement.query.all()
    ancmts.reverse()
    return render_template('announcements.html', ancmts=ancmts)




#CHALLENGE ROUTES

@challenges.route('/noob', methods=['GET', 'POST'])
@login_required
def noob():
    if current_user.level>0 and current_user.user_type!="Godzilla":
        stats=Stats.query.filter_by(level=1, uid=current_user.id).first()
        return render_template('challenges/chal_1.html', stats=stats)
    else:
        form=SubmissionForm()
        att=7
        attempts=Attempts.query.filter_by(of=current_user.id, stage=1).first()
        if form.validate_on_submit():
            sub(form, att)
            return redirect(url_for('challenges.noob'))

        return render_template('challenges/chal_1.html', form=form, attempts=attempts, att=att)

@challenges.route('/unknown', methods=['GET', 'POST'])
@login_required
def unknown():
    if current_user.level<1:
        abort(403)
    elif current_user.level>1 and current_user.user_type!="Godzilla":
        stats=Stats.query.filter_by(level=2, uid=current_user.id).first()
        return render_template('challenges/chal_2.html', stats=stats)
    else:
        form=SubmissionForm()
        att=5
        attempts=Attempts.query.filter_by(of=current_user.id, stage=2).first()
        if form.validate_on_submit():
            sub(form, att)
            return redirect(url_for('challenges.unknown'))

        return render_template('challenges/chal_2.html', form=form, attempts=attempts, att=att)

@challenges.route('/amateur', methods=['GET', 'POST'])
@login_required
def amateur():
    if current_user.level<2:
        abort(403)

    elif current_user.level>2 and current_user.user_type!="Godzilla":
        stats=Stats.query.filter_by(level=3, uid=current_user.id).first()
        return render_template('challenges/chal_3.html', stats=stats)
    else:
        form=SubmissionForm()
        att=5
        attempts=Attempts.query.filter_by(of=current_user.id, stage=3).first()
        if form.validate_on_submit():
            sub(form, att)
            return redirect(url_for('challenges.amateur'))

        return render_template('challenges/chal_3.html', form=form, attempts=attempts, att=att)

@challenges.route('/average', methods=['GET', 'POST'])
@login_required
def average():
    if current_user.level<3:
        abort(403)

    elif current_user.level>3 and current_user.user_type!="Godzilla":
        stats=Stats.query.filter_by(level=4, uid=current_user.id).first()
        return render_template('challenges/chal_4.html', stats=stats)
    else:
        form=SubmissionForm()
        att=5
        attempts=Attempts.query.filter_by(of=current_user.id, stage=4).first()
        if form.validate_on_submit():
            sub(form, att)
            return redirect(url_for('challenges.average'))

        return render_template('challenges/chal_4.html', form=form, attempts=attempts, att=att)

@challenges.route('/working', methods=['GET', 'POST'])
@login_required
def working():
    if current_user.level<4:
        abort(403)

    elif current_user.level>4 and current_user.user_type!="Godzilla":
        stats=Stats.query.filter_by(level=5, uid=current_user.id).first()
        return render_template('challenges/chal_5.html', stats=stats)
    else:
        form=SubmissionForm()
        att=5
        attempts=Attempts.query.filter_by(of=current_user.id, stage=5).first()
        if form.validate_on_submit():
            sub(form, att)
            return redirect(url_for('challenges.working'))

        return render_template('challenges/chal_5.html', form=form, attempts=attempts, att=att)

@challenges.route('/famous', methods=['GET', 'POST'])
@login_required
def famous():
    if current_user.level<5:
        abort(403)

    elif current_user.level>5 and current_user.user_type!="Godzilla":
        stats=Stats.query.filter_by(level=6, uid=current_user.id).first()
        return render_template('challenges/chal_6.html', stats=stats)
    else:
        form=SubmissionForm()
        att=3
        attempts=Attempts.query.filter_by(of=current_user.id, stage=6).first()
        if form.validate_on_submit():
            sub(form, att)
            return redirect(url_for('challenges.famous'))

        return render_template('challenges/chal_6.html', form=form, attempts=attempts, att=att)

@challenges.route('/creator', methods=['GET', 'POST'])
@login_required
def creator():
    if current_user.level<6:
        abort(403)

    elif current_user.level>6 and current_user.user_type!="Godzilla":
        stats=Stats.query.filter_by(level=7, uid=current_user.id).first()
        return render_template('challenges/chal_7.html', stats=stats)
    else:
        form=SubmissionForm()
        att=3
        attempts=Attempts.query.filter_by(of=current_user.id, stage=7).first()
        if form.validate_on_submit():
            sub(form, att)
            return redirect(url_for('challenges.creator'))

        return render_template('challenges/chal_7.html', form=form, attempts=attempts, att=att)

@challenges.route('/wip', methods=['GET', 'POST'])
@login_required
def wip():
    return render_template('wip.html')
