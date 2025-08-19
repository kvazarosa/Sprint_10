from locators.drawing_route_locators import DrawingRouteLocators
from .base_page import BasePage


class DrawingRoutePage(BasePage):
    def set_route_points(self, from_address, to_address):
        self.input_address(DrawingRouteLocators.FIELD_FROM, from_address)
        self.input_address(DrawingRouteLocators.FIELD_WHERE, to_address)

    def is_start_point_visible(self):
        return self.is_point_visible(DrawingRouteLocators.KHAMOVNICHESKY)

    def is_end_point_visible(self):
        return self.is_point_visible(DrawingRouteLocators.ZUBOVSKY)