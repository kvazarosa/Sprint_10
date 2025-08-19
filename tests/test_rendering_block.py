from data import Messages
from pages.rendering_block_page import RenderingBlockPage


def test_route_block_with_different_addresses(driver, default_route):
    page = RenderingBlockPage(driver)
    assert page.is_route_block_displayed(), "Блок с маршрутом не отображается"


def test_same_address_shows_zero_minutes(driver):
    page = RenderingBlockPage(driver)
    page.set_same_address()
    assert page.is_text_present(Messages.SAME_ADDRESS_ROUTE), (
        f"Текст '{Messages.SAME_ADDRESS_ROUTE}' не найден на странице"
    )
