import streamlit as st

st.set_page_config(page_title="증상", page_icon="📌")
st.markdown("<h2>📌 당뇨병 주요 증상</h2>", unsafe_allow_html=True)
st.markdown("<p>아래 항목을 클릭하면 증상별 상세 설명을 볼 수 있어요.</p>", unsafe_allow_html=True)

# 공통 스타일 (박스형 강조 배경)
def symptom_box(title, emoji, content, color):
    st.markdown(f"""
    <div style='background-color: {color}; padding: 15px 20px; border-radius: 12px; margin-bottom: 15px;'>
        <h4 style='margin-bottom:10px;'>{emoji} <strong>{title}</strong></h4>
        <p style='margin: 0;'>{content}</p>
    </div>
    """, unsafe_allow_html=True)

# 증상 항목
with st.expander("🚽 잦은 소변"):
    st.write("""
    혈당 수치가 높으면 신장은 과도한 포도당을 소변으로 배출하려고 하며, 이로 인해 소변량이 증가합니다.  
    특히 밤에 화장실을 자주 가는 경우 주의가 필요합니다.
    """)

with st.expander("🥤 심한 갈증"):
    st.write("""
    소변을 자주 보게 되면 체내 수분이 빠져나가 탈수가 발생하고, 이로 인해 지속적인 갈증을 느끼게 됩니다.  
    물을 자주 마셔도 갈증이 해소되지 않는다면 혈당 이상을 의심할 수 있어요.
    """)

with st.expander("😴 피로감"):
    st.write("""
    세포가 포도당을 제대로 사용하지 못하면 에너지가 부족해져 쉽게 피로해집니다.  
    충분히 쉬었는데도 나른하거나 무기력하다면 당뇨 초기 증상일 수 있어요.
    """)

with st.expander("📉 체중 감소"):
    st.write("""
    인슐린이 부족하거나 작동하지 않으면 몸은 지방과 근육을 에너지로 사용하게 됩니다.  
    식사량이 평소와 비슷한데도 체중이 줄어드는 현상이 있다면 주의가 필요합니다.
    """)

with st.expander("👁️ 흐린 시야"):
    st.write("""
    혈당이 높을 경우 안구 내 수분 균형이 깨져 시력이 일시적으로 흐려질 수 있어요.  
    장기적으로는 당뇨망막병증 등 합병증으로 진행될 위험도 있습니다.
    """)

with st.expander("🩹 상처 회복 지연"):
    st.write("""
    고혈당은 혈관과 면역 기능을 손상시켜 상처 회복을 더디게 만듭니다.  
    작은 상처가 쉽게 낫지 않거나 감염이 반복된다면, 혈당 관리를 점검해야 합니다.
    """)
