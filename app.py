import streamlit as st
from multiapp import MultiApp
from apps import attendance, camera  # import your app modules here

app = MultiApp()

st.markdown("""#MultiPageApp
            This multipage app is using the Streamlit functionality
            """)

# Add all your application here
app.add_app("Attendance", attendance.app)
app.add_app("Camera", camera.app)
# The main app
app.run()
