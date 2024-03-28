import streamlit as st
import random
import requests
import json


st.title('APIテスト画面 (ユーザー)')

with st.form(key='user'):
  user_id: int = random.randint(0, 10)
  username: str = st.text_input('ユーザー名', max_chars=12)
  data = {
    
  }