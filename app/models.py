from app import db

class Diary(db.Model):
    __tablename__ = 'diary'
    id = db.Column(db.Integer, db.Sequence('diary_id_seq'), primary_key=True)
    color = db.Column(db.String(32))

class OrderItem(db.Model):
    __tablename__ = 'orderitem'
    id = db.Column(db.Integer, db.Sequence('orderitem_id_seq'), primary_key=True)
    diary_id = db.Column(db.Integer, db.ForeignKey('diary.id'))
    diary = db.relationship("Diary")
    quantity = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, db.Sequence('order_id_seq'), primary_key=True)
    items = db.relationship('OrderItem', backref='order', lazy='dynamic')