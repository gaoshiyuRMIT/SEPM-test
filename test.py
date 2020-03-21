from app.models import Diary, OrderItem, Order
from app import db

if __name__ == '__main__':
    d = Diary(color="yellow")
    o = Order()
    oi = OrderItem(diary=d, quantity=12, order=o)
    db.session.add(oi)
    db.session.commit()

    print("diaries: ")
    for d in Diary.query.all():
        print(d.id, d.color)
    o1 = Order.query.get(o.id)
    print("order: {}".format(o1.id))
    print("order items:")
    for oi1 in o1.items:
        print(oi1.id, oi1.diary.id, oi1.diary.color, oi1.quantity)
