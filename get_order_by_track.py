import sender


# Тест 1. Получение заказа по треку.
def test_get_order_by_track_success_response():
    post_order_response = sender.post_order()
    track = post_order_response.json()["track"]
    get_order_by_track_response = sender.get_order_by_track(track)
    assert get_order_by_track_response.status_code == 200
