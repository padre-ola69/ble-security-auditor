"""
BLE Security Auditor Pro - Flask Backend
Author: PADRÉ OLA
License: MIT
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'ble_auditor.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(17), unique=True, nullable=False)
    name = db.Column(db.String(255))
    rssi = db.Column(db.Integer)
    first_seen = db.Column(db.DateTime, default=datetime.utcnow)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {'id': self.id, 'address': self.address, 'name': self.name, 'rssi': self.rssi}

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({'status': 'running', 'version': '1.0.0-alpha'}), 200

@app.route('/api/devices', methods=['GET'])
def get_devices():
    try:
        devices = Device.query.all()
        return jsonify({'devices': [d.to_dict() for d in devices]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
