import pytest
import time

BUTTON_TEXT = dict([
    ('ru', 'Добавить в корзину'),
    ('en-gb', 'Add to basket'),
    ('es', 'Añadir al carrito'),
    ('fr', 'Ajouter au panier'),
])

def test_button_add_to_card(browser, language):

    # Проверяем что язык из списка ожидаемых
    if language not in BUTTON_TEXT.keys():
        raise pytest.UsageError(f"parameter --language not in one of: {','.join(BUTTON_TEXT)}")

    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    browser.get(link)

    time.sleep(10)  # больше не стал делать

    button = browser.find_element_by_css_selector('button.btn-add-to-basket')

    assert button.text == BUTTON_TEXT[language], 'No valid text on button: "add to card"'
