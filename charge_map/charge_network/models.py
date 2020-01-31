from charge_map.extentions import db


class ChargeNetworkModel(db.Model):
    __tablename__ = 'chargenetworkmodel'

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.FLOAT, nullable=False)
    longitude = db.Column(db.FLOAT, nullable=False)
    charge_points = db.relationship("ChargePointModel", backref=db.backref(__tablename__), lazy='dynamic')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    price_per_1kWh = db.Column(db.FLOAT, nullable=False)
    owner = db.Column(db.String, nullable=False)
    avg_charge_power = db.Column(db.FLOAT, nullable=False)

    def __init__(self, latitude, longitude, price, owner, avg_power, **kwargs):
        db.Model.__init__(self, latitude=latitude, longitude=longitude, price_per_1kWh=price, owner=owner,
                          avg_charge_power=avg_power, **kwargs)
        # self.latitude = latitude
        # self.longitude = longitude
        # self.charge_points = []
        # self.price_per_1kWh = price
        # self.owner = owner
        # self.avg_charge_power = avg_power

    def __repr__(self):
        return f"{self.__tablename__}"

    def add_charge_point(self, point):
        if point not in self.charge_points:
            self.charge_points.append(point)
            return True
        return False


class ChargePointModel(db.Model):
    __tablename__ = 'chargepointmodel'

    id = db.Column(db.Integer, primary_key=True)
    offer_charge_power = db.Column(db.Float, nullable=False)
    charge_network_id = db.Column(db.ForeignKey("chargenetworkmodel.id"), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, offer_charge_power, charge_network_id):
        self.offer_charge_power = offer_charge_power
        self.charge_network_id = charge_network_id

    def __repr__(self):
        return f'{self.__tablename__}'
