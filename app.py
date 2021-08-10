from flask import Flask, jsonify, json, request, url_for, redirect, flash
from flask_crontab import Crontab
from flask_pymongo import PyMongo
from bson import json_util, ObjectId
from werkzeug.utils import secure_filename

from utils import upload_file

app = Flask(__name__, static_folder='uploads')
app.config["MONGO_URI"] = "mongodb://localhost:27017/subscriber_db"
mongodb_client = PyMongo(app)
db = mongodb_client.db

crontab = Crontab(app)


@crontab.job(minute='0', hour='0', day='5')
def schedule_job():
    from notifications import send_reminder_notification
    send_reminder_notification()


@app.route('/user', methods=["POST"])
def user():
    result = db.mongo.user.insert_one(request.json)
    return jsonify(json.loads(json_util.dumps(result.inserted_id)))


# get user
@app.route('/login', methods=['POST'])
def login():
    credentials = request.json
    if not credentials:
        return jsonify(msg='No credentials provided'), 400
    if 'mobile_number' not in credentials or credentials['mobile_number'] is None:
        return jsonify(msg='Invalid mobile number'), 400
    mobile = credentials['mobile_number']
    user = db.subscriber.find_one_or_404({'mobile_number': mobile})
    return jsonify(json.loads(json_util.dumps(user)))


# create subscriber
@app.route('/signup', methods=['POST'])
def signup():
    credentials = request.json
    credentials['subscriptions'] = []
    insert_result = db.subscriber.insert_one(credentials)
    user = db.signup.find_one({'_id': insert_result.inserted_id})
    return jsonify(json.loads(json_util.dumps(user)))


@app.route('/update/user', methods=["PUT"])
def update_user():
    uid = request.json['uid']
    user_id = request.json['user_id']
    status = request.json['status']
    user = {'_id': ObjectId(user_id)}
    token = {'$set': {'uid': uid, 'status': status}}
    # update_user_status = {'$set': {'status': status}}
    db.subscriber.update_one(user, token, upsert=True)
    return '', 200


@app.route("/upload/photo", methods=["POST"])
def save_upload():
    user_id = request.form.get('user_id')
    photo = upload_file(
        path='uploads/subscribers/{}/'.format(user_id),
        file=request.files['file'])
    return photo


#     mongo.save_file(filename, request.files["file"])
#     return redirect(url_for("get_upload", filename=filename))

# end of user

# start subscriptions
@app.route('/subscriptions', methods=["POST"])
def subscription():
    sub_result = db.subscription.insert_one(request.json)
    return jsonify(json.loads(json_util.dumps(sub_result.inserted_id)))


@app.route('/pause/subscription', methods=['POST'])
def pause_subscription():
    user_id = request.json['user_id']
    status = request.json['status']
    user = {'_id': ObjectId(user_id)}
    update_status = db.subscription.update_one(user, status, upsert=True)
    pause_result = db.pauseSubscription.insert_one(request.json)
    return jsonify(json.loads(json_util.dumps(pause_result.inserted_id, update_status)))


@app.route('/cancel/subscription', methods=['POST'])
def cancel_subscription():
    user_id = request.json['user_id']
    status = request.json['status']
    reason = request.json['reason']
    user = {'userId': user_id}
    token = {'$set': {'status': status, 'reason': reason}}
    user_status = {'$set': {'status': status}}
    update_cancel_user = db.subscription.update_one(user, token, upsert=True)
    update_user = db.subscriber.update_one({'_id': ObjectId(user_id)}, user_status, upsert=True)
    cancel_result = db.cancelSubscription.insert_one(request.json)
    return jsonify(status=True, msg="Cancelled Subscription")


@app.route('/animalExpert', methods=["POST"])
def animalExpert():
    animal_result = db.animalExpert.insert_one(request.json)
    return jsonify(json.loads(json_util.dumps(animal_result.inserted_id)))


@app.route('/payment', methods=["POST"])
def payment():
    payment = db.mongo.payment.insert_one(request.json)
    return jsonify(json.loads(json_util.dumps(payment.inserted_id)))


@app.route('/update/payment', methods=["PUT"])
def update_payment():
    print(request.json)
    _id = ObjectId(request.json['_id'])
    update_dict = request.json
    del update_dict['_id']
    # payment_result = db.mongo.payment.insert_one(request.json)
    # notification = db.payment.insert_one(update_dict)
    filter = {'_id': _id}
    payment = {'$set': update_dict}
    db.mongo.payment.update_one(filter, payment, upsert=True)
    return '', 200


@app.route('/support', methods=["POST"])
def support():
    support_result = db.support.insert_one(request.json)
    return '', 200


@app.route('/calendar', methods=["POST"])
def calendar():
    calendar_result = db.calendar.insert_one(request.json)
    return jsonify(json.loads(json_util.dumps(calendar_result.inserted_id)))


@app.route('/user/<user_id>/events')
def events(user_id):
    user_events = db.calendar.find({'user_id': user_id})
    return jsonify(json.loads(json_util.dumps(user_events)))


@app.route('/address', methods=["POST"])
def address():
    address_result = db.address.insert_one(request.json)
    return jsonify(json.loads(json_util.dumps(address_result.inserted_id)))


@app.route('/user/<mobile_number>', methods=["GET"])
def get_user(mobile_number):
    result = db.subscriber.find_one({'mobile_number': mobile_number})
    user_id = str(result["_id"])
    print(user_id)
    address = db.address.find({'user_id': user_id})
    user_events = db.calendar.find({'user_id': user_id})
    sub = db.subscription.find({'user_id': user_id})
    result['_id'] = str(result['_id'])
    result['addresses'] = address
    result['events'] = user_events
    result['subscriptions'] = sub
    return jsonify(json.loads(json_util.dumps(result)))


@app.route('/user/id/<id>', methods=["GET"])
def get_user_by_id(id):
    result = db.subscriber.find_one_or_404({'_id': ObjectId(id)})
    user_id = str(result["_id"])
    address = db.address.find({'user_id': user_id})
    user_events = db.calendar.find({'user_id': user_id})
    sub = db.subscription.find({'user_id': user_id})
    result['_id'] = str(result['_id'])
    result['addresses'] = address
    result['events'] = user_events
    result['subscriptions'] = sub
    return jsonify(json.loads(json_util.dumps(result)))


@app.route('/get/calendar', methods=["GET"])
def get_calendar():
    cal = db.calendar.find_one()
    cal['_id'] = str(cal['_id'])
    return jsonify(cal)


@app.route('/user/paused/subscriptions/<user_id>', methods=["GET"])
def get_pausedSubscriptions(user_id):
    pausedSub = db.subscription.find({'$and': [{'user_id': user_id}, {"status": 2}]})
    # pausedSub['user_id'] = str(pausedSub['user_id'])
    return jsonify(json.loads(json_util.dumps(pausedSub)))


@app.route('/events/calendar_id', methods=["GET"])
def get_events(calendar_id):
    event = db.calendar.find({'_id': calendar_id})
    output = []
    for e in event.find():
        output.append(request.args.get(e))
    return jsonify({'result': output})


@app.route('/get/monthly/events/user_id', methods=["GET"])
def get_montly_events(user_id):
    monthly_events = db.calendar.find({'_id': user_id})
    month_event = []
    for month in monthly_events.find():
        month_event.append(request.args.get(month))
    return jsonify({'result': len(month_event) - 1})


@app.route('/user/<user_id>/subscriptions', methods=["GET"])
def get_subscription(user_id):
    sub = db.subscription.find({'user_id': user_id})
    if sub is None:
        return jsonify(''), 404
    return jsonify(json.loads(json_util.dumps(sub)))


@app.route('/user/<id>/payments', methods=["GET"])
def get_payments(id):
    payment = db.mongo.payment.find({'userId': id, 'status': 0})
    if payment is None:
        return jsonify(''), 404
    return jsonify(json.loads(json_util.dumps(payment)))


@app.route('/get/address/<user_id>', methods=['GET'])
def get_address(user_id):
    add = db.address.find({'user_id': user_id})
    return jsonify(json.loads(json_util.dumps(add)))


@app.route('/update/address/<user_id>', methods=["PUT"])
def update_address(user_id):
    collection = db.address
    filter = {'user_id': user_id}
    new_values = {'$set': request.json}
    collection.update_one(filter, new_values, upsert=True)
    return '', 200


@app.route("/post/invoices", methods=["POST"])
def post_invoices():
    invoice = db.invoices.insert_one(request.json)
    return '', 200


@app.route('/get/invoices/<user_id>', methods=['GET'])
def get_invoices(user_id):
    # user_id = ObjectId(oid=user_id)
    invoices_get = db.invoices.find({'user_id': user_id})
    return jsonify(json.loads(json_util.dumps(invoices_get)))


# Delivery App APIs
@app.get('/delivery/agent/<mobile>')
def get_delivery_agent(mobile):
    delivery_agent = db.delivery_agents.find_one_or_404({'mobile': mobile})
    return jsonify(json.loads(json_util.dumps(delivery_agent))) 

def register_blueprints():
    from notifications import notification_bp
    app.register_blueprint(notification_bp)    


register_blueprints()
if __name__ == '__main__':
    app.run(host='0.0.0.0')
