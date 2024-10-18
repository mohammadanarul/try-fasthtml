from fasthtml.common import fast_app, serve
from templates.base import base_template
from templates.home_page import home_page_template

app, rt = fast_app()


@rt("/")
def root_page():
    return base_template(home_page_template)


@rt("/home")
def home_page():
    return base_template(home_page_template)


if __name__ == "__main__":
    serve()
