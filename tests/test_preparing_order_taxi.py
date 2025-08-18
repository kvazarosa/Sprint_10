from pages.preparing_order_taxi_page import PreparingOrderTaxiPage
import pytest


class TestPreparingOrderTaxi:
    @pytest.mark.usefixtures("default_route")
    def test_switch_to_optimal_mode_updates_prices(self, driver):
        page = PreparingOrderTaxiPage(driver)

        # 1. Кликаем на оптимальный режим
        page.switch_to_optimal_mode()

        # 2. Проверяем активное состояние
        assert page.is_optimal_mode_active(), (
            "Оптимальный режим должен стать активным после клика"
        )

        # 3. Проверяем отображение цены
        assert page.is_price_visible(), (
            "Цена авто должна отображаться после переключения"
        )

    @pytest.mark.usefixtures("default_route")
    def test_switch_to_custom_mode_changes_active_tab(self, driver):
        page = PreparingOrderTaxiPage(driver)

        # 1. Кликаем на свой режим
        page.switch_to_custom_mode()

        # 2. Проверяем активное состояние
        assert page.is_custom_mode_active(), (
            "Режим 'Свой' должен стать активным после клика"
        )

    @pytest.mark.usefixtures("default_route")
    def test_fast_mode_has_call_taxi_button(self, driver):
        page = PreparingOrderTaxiPage(driver)

        assert page.is_call_taxi_button_visible(), (
            "При активном быстром режиме должна отображаться кнопка 'Вызвать такси'"
        )

    @pytest.mark.usefixtures("default_route")
    def test_custom_mode_with_drive_has_book_button(self, driver):
        page = PreparingOrderTaxiPage(driver)

        # 1. Переключаемся на режим "Свой"
        page.switch_to_custom_mode()
        assert page.is_custom_mode_active(), "Режим 'Свой' должен быть активен"

        # 2. Выбираем тип "Драйв"
        page.select_drive_type()

        # 3. Проверяем наличие кнопки "Забронировать"
        assert page.is_book_button_visible(), (
            "При выборе 'Свой' режима и 'Драйв' типа должна отображаться кнопка 'Забронировать'"
        )