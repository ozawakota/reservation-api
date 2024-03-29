import streamlit as st
import datetime
import requests
import json
import pandas as pd

page = st.sidebar.selectbox('Choose your page', ['users', 'rooms', 'bookings'])

URL_LOCALHOST = 'http://127.0.0.1:8000'

if page == 'users':
  st.title('ユーザー登録画面')

  with st.form(key='user'):
    # user_id: int = random.randint(0, 10)
    username: str = st.text_input('ユーザー名', max_chars=12)
    data = {
      # 'user_id': user_id,
      'username': username,
    }
    submit_button = st.form_submit_button(label='ユーザー登録')

  if submit_button:
    st.write('## レスポンス結果')
    url = URL_LOCALHOST + '/users'
    res = requests.post(
      url,
      data=json.dumps(data)
    )
    if res.status_code == 200:
      st.success('ユーザー登録が完了')
    st.write(res.status_code)
    st.json(res.json())

elif page == 'rooms':
  st.title('会議室登録画面')

  with st.form(key='room'):
    # room_id: int = random.randint(0, 10)
    room_name: str = st.text_input('会議室名', max_chars=12)
    capacity: int = st.number_input('定員', step=1)
    data = {
      # 'room_id': room_id,
      'room_name': room_name,
      'capacity' : capacity
    }
    submit_button = st.form_submit_button(label='会議室登録')

  if submit_button:
    url = URL_LOCALHOST + '/rooms'
    res = requests.post(
      url,
      data=json.dumps(data)
    )
    if res.status_code == 200:
      st.success('会議室登録完了')
    st.write(res.status_code)
    st.json(res.json())

elif page == 'bookings':
  st.title('会議室予約画面')
  # ユーザー一覧
  url_users = URL_LOCALHOST + '/users'
  res = requests.get(url_users)
  users = res.json()
  # ユーザー名をキーにして、ユーザーIDをバリュー
  users_dict = {}
  for user in users:
    users_dict[user['username']] = user['user_id']

  # st.write(users_dict)

  # 会議室一覧の取得
  url_rooms = URL_LOCALHOST + '/rooms'
  res = requests.get(url_rooms)
  rooms = res.json()
  rooms_dict = {}
  for room in rooms:
    rooms_dict[room['room_name']] = {
      'room_id' : room['room_id'],
      'capacity' : room['capacity']
    }

  st.write('### 会議室一覧')
  df_rooms = pd.DataFrame(rooms)
  df_rooms.columns = ['会議室', '定員', '会議室ID']
  st.table(df_rooms)

  with st.form(key='booking'):
    username: str = st.selectbox('予約者名', users_dict.keys())
    room_name: str = st.selectbox('会議室名', rooms_dict.keys())
    booked_num: int = st.number_input('予約人数', step=1, min_value=1)
    date = st.date_input('日付: ', min_value=datetime.date.today())
    start_time = st.time_input('開始時刻: ', value=datetime.time(hour=9, minute=0))
    end_time = st.time_input('終了時刻: ', value=datetime.time(hour=20, minute=0))
    submit_button = st.form_submit_button(label='予約登録')

  if submit_button:
    user_id: int = users_dict[username]
    room_id: int = rooms_dict[room_name]['room_id']
    capacity: int = rooms_dict[room_name]['capacity']

    data = {
      'user_id': user_id,
      'room_id': room_id,
      'booked_num': booked_num,
      'start_datetime': datetime.datetime(
        year=date.year,
        month=date.month,
        day=date.day,
        hour=start_time.hour,
        minute=start_time.minute
      ).isoformat(),
      'end_datetime': datetime.datetime(
        year=date.year,
        month=date.month,
        day=date.day,
        hour=end_time.hour,
        minute=end_time.minute
      ).isoformat(),
    }
    # 定員以下の予約人数の場合
    if booked_num <= capacity:
      # 会議室の予約を行う
      url = URL_LOCALHOST + '/bookings'
      res = requests.post(
        url,
        data=json.dumps(data)
      )
      if res.status_code == 200:
        st.success('予約完了しました')
      st.json(res.json())

    else:
      st.error(f'{room_name}の定員は、{capacity}名です。{capacity}名以下の予約人数のみ受け付けております。')