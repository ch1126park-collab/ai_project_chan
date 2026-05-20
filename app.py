import streamlit as st


st.set_page_config(
    page_title="AI 협업 개발 실습",
    page_icon="🤝",
    layout="centered",
)


st.title("AI 협업 개발 실습용 첫 번째 Streamlit 앱")
st.caption("Python과 Streamlit으로 빠르게 웹앱을 만들고 AI와 협업하는 흐름을 연습합니다.")

st.header("1. 실습 목표")
st.write(
    """
    이 앱은 첫 번째 Streamlit 실행을 확인하기 위한 간단한 예제입니다.
    아래 입력값을 바꿔 보면서 코드 수정, 실행, 결과 확인의 기본 사이클을 연습하세요.
    """
)

name = st.text_input("이름을 입력하세요", value="AI 개발자")
role = st.selectbox(
    "오늘 연습할 역할을 선택하세요",
    ["기획자", "개발자", "리뷰어", "테스터"],
)
confidence = st.slider("Streamlit 자신감", min_value=0, max_value=100, value=50)

st.header("2. 결과")
st.success(f"{name}님은 오늘 '{role}' 역할로 실습합니다.")
st.progress(confidence)

if confidence < 40:
    st.info("천천히 입력값을 바꿔 보며 Streamlit의 동작을 확인해 보세요.")
elif confidence < 80:
    st.info("좋습니다. 이제 위젯을 추가하거나 문구를 바꿔 보세요.")
else:
    st.info("충분히 익숙합니다. 다음 단계로 기능을 하나 더 추가해 보세요.")

st.header("3. AI에게 요청해 볼 과제")
st.code(
    """
이 Streamlit 앱에 체크박스 하나를 추가하고,
체크되면 오늘의 실습 체크리스트를 보여줘.
""".strip(),
    language="text",
)
