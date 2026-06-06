# import streamlit as st

# from src.screens.home_screen import home_screen
# from src.screens.student_screen import student_screen
# from src.screens.teacher_screen import teacher_screen

# from src.components.dialog_auto_enroll import auto_enroll_dialog

# def main():
  
#   if 'login_type' not in st.session_state:
#     st.session_state['login_type']=None

#   match st.session_state['login_type']:
#     case 'teacher':
#       teacher_screen()
    
#     case 'student':
#       student_screen()
    
#     case None:
#       home_screen()
    

#   join_code =  st.query_params.get('join_code')  
#   if join_code:
#     if st.session_state.login_type != 'student':
#       st.session_state.login_type = 'student'
#       st.rerun()
#     if st.session_state.get('is_logged_in') and st.session_state.get('user_role')=='student':
#       auto_enroll_dialog(join_code)
# main()









import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog


def main():

    st.set_page_config(
        page_title='SnapClass - Making Attendance faster using AI',
        page_icon='snap27.jpeg'
    )

    # FIRST READ QUERY PARAM
    join_code = st.query_params.get("join_code")

    # IF LINK OPENED -> FORCE STUDENT SCREEN IMMEDIATELY
    if join_code:
        st.session_state["login_type"] = "student"
        st.session_state["join_code"] = join_code

    # DEFAULT STATE
    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None

    # RENDER SCREEN
    if st.session_state["login_type"] == "teacher":
        teacher_screen()

    elif st.session_state["login_type"] == "student":
        student_screen()

    else:
        home_screen()

    # AUTO ENROLL AFTER LOGIN
    saved_join_code = st.session_state.get("join_code")

    if (
        saved_join_code
        and st.session_state.get("is_logged_in")
        and st.session_state.get("user_role") == "student"
    ):
        auto_enroll_dialog(saved_join_code)


main()