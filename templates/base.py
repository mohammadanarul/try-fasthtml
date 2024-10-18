from fasthtml.common import Html
from templates.header import headers


def base_template(html):
    return Html(*headers, html)
