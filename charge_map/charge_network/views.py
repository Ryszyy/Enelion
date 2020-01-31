from flask import request
from flask_restful import Resource
from charge_map.charge_network.models import ChargeNetworkModel, ChargePointModel
from charge_map.charge_network.serializers import ChargeNetworkSchema, ChargePointSchema


def template(code, data):
    return {'status_code': code, 'message': data}


ITEM_NOT_FOUND = template(404, "Item not found")
DB_WRITE_SUCCESSFUL = template(200, "Write to db successful")
DB_WRITE_FAILED = template(300, "Write to db was not successful")


class ChargePointResource(Resource):
    def get(self, id=None):
        schema = ChargePointSchema()
        if id is not None:
            point = ChargePointModel.query.get(id)
            if point is None:
                return ITEM_NOT_FOUND
            else:
                return schema.dump(point)
        else:
            points = ChargePointModel.query.all()
            return [schema.dump(x) for x in points]

    def post(self):
        requested_data = request.get_json()
        network_id = requested_data["charge_network_id"]
        network = ChargeNetworkModel.query.get(network_id)
        if network is None:
            return ITEM_NOT_FOUND
        # try:
        point = ChargePointModel(**requested_data)
        print(network.add_charge_point(point))

        charge_points_list = network.charge_points

        print(charge_points_list)

        network.update(charge_points=network)
        point.save()

        return DB_WRITE_SUCCESSFUL
        # except TypeError:
        #     return DB_WRITE_FAILED

    def put(self, id=None):
        requested_data = request.get_json()
        try:
            point = ChargePointModel.query.get(id)
            if point is None:
                return ITEM_NOT_FOUND
            point.update(**requested_data)
            return DB_WRITE_SUCCESSFUL
        except TypeError:
            return DB_WRITE_FAILED

    def delete(self, id=None):
        point = ChargePointModel.query.get(id)
        if point is None:
            return ITEM_NOT_FOUND
        point.delete()
        return DB_WRITE_SUCCESSFUL


class ChargeNetworkResource(Resource):
    def get(self, id=None):
        schema = ChargeNetworkSchema()
        if id is not None:
            network = ChargeNetworkModel.query.get(id)
            if network is None:
                return ITEM_NOT_FOUND
            else:
                return schema.dump(network)
        else:
            points = ChargeNetworkModel.query.all()
            return [schema.dump(x) for x in points]

    def post(self):
        requested_data = request.get_json()
        try:
            network = ChargeNetworkModel(**requested_data)
            network.save()
            return DB_WRITE_SUCCESSFUL
        except TypeError:
            return DB_WRITE_FAILED

    def put(self, id=None):
        requested_data = request.get_json()
        try:
            network = ChargeNetworkModel.query.get(id)
            if network is None:
                return ITEM_NOT_FOUND
            network.update(**requested_data)
            return DB_WRITE_SUCCESSFUL
        except TypeError:
            return DB_WRITE_FAILED

    def delete(self, id=None):
        point = ChargeNetworkModel.query.get(id)
        if point is None:
            return ITEM_NOT_FOUND
        point.delete()
        return DB_WRITE_SUCCESSFUL
