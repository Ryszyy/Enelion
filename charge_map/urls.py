from charge_map.extentions import api
from charge_map.charge_network import views


api.add_resource(views.ChargePointResource,
                 "/charge_point",
                 "/charge_point/<id>",
                 endpoint="charge_point")
api.add_resource(views.ChargeNetworkResource,
                 "/charge_network",
                 "/charge_network/<id>",
                 endpoint="charge_network")
