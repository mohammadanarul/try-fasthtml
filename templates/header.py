from fasthtml.common import Script, Meta, Title

headers = (
    Meta(charset="UTF-8"),
    Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    Meta(
        name="description",
        content="Fast HTML is a Python library for building HTML pages with ease.",
    ),
    Meta(name="author", content="Anarul"),
    Meta(name="keywords", content="HTML, Python, Library, Fast HTML"),
    Meta(name="theme-color", content="#0077B6"),
    Title("Try to FastHTML"),
    Script(src="https://cdn.tailwindcss.com"),
)
