import streamlit as st



def start_screen():
    st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>야구 직관 팬 성향 분석</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image("https://storage2.ilyo.co.kr/contents/article/images/2024/0322/1711090517318430.jpg", use_column_width=True)
        
        st.write("") # Gap
        
        if st.button("테스트 시작", key="btn-start", use_container_width=True):
            st.session_state.inspection_start = True
            st.rerun()
