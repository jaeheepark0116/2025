import streamlit as st

st.set_page_config(page_title="MBTI 기반 진로 추천", page_icon="🎯", layout="wide")

# 간단 데이터
MBTI_DATA = {
    "ENFP": {
        "summary": "아이디어 넘치고 사람 좋아하는 탐험가형",
        "jobs": [
            {"title": "마케팅 기획자", "why": "아이디어 발산과 스토리텔링에 강점. 캠페인 기획에 적합.", "tags": ["창의", "대인", "트렌드"]},
            {"title": "프로덕트 매니저", "why": "사용자 공감과 커뮤니케이션으로 팀 조율에 강점.", "tags": ["문제해결", "커뮤니케이션"]},
            {"title": "크리에이티브 디렉터", "why": "브랜딩과 콘셉트 메이킹에 적합.", "tags": ["창의", "비전"]},
            {"title": "콘텐츠 플래너", "why": "이야기 구조화와 트렌드 감각 좋음.", "tags": ["콘텐츠", "기획"]},
            {"title": "행사기획자", "why": "사람 중심의 경험 설계에 강점.", "tags": ["대인", "운영"]}
        ],
        "skills": ["스토리텔링", "커뮤니케이션", "기획력", "트렌드 분석"],
        "majors": ["경영/마케팅", "미디어커뮤니케이션", "디자인(브랜딩)"]
    },
    "INTJ": {
        "summary": "전략적이고 구조화 잘하는 설계자형",
        "jobs": [
            {"title": "전략기획", "why": "장기적 관점에서 구조 설계에 강함.", "tags": ["전략", "분석"]},
            {"title": "데이터 사이언티스트", "why": "가설-검증 루프에 익숙, 정량 분석 적합.", "tags": ["데이터", "문제해결"]},
            {"title": "UX 리서처", "why": "체계적 조사/분석에 강점.", "tags": ["리서치", "논리"]},
            {"title": "정책분석가", "why": "복잡한 시스템 이해/설계에 적합.", "tags": ["분석", "거시관점"]},
            {"title": "기술컨설턴트", "why": "기술-비즈니스 연결, 요구사항 구조화.", "tags": ["설계", "컨설팅"]}
        ],
        "skills": ["논리적 사고", "모델링", "문제정의", "리서치"],
        "majors": ["산업공학", "통계/데이터", "정책학", "HCI"]
    },
    "ISFJ": {
        "summary": "세심하고 성실한 헌신가형",
        "jobs": [
            {"title": "임상심리사", "why": "공감과 책임감, 절차 준수에 강점.", "tags": ["대인", "윤리"]},
            {"title": "보건의료행정", "why": "정확성/규정 준수 필요.", "tags": ["정확성", "운영"]},
            {"title": "초중등교사", "why": "돌봄과 체계적 관리에 적합.", "tags": ["교육", "관리"]},
            {"title": "HR 운영", "why": "세부 프로세스/내규 관리 강점.", "tags": ["운영", "조직"]},
            {"title": "기록연구사", "why": "정리/보존/체계화 업무와 적합.", "tags": ["정리", "아카이브"]}
        ],
        "skills": ["세부관리", "공감", "문서화", "윤리의식"],
        "majors": ["심리학", "교육학", "보건행정", "문헌정보"]
    },
    "ESTP": {
        "summary": "현장감각 뛰어난 해결사형",
        "jobs": [
            {"title": "영업/BD", "why": "실전 협상과 네트워킹 강점.", "tags": ["대인", "실행"]},
            {"title": "이벤트 운영", "why": "현장 이슈 대응, 즉흥 문제해결.", "tags": ["운영", "기민"]},
            {"title": "스포츠 매니지먼트", "why": "현장 중심의 역동적 환경 선호.", "tags": ["현장", "리더십"]},
            {"title": "현장 PM", "why": "리소스/일정 조율, 빠른 결단.", "tags": ["PM", "조율"]},
            {"title": "트레이더", "why": "리스크 감내/순간 판단.", "tags": ["결단", "분석"]}
        ],
        "skills": ["협상", "우선순위 판단", "리스크 관리", "대응력"],
        "majors": ["경영", "스포츠과학", "이벤트/컨벤션", "공학계열(PM)"]
    }
}

ALL_TYPES = ['INTJ','INTP','ENTJ','ENTP','INFJ','INFP','ENFJ','ENFP','ISTJ','ISFJ','ESTJ','ESFJ','ISTP','ISFP','ESTP','ESFP']

# 사이드바
st.sidebar.title("MBTI 선택")
selected = st.sidebar.selectbox("내 MBTI를 골라줘", ALL_TYPES, index=ALL_TYPES.index("ENFP"))

st.title("🎯 MBTI 기반 진로 추천")
st.caption("참고용 가이드예요. 개인 성향/경험은 MBTI보다 더 중요해요!")

# 선택 요약
if selected in MBTI_DATA:
    st.subheader(f"{selected} · {MBTI_DATA[selected]['summary']}")
else:
    st.subheader(f"{selected}")
    st.info("이 유형은 아직 상세 데이터가 적어요. 유사 성향 유형 참고를 추천!")

# 추천 카드
def render_job_card(job):
    with st.container():
        st.markdown(f"**{job['title']}**")
        st.write(job["why"])
        if "tags" in job:
            st.write("태그: " + " · ".join(job["tags"]))
        st.divider()

data = MBTI_DATA.get(selected)
if data:
    st.markdown("#### 추천 직업")
    for job in data["jobs"]:
        render_job_card(job)

    with st.expander("역량/전공 팁"):
        st.write("핵심 역량: " + ", ".join(data["skills"]))
        st.write("관련 전공: " + ", ".join(data["majors"]))
else:
    st.warning("임시 추천: 관심 키워드로 탐색해보세요!")

# 유사 유형도 보기
SIMILAR = {
    "ENFP": ["ENFJ", "ENTP", "INFP"],
    "INTJ": ["INTP", "ENTJ", "INFJ"],
    "ISFJ": ["ISTJ", "ESFJ", "ISFP"],
    "ESTP": ["ESFP", "ENTP", "ESTJ"]
}
similar = SIMILAR.get(selected, [])
if similar:
    st.markdown("#### 비슷한 유형도 참고해봐")
    st.write(", ".join(similar))

# 피드백
st.divider()
st.write("의견 남기기")
fb = st.text_area("어떤 점이 유용했어? 추가로 보고 싶은 직업은?")
if st.button("보내기"):
    st.success("고마워! 다음 업데이트에 참고할게 🙌")
