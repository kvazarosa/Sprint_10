import pytest
from data import Addresses
from pages.drawing_route_page import DrawingRoutePage


@pytest.mark.parametrize("from_addr,to_addr", [
    (Addresses.KHAMOVNICHESKY_VAL, Addresses.ZUBOVSKY_BULVAR),
    (Addresses.ZUBOVSKY_BULVAR, Addresses.KHAMOVNICHESKY_VAL)
])
def test_route_points_visibility(driver, from_addr, to_addr):
    page = DrawingRoutePage(driver)
    page.set_route_points(from_addr, to_addr)
    assert page.is_start_point_visible()
    assert page.is_end_point_visible()