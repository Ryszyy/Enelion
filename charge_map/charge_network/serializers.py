from marshmallow import Schema, fields


class ChargePointSchema(Schema):
    id = fields.Integer()
    offer_charge_power = fields.Float()
    charge_network_id = fields.Integer()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class ChargeNetworkSchema(Schema):
    id = fields.Integer()
    latitude = fields.Float()
    longitude = fields.Float()
    charge_points = fields.Nested(ChargePointSchema)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    price_per_1kWh = fields.Float()
    owner = fields.Str()
    avg_charge_power = fields.Float()
