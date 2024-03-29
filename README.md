# 会議室予約 API 開発

Python でデータベースを扱う

SQLAlchemy

## 参照

## 起動

▼ アプリケーション (front)

```bash
streamlit run app.py # http://192.168.100.6:8501 or http://localhost:8501
```

▼ API(ローカル)

```bash
uvicorn main:app --reload # http://127.0.0.1:8000
```

## DB 設定

---

### テーブル設定

■ users

- user_id : ユーザー ID
- user_name : ユーザー名

■ rooms

- room_id : 会議室 ID
- room_name : 会議室名
- capacity : 定員
  - 各会議室ごとに定員を定める

■ bookings

- booking_id : 予約 ID
- user_id : 予約 ID
  - users テーブルと紐付け
- room_id : 会議室 ID
  - rooms テーブルと紐付け
- reserved_num : 予約人数
  - 6 名まで
- start_data_time : 開始時間
  - 15 分刻み
- end_data_time : 終了時間
  - 15 分刻み

---

### DB 条件

- capacity(定員) 以上の reserved_num(予約人数)は不可
  - capacity >= reserved_num
- 利用時間は 9:00 ~ 20:00

---

### 必要な処理

#### Create

- ユーザー登録
- 会議室作成
- 予約登録

#### Read

- ユーザー情報読み込み
- 会議室情報読み込み
- 予約一覧読み込み

#### Update

なし

#### Delete

なし

## チュートリアル

FastAPI

https://fastapi.tiangolo.com/ja/tutorial/sql-databases/

streamlit

https://docs.streamlit.io/library/api-reference
