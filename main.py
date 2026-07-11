import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(
    page_title="K-POP 아이돌 데이터 센터",
    page_icon="🎤",
    layout="wide" # 분석 대시보드이므로 넓은 화면 레이아웃 사용
)

# 데이터 불러오기 (샘플 데이터 구성)
@st.cache_data
def load_data():
    # 실제 프로젝트 시 이 부분을 데이터베이스나 CSV 파일 로드로 변경할 수 있습니다.
    data = {
        "그룹명": ["뉴진스", "아이브", "에스파", "세븐틴", "라이즈", "투어스", "르세라핌", "스트레이 키즈"],
        "소속사": ["HYBE (어도어)", "스타쉽", "SM", "HYBE (플레디스)", "SM", "HYBE (플레디스)", "HYBE (쏘스)", "JYP"],
        "멤버수": [5, 6, 4, 13, 6, 6, 5, 8],
        "데뷔년도": [2022, 2021, 2020, 2015, 2023, 2024, 2022, 2018],
        "대표곡": ["Ditto", "I AM", "Supernova", "Super Shy", "Get A Guitar", "첫 만남은 계획대로 되지 않아", "EASY", "Chk Chk Boom"]
    }
    df = pd.DataFrame(data)
    # 2026년 기준으로 연차 계산
    df["연차 (2026년 기준)"] = 2026 - df["데뷔년도"] + 1
    return df

df = load_data()

# 2. 타이틀 영역
st.title("🎤 K-POP 아이돌 검색 및 분석 대시보드")
st.write("원하는 아이돌을 검색하고 소속사별, 연차별 데이터를 한눈에 분석해 보세요.")

st.divider()

# 3. 사이드바 - 필터링 기능
st.sidebar.header("🔍 데이터 필터")

# 소속사 필터
companies = ["전체"] + list(df["소속사"].unique())
selected_company = st.sidebar.selectbox("소속사를 선택하세요", companies)

# 검색창
search_query = st.sidebar.text_input("아이돌 그룹명 검색", "")

# 데이터 필터링 적용
filtered_df = df.copy()
if selected_company != "전체":
    filtered_df = filtered_df[filtered_df["소속사"] == selected_company]
if search_query:
    filtered_df = filtered_df[filtered_df["그룹명"].str.contains(search_query, case=False)]

# 4. 메인 화면 - 통계 요약 (Metrics)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("총 등록 그룹 수", f"{len(filtered_df)} 개")
with col2:
    st.metric("평균 멤버 수", f"{filtered_df['멤버수'].mean():.1f} 명")
with col3:
    st.metric("평균 연차", f"{filtered_df['연차 (2026년 기준)'].mean():.1f} 년차")

st.write("")

# 5. 데이터 표 출력
st.subheader("📋 아이돌 리스트")
st.dataframe(filtered_df, use_container_width=True)

st.divider()

# 6. 간단한 분석 차트 데이터 시각화
st.subheader("📊 차트 분석")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.markdown("##### 📈 그룹별 멤버 수 비교")
    # 바 차트 시각화
    st.bar_chart(data=filtered_df, x="그룹명", y="멤버수", color="#ff4b4b")

with chart_col2:
    st.markdown("##### ⏳ 그룹별 연차 현황")
    # 선 차트 시각화
    st.line_chart(data=filtered_df, x="그룹명", y="연차 (2026년 기준)", color="#29b5e8")

st.divider()
st.caption("© 2026 K-POP Idol Data Analytics App. Powered by Streamlit.")
