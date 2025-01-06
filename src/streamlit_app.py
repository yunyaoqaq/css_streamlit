import streamlit as st

st.set_page_config(layout="wide")

st.logo("https://streamlit.io/images/brand/streamlit-mark-color.png", size="large")

nav_menu = {
    "Main": [
        st.Page(
            title="Welcome",
            page="home/home.py",
            icon=":material/home:",
        )
    ],
    "Widgets": [
        st.Page(
            title="Buttons",
            page="widgets/buttons.py",
            icon=":material/buttons_alt:",
        ),
        st.Page(
            title="Headers",
            page="widgets/headers.py",
            icon=":material/title:",
        ),
    ],
    "Layouts": [
        st.Page(
            title="Containers",
            page="layouts/containers.py",
            icon=":material/tab_group:",
        ),
        st.Page(title="Dialogs", page="layouts/dialogs.py", icon=":material/dialogs:"),
        st.Page(title="Tabs", page="layouts/tabs.py", icon=":material/folder:"),
        st.Page(
            title="Expanders",
            page="layouts/expanders.py",
            icon=":material/open_in_full:",
        ),
    ],
}
nav = st.navigation(nav_menu, position="sidebar")
nav.run()
