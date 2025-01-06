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
st.header("Dialogs")

st.write(
    "To style a specific container, assign a value to the `key` argument to create a CSS class. Using the `:has` pseudo selector in combination with containers, dialogs can be diferentiated from each other.  "
)

st.subheader("Try it!")
code, preview = st.columns(2, border=True, vertical_alignment="top")


with code:
    dialog_css = dedent(
        """
/*USES THE HAS SELECTOR TO FILTER BY THE NESTED CONTAINER*/

div[role="dialog"]:has(.st-key-large){
    width:85%;
}

div[role="dialog"]:has(.st-key-medium){
    width:65%;
}
           """
    )
    styles = st_monaco(
        value=dialog_css.strip(),
        height="400px",
        language="css",
        lineNumbers=True,
        minimap=False,
    )

st.html(base_style.substitute(css=styles))
with preview:
    with st.echo("below"):

        @st.dialog("Large Dialog")
        def big_dialog():
            with st.container(key="large"):
                st.write("This now uses 85% of the screen")

        @st.dialog("Medium")
        def medium_dialog():
            with st.container(key="medium"):
                st.write("This now uses 65% of the screen")

        if st.button("Open Large"):
            big_dialog()
        if st.button("Open Medium"):
            medium_dialog()
