import pytest
from pages.ordering_taxi_page import OrderingTaxiPage


class TestOrderingTaxi:
    def test_tariffs_displayed_correctly(self, taxi_order_created):
        page = OrderingTaxiPage(taxi_order_created)
        assert page.all_tariffs_count == 6
        assert page.active_tariffs_count == 1

    def test_tariffs_displayed_correctly(self, taxi_order_created):
        page = OrderingTaxiPage(taxi_order_created)
        assert page.all_tariffs_count == 6
        assert page.active_tariffs_count == 1

    @pytest.mark.xfail(reason="Баг в описании тарифа 'Сонный' - описания поменяли местами")
    def test_tariff_tooltips_sleepy(self, taxi_order_created):
        page = OrderingTaxiPage(taxi_order_created)
        assert page.check_tariff_tooltip("Сонный")

    @pytest.mark.xfail(reason="Баг в описании тарифа 'Разговорчивый' - описания поменяли местами")
    def test_tariff_tooltips_talkative(self, taxi_order_created):
        page = OrderingTaxiPage(taxi_order_created)
        assert page.check_tariff_tooltip("Разговорчивый")

    def test_tariff_tooltips(self, taxi_order_created, tariff_name):
        if tariff_name in ["Сонный", "Разговорчивый"]:
            pytest.skip(f"Пропуск проверки для тарифа '{tariff_name}' - известный баг")
        page = OrderingTaxiPage(taxi_order_created)
        assert page.check_tariff_tooltip(tariff_name)
