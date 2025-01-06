import streamlit as st
from string import Template
from textwrap import dedent
from streamlit.components.v1 import html
from streamlit_monaco import st_monaco

base_style = Template(
    dedent(
        """
        <style>
            $css
        </style>"""
    )
)
st.header("Buttons")

st.write(
    "You can isolate and style buttons by adding styles to the generated CSS class in the DOM named after the `key` argument in you widget. These styles apply with some minor differences to `st.button`, `st.form_submit_button` and `st.popover`. The basic structure of a button will also depend on the precense of an icon argument"
)

st.subheader("Try it!")
code, preview = st.columns(2, border=True, vertical_alignment="top")


with code:
    button_css = dedent(
        """

.st-key-styled_button button{
        border-radius:25px;
        box-shadow: 3px 5px 10px 0px rgba(128, 128, 128, 0.245);
        border-color:white;
    }
.st-key-styled_button:hover button{
        border-color:white;
    }
.st-key-styled_button :focus:not(:active) {
        border-color:white;
    }
.st-key-styled_button p{
        color:grey;
        font-weight: bold;
    }
.st-key-styled_button :active p {
        color:white;
        font-weight: bold;
    }
.st-key-styled_button span[data-testid="stIconMaterial"]{
        color:orange;
    }
.st-key-styled_button :active span[data-testid="stIconMaterial"]{
         color:white;
    }
           """
    )
    styles = st_monaco(
        value=button_css,
        height="400px",
        language="css",
        lineNumbers=True,
        minimap=False,
    )

with preview:

    with st.expander("Button widget structure"):
        st.html("html_diagrams/buttons_tree.html")
    if st.toggle("Preview Style Changes", value=True):
        st.html(base_style.substitute(css=styles))
    with st.echo("below"):
        st.button(
            "Sample Button",
            key="styled_button",
            icon=":material/home:",
        )
