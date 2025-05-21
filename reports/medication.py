import streamlit as st
import datetime
from utils import load_patient_info, load_medications, save_medications
import plotly.express as px
import pandas as pd

# -------------------
# 페이지 설정
# -------------------
st.set_page_config(page_title="복용중인 약 & 갤러드", page_icon="💊")
st.title("💊 복용중인 약 & 갤러드")

# -------------------
# 사용자 선택
# -------------------
all_users = load_patient_info()
if not all_users:
    st.warning("먼저 개인정보를 입력해 주세요.")
    st.stop()

user_labels = [f"{u['name']} / {u['age']}세 / {u['gender']}" for u in all_users]
selected_label = st.selectbox("👤 사용자 선택", user_labels)
user = next(u for u in all_users if f"{u['name']} / {u['age']}세 / {u['gender']}" == selected_label)
user_id = f"{user['name']}_{user['age']}_{user['gender']}"
st.success(f"🔍 현재 선택된 사용자: {user['name']}")

# -------------------
# 기존 약 데이터 불러오기
# -------------------
med_list = load_medications(user_id)

# -------------------
# 입력 폼 - 약 정보 추가
# -------------------
st.markdown("### ✏️ 복용약 정보 입력")
diabetes_meds = [
    "메트포르민", "글리메피리드", "글리클라지드", "글리벤클라미드",
    "DPP-4 억제제", "SGLT-2 억제제", "GLP-1 유사체", "인슐린", "기타"
]

with st.form("med_input_form"):
    selected_meds = st.multiselect("약 이름(중복 선택 가능)", diabetes_meds)
    custom_meds = []
    if "기타" in selected_meds:
        other_input = st.text_input("기타 약 입력 (쉼표로 구분)")
        if other_input:
            custom_meds = [name.strip() for name in other_input.split(",") if name.strip()]
    final_meds = [m for m in selected_meds if m != "기타"] + custom_meds

    med_date = st.date_input("복용 날짜", value=datetime.date.today())
    med_time = st.time_input("복용 시간", value=datetime.time(9, 0))
    med_memo = st.text_input("비고")

    if st.form_submit_button("추가") and final_meds:
        for med in final_meds:
            med_list.append({
                "약 이름": med,
                "복용 날짜": med_date.strftime("%Y-%m-%d"),
                "복용 시간": med_time.strftime("%H:%M"),
                "비고": med_memo
            })
        save_medications(user_id, med_list)
        st.success("💾 약 정보가 저장되었습니다.")
        st.rerun()

# -------------------
# 복용중인 약 목록
# -------------------
if med_list:
    st.markdown("### 📋 복용중인 약 목록")
    col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 1])
    with col1: st.markdown("**약 이름**")
    with col2: st.markdown("**복용 날짜**")
    with col3: st.markdown("**복용 시간**")
    with col4: st.markdown("**비고**")
    with col5: st.markdown("**삭제**")

    for i, med in enumerate(med_list):
        col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 1])
        with col1: st.write(med["약 이름"])
        with col2: st.write(med["복용 날짜"])
        with col3: st.write(med["복용 시간"])
        with col4: st.write(med.get("비고", ""))
        with col5:
            if st.button("삭제", key=f"del_{i}"):
                med_list.pop(i)
                save_medications(user_id, med_list)
                st.rerun()
else:
    st.info("복용중인 약 정보를 입력해 주세요.")

# -------------------
# 달력 시각화 (Plotly Timeline)
# -------------------
if med_list:
    st.markdown("### 🗓️ 복용 캘린더")
    df = pd.DataFrame(med_list)
    df["복용 날짜"] = pd.to_datetime(df["복용 날짜"])
    df["복용 시간"] = pd.to_datetime(df["복용 시간"], format="%H:%M").dt.time
    df["start"] = df.apply(lambda row: datetime.datetime.combine(row["복용 날짜"], row["복용 시간"]), axis=1)
    df["end"] = df["start"] + pd.Timedelta(minutes=15)  # 복용 시간 15분 간격

    fig = px.timeline(
        df,
        x_start="start",
        x_end="end",
        y="약 이름",
        color="약 이름",
        title=f"{user['name']}님의 복용 캘린더",
        labels={"약 이름": "약 이름"},
    )
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
