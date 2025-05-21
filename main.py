import streamlit as st

# 페이지 정의
home = st.Page("home.py", title="홈", icon="🏠", default=True)
chatbot = st.Page("chatbot.py", title="챗봇", icon="🤖")
# About
diet = st.Page("about/diet.py", title="식습관", icon="🥗")
prevention = st.Page("about/prevention.py", title="예방", icon="🛡️")
symptoms = st.Page("about/symptoms.py", title="증상", icon="🤒")
treatment = st.Page("about/treatment.py", title="치료", icon="💉")
# Reports
personal_info = st.Page("reports/personal_info.py", title="개인정보", icon="🧍")
glucose = st.Page("reports/glucose.py", title="혈당관리", icon="🩸")
medication = st.Page("reports/medication.py", title="복용약", icon="💊")
final_report = st.Page("reports/final_report.py", title="리포트", icon="📄")

# 네비게이션 실행
pg = st.navigation({
    "🏠 Home": [home],
    "🤖 Chatbot": [chatbot],
    "📘 당뇨정보": [diet, prevention, symptoms, treatment],
    "📋 리포트": [personal_info, glucose, medication, final_report]  
})

pg.run()
