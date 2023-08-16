import streamlit as st 
import webbrowser
import sqlite3
#import segment.analytics as analytics

st.set_page_config(page_title="Sortly GA4+Segment Tester", page_icon="🚀" )     
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("Image-of-your-choice");
background-size: 100%;
display: flex;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
analytics.write_key = 'YOUR_WRITE_KEY'
st.markdown(page_bg_img, unsafe_allow_html=True)

conn = sqlite3.connect("pwd.db")
c = conn.cursor()
c.execute("""CREATE TABLE if not exists pwd_mgr (app_name varchar(20) not null,
                        user_name varchar(50) not null,
                        pass_word varchar(50) not null,
                        email_address varchar(100) not null,
                        url varchar(255) not null,
                    primary key(app_name)       
                    );""")


def insert_data(u):
    with conn:
        c.execute("insert into pwd_mgr values (:app, :user, :pass, :email, :url)", {'app': u.app, 'user': u.username, 'pass': u.password, 'email': u.email, 'url': u.url})
        
def get_cred_by_app(app):
    with conn:
        c.execute("select app_name, user_name, pass_word, email_address,url FROM pwd_mgr where app_name = :name;", {'name': app})
        return c.fetchone()
    
def remove_app_cred(app):
    with conn:
        c.execute("DELETE from pwd_mgr WHERE app_name = :name", {'name': app})
        
def update_password(app,new_pass_word):
    with conn:
        c.execute("update pwd_mgr set pass_word = :pass where app_name = :name", {'name': app, 'pass': new_pass_word})


st.title("Marketing Site 🔐")
st.markdown('#')

c.execute("select count(*) from pwd_mgr")
db_size = c.fetchone()[0] 

c.execute("select app_name from pwd_mgr")
app_names = c.fetchall()
app_names = [i[0] for i in app_names]

radio_option = st.sidebar.radio("Menu", options=["Marketing Home","Marketing Price Page"])

if radio_option=="Marketing Home":    
    #home_radio_btn.home_radio_selected()
    if st.button('Send Event ⚡️', use_container_width=True):


        st.write('Nice :)')