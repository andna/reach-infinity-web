from fasthtml.common import *

# Inline CSS for basic styling
css_code = """
body {
  margin: 0;
  font-family: Arial, sans-serif;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  color: #fff;
  padding: 1rem;
}
.site-title {
  margin: 0;
}
.hamburger {
  font-size: 1.5rem;
  cursor: pointer;
}
.drawer {
  display: none;
  background-color: #444;
  color: #fff;
  padding: 1rem;
}
.drawer.active {
  display: block;
}
.drawer ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.drawer ul li {
  margin: 0.5rem 0;
}
.drawer ul li a {
  color: #fff;
  text-decoration: none;
}
.main {
  padding: 1rem;
}
"""

# Inline JavaScript for toggling the drawer menu
script_code = """
document.addEventListener("DOMContentLoaded", function() {
  var toggle = document.getElementById("drawer-toggle");
  var drawer = document.getElementById("drawer");
  toggle.addEventListener("click", function() {
    drawer.classList.toggle("active");
  });
});
"""

# Add the inline style and script as header elements
assets = (
    Style(css_code),
    Script(script_code)
)

app, rt = fast_app(
    pico=False,
    hdrs=assets,
    live=True
)

@rt("/")
def home():
    return Div(
        # Header section with site title and hamburger button
        Div(
            H1("Landing Page", cls="site-title"),
            Div("☰", id="drawer-toggle", cls="hamburger"),
            cls="header"
        ),
        # Drawer menu
        Div(
            Ul(
                Li(A("Home", href="/")),
                Li(A("About", href="/about")),
                Li(A("Contact", href="/contact"))
            ),
            id="drawer",
            cls="drawer"
        ),
        # Main content
        Div(
            H2("Welcome to Our Website!"),
            P("This is a simple landing page built with FastHTML."),
            cls="main"
        )
    )

serve()
