from fasthtml.common import (
    Div,
    H1,
    P,
    A,
    Img,
    Span,
    Button,
    Form,
    Input,
    Label,
    Select,
    Option,
    Table,
    Tr,
    Th,
    Td,
)

home_page_template = Div(
    H1("Welcome to FastHTML", cls="text-3xl font-bold text-teal-600 font-serif"),
    P("This is a simple HTML template using FastHTML."),
    A("Learn more", href="https://github.com/anarul/fasthtml"),
    Img(src="https://via.placeholder.com/500x200", alt="placeholder image"),
    Span("This is a span tag"),
    Button(
        "Click me",
        cls="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded my-3 ml-2",
    ),
    Form(
        Input(type="text", name="name", placeholder="Enter your name"),
        Label("Email"),
        Input(type="email", name="email", placeholder="Enter your email"),
        Label("Message"),
        Select(
            name="options",
            options=[Option("Option 1"), Option("Option 2"), Option("Option 3")],
        ),
        Button("Submit"),
        Table(
            Tr(Th("Header 1"), Th("Header 2"), Th("Header 3")),
            Tr(Td("Data 1"), Td("Data 2"), Td("Data 3")),
            Tr(Td("Data 4"), Td("Data 5"), Td("Data 6")),
        ),
    ),
    cls="container mx-auto",
)
