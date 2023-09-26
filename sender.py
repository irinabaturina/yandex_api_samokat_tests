import requests

import configuration
import data


def post_order():
    return requests.post(configuration.URL_SERVICE + configuration.ORDERS_PATH,
                         json=data.order_post_body,
                         headers=data.headers)


def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_TRACK_PATH,
                        params={"t": track},
                        headers=data.headers)
