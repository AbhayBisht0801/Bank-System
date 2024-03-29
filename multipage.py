import streamlit as st
from PIL import Image

from streamlit_option_menu import option_menu

import loginpage,chatbot,homee
def reset_pages():
    st.experimental_rerun()

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        with st.sidebar:        
            app = option_menu(
                menu_title='Menu ',
                options=['Home','Login','chatbot'],
                icons=['Home','login','chatbot'],
                menu_icon='menu-button',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )
        
        if app=='Home':
            homee.app()
        if app == "Login":
            loginpage.app()
        if app == "chatbot":
            chatbot.app() 
              
    
    run()
        