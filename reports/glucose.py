import streamlit as st
import datetime
import os
import json
import matplotlib.pyplot as plt
import pandas as pd

from utils import load_patient_info

st.set_page_config(page_title="혈당관리", page_icon="🩸")
st.title("🩸 혈당 관리")

# 사용자 선택
all_users = load_patient_info()
if not all_users:
    st.warning("먼저 [개인정보] 탭에서 사용자 정보를 입력해 주세요.")
    st.stop()

user_options = [f"{u['name']} / {u['age']}세 / {u['gender']}" for u in all_users]
selected = st.selectbox("👤 사용자 선택", user_options)
user = next((u for u in all_users if f"{u['name']} / {u['age']}세 / {u['gender']}" == selected), None)
user_id = f"{user['name']}_{user['age']}_{user['gender']}"

st.success(f"🔍 현재 선택된 사용자: {user['name']}")

# 파일 경로
path = "data/glucose.json"
os.makedirs("data", exist_ok=True)

# 데이터 불러오기
try:
    with open(path, "r", encoding="utf-8") as f:
        all_data = json.load(f)
except:
    all_data = {}

user_data = all_data.get(user_id, [])

# 입력 폼
with st.form("glucose_form"):
    date = st.date_input("측정일자", value=datetime.date.today())
    time = st.time_input("측정시간", value=datetime.time(9, 0))
    glucose = st.number_input("혈당(mg/dL)", min_value=0, max_value=500, value=100)
    submit = st.form_submit_button("저장")

    if submit:
        new_entry = {
            "date": str(date),
            "time": time.strftime("%H:%M"),
            "glucose": glucose
        }

        # ✅ 중복 제거 (같은 날짜+시간)
        user_data = [d for d in user_data if not (d["date"] == new_entry["date"] and d["time"] == new_entry["time"])]
        user_data.append(new_entry)
        user_data.sort(key=lambda x: x["date"] + x["time"])

        all_data[user_id] = user_data
        with open(path, "w", encoding="utf-8") as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        st.success("✅ 혈당 정보가 저장되었습니다.")
        st.rerun()

# 시각화
if user_data:
    st.markdown("### 📈 혈당 변화 추이")

    df = pd.DataFrame(user_data)
    df["datetime"] = pd.to_datetime(df["date"] + " " + df["time"])
    df = df.sort_values("datetime")

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df["datetime"], df["glucose"], marker="o", linestyle="-", color="darkred")
    ax.set_title("📊 혈당 변화 그래프")
    ax.set_xlabel("측정 시간")
    ax.set_ylabel("혈당 (mg/dL)")
    ax.grid(True)
    plt.xticks(rotation=45)

    st.pyplot(fig)
else:
    st.info("아직 혈당 기록이 없습니다. 데이터를 입력해 주세요.")
