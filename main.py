import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(
    page_title="지구촌 MBTI 분석",
    page_icon="🌍",
    layout="centered"
)

# 타이틀 및 소개
st.title("🌍 나라별 MBTI 성향 & 비율 분석")
st.write("세계 여러 나라의 문화적 특성과 통계적 MBTI 경향을 살펴보는 공간입니다.")

st.divider()

# 1. 국가별 가상 MBTI 통계 데이터 (pandas 데이터프레임 활용)
st.subheader("📊 주요 국가별 MBTI 최다 비율 순위")
st.caption("※ 일반적인 글로벌 통계 자료를 바탕으로 재구성한 데이터입니다.")

# 데이터 생성
mbti_data = {
    "국가": ["대한민국 (Korea)", "미국 (USA)", "일본 (Japan)", "독일 (Germany)", "브라질 (Brazil)"],
    "가장 많은 MBTI": ["INFP / INFJ", "ESTJ / ESFP", "ISFJ", "ISTJ", "ENFP / ESFP"],
    "문화적 성향 핵심 키워드": ["트렌드 민감, 관계 중심", "개인주의, 실용주의", "조화와 배려, 매너", "원칙주의, 체계적 시스템", "열정, 사교성, 축제"]
}
df = pd.DataFrame(mbti_data)

# 스트림릿 테이블로 보기 좋게 출력
st.table(df)

st.divider()

# 2. 국가 선택 상세 분석 (인터랙체 위젯)
st.subheader("🔍 국가별 깊이 알아보기")
selected_country = st.selectbox(
    "궁금한 국가를 선택하세요:",
    ["대한민국", "미국", "일본", "독일"]
)

# 선택된 국가에 따른 동적 콘텐츠 출력
if selected_country == "대한민국":
    st.markdown("### 🇰🇷 대한민국")
    st.write("**특징:** 전 세계에서 MBTI에 대한 관심도가 가장 높은 나라 중 하나입니다.")
    st.info("최근 통계에 따르면 전통적인 유교 문화의 영향으로 내향적 배려(I)와 계획성(J)이 높게 나타나기도 하지만, 젊은 층을 중심으로 개성 넘치는 N(직관형) 성향의 비율도 급격히 주목받고 있습니다.")

elif selected_country == "미국":
    st.markdown("### 🇺🇸 미국")
    st.write("**특징:** 개척 정신과 실용주의가 강한 문화적 배경을 가지고 있습니다.")
    st.info("외향형(E)과 사고형(T)의 비율이 상대적으로 높게 나타나며, 스타트업이나 도전적인 문화에서는 ENTJ나 ENFP 같은 유형이 활발하게 활약하는 경향이 있습니다.")

elif selected_country == "일본":
    st.markdown("### 🇯🇵 일본")
    st.write("**특징:** 타인에게 피해를 주지 않으려는 '메이와쿠(迷惑)' 문화가 깊게 자리 잡고 있습니다.")
    st.info("전반적으로 내향 감정(I)과 수호자 성향인 ISFJ 유형이 다수를 차지하는 편이며, 공동체의 평화와 규칙을 중시하는 J(판단형) 성향이 강하게 나타납니다.")

elif selected_country == "독일":
    st.markdown("### 🇩🇪 독일")
    st.write("**특징:** 철저한 규칙과 시간 엄수, 장인 정신으로 유명한 국가입니다.")
    st.info("통계적으로 ISTJ(청렴결백한 논리주의자) 성향과 가장 잘 부합하는 문화를 가졌다고 평가받으며, 감정보다는 논리(T)와 계획(J)을 기반으로 안정적인 사회 시스템을 선호합니다.")

st.divider()

# 3. 간단한 MBTI 매칭 퀴즈나 팁
st.subheader("💡 재미로 보는 팁")
with st.expander("내 MBTI와 어울리는 여행지는?"):
    st.write("- **ENFP / ESFP (자유로운 영혼):** 축제와 열정이 가득한 **브라질**")
    st.write("- **ISTJ / INTJ (철저한 계획파):** 기차 시간표가 칼같이 맞는 **독일**")
    st.write("- **INFP / INFJ (감성 충만 사색가):** 아기자기한 골목과 힐링이 있는 **일본**")

st.divider()
st.caption("© 2026 Global MBTI Analytics App.")
