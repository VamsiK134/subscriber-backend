import json

from bson import ObjectId, json_util
from flask import Blueprint, request, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate("subscriberapp-1b005-firebase-adminsdk-ytjt8-82d190ad40.json")
firebase_admin.initialize_app(cred)

notification_bp = Blueprint('notification_bp', __name__)


@notification_bp.route('/send/notification/payment/<user_id>', methods=['POST', 'GET'])
def send_notification(user_id):
    registration_token = request.json['token']
    send_delivery_notifications(registration_token)
    message = messaging.Message(
        data={
            'header': request.json['header'],
            'title': request.json['title'],
        },
        topic='global')
    from main import db
    # user_id = request.json(ObjectId(oid=user_id))
    # db.notification.update({user_id})
    something = request.json
    something["user_id"] = user_id
    notifications = db.notification.insert_one(something)
    # return jsonify(json.loads(json.dumps(notification)))
    response = messaging.send(message)

    print('Successfully sent message:', response)


def send_delivery_notifications(registration_token):
    message = messaging.Message(
        data={

            'header': request.json['header'],
            'title': request.json['title'],
        },
        token=registration_token)
    from main import db

    # notification = db.notification.insert_one(request.json)
    # return jsonify(json.loads(json.dumps(notification)))
    response = messaging.send(message)
    # print('Successfully sent message:', response)


@notification_bp.route('/send/notification/delivery', methods=['POST', 'GET'])
def send_delivery_notification():
    registration_token = "bRMz40OpyxT1r0c2rlFQMPZgngo2"

    message = messaging.Message(
        data={
            'header': request.json['header'],
            'title': request.json['title'],
        },
        topic='global')
    from main import db

    notification = db.notification.insert_one(request.json)
    # return jsonify(json.loads(json.dumps(notification)))

    response = messaging.send(message)

    print('Successfully sent message:', response)


@notification_bp.route('/send/notification/invoice', methods=['POST', 'GET'])
def send_invoice_notification():
    registration_token = "bRMz40OpyxT1r0c2rlFQMPZgngo2"

    message = messaging.Message(
        data={
            'header': request.json['header'],
            'title': request.json['title'],
        },
        topic='global')
    from main import db

    notification = db.notification.insert_one(request.json)
    # return jsonify(json.loads(json.dumps(notification)))

    response = messaging.send(message)

    print('Successfully sent message:', response)


@notification_bp.route('/get/notification/delivery/<user_id>', methods=["GET"])
def get_notification(user_id):
    from main import db
    notificat = db.notification.find({'user_id': user_id})
    # notify = []
    # for notifications in notificat.find():
    #     notify.append(request.args.get(notifications))
    return jsonify(json.loads(json_util.dumps(notificat)))


@notification_bp.route('/delete/notification', methods=['PUT'])
def delete_notification():
    from main import db
    id = ObjectId(oid=request.json['id'])
    erase_notification = db.notification.delete_one({'_id': id})
    return '', 200
