import streamlit as st
import random

st.set_page_config(page_title="만화책 추천기", page_icon="📚", layout="wide")

# --- 만화 장르별 추천 데이터 ---
manga_data = {
    "액션": [
        {"title": "나루토", "desc": "닌자의 세계에서 펼쳐지는 성장과 우정 이야기",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"},
        {"title": "원피스", "desc": "해적왕을 꿈꾸는 루피와 동료들의 대모험",
         "img": "https://images.unsplash.com/photo-1542744095-1e3b3f6f4e5b"},
        {"title": "진격의 거인", "desc": "거인과 인류의 생존 전쟁",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"},
        {"title": "블리치", "desc": "사신의 힘을 얻은 소년의 전투와 성장",
         "img": "https://images.unsplash.com/photo-1542744095-1e3b3f6f4e5b"},
        {"title": "헌터x헌터", "desc": "헌터가 되기 위한 소년의 모험",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"}
    ],
    "로맨스": [
        {"title": "너의 이름은", "desc": "운명처럼 얽히는 두 소년소녀 이야기",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"},
        {"title": "오렌지", "desc": "편지를 통해 미래를 바꾸려는 고등학생들의 이야기",
         "img": "https://images.unsplash.com/photo-1542744095-1e3b3f6f4e5b"},
        {"title": "토라도라!", "desc": "작지만 무서운 소녀와 순진한 소년의 러브코미디",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"},
        {"title": "피치 걸", "desc": "사랑과 우정을 그린 학원 로맨스",
         "img": "https://images.unsplash.com/photo-1542744095-1e3b3f6f4e5b"},
        {"title": "카드캡터 사쿠라", "desc": "마법과 소년 소녀의 성장 이야기",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"}
    ],
    "판타지": [
        {"title": "풀메탈 알케미스트", "desc": "형제가 잃어버린 것을 되찾는 여정",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"},
        {"title": "Re:제로", "desc": "죽음을 반복하며 운명을 개척하는 소년 이야기",
         "img": "https://images.unsplash.com/photo-1542744095-1e3b3f6f4e5b"},
        {"title": "소드 아트 온라인", "desc": "가상현실 세계에서의 모험과 사랑",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"},
        {"title": "블랙 클로버", "desc": "마법 왕이 되기 위한 소년의 성장기",
         "img": "https://images.unsplash.com/photo-1542744095-1e3b3f6f4e5b"},
        {"title": "페어리 테일", "desc": "길드 동료들과의 모험과 우정",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"}
    ],
    "스포츠": [
        {"title": "슬램덩크", "desc": "농구를 통해 성장하는 청춘 이야기",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"},
        {"title": "하이큐!!", "desc": "배구를 향한 열정과 팀워크 이야기",
         "img": "https://images.unsplash.com/photo-1542744095-1e3b3f6f4e5b"},
        {"title": "아이실드 21", "desc": "미식축구를 통해 성장하는 소년 이야기",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"},
        {"title": "킹덤", "desc": "중국 전국시대를 배경으로 한 전쟁 만화",
         "img": "https://images.unsplash.com/photo-1542744095-1e3b3f6f4e5b"},
        {"title": "베이비 스텝", "desc": "테니스를 통해 성장하는 청춘 이야기",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"}
    ],
    "스릴러": [
        {"title": "데스노트", "desc": "죽음의 노트를 손에 넣은 소년의 심리 게임",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"},
        {"title": "몬스터", "desc": "연쇄살인 사건의 진실을 쫓는 의사 이야기",
         "img": "https://images.unsplash.com/photo-1542744095-1e3b3f6f4e5b"},
        {"title": "도쿄구울", "desc": "인간과 구울 사이의 갈등과 성장",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"}
    ],
    "코미디": [
        {"title": "짱구는 못말려", "desc": "유쾌한 일상과 장난꾸러기 소년 이야기",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"},
        {"title": "은혼", "desc": "사무라이와 코믹 사건이 함께하는 이야기",
         "img": "https://images.unsplash.com/photo-1542744095-1e3b3f6f4e5b"},
        {"title": "니세코이", "desc": "사랑과 코미디가 가득한 학원 이야기",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"}
    ],
    "공포": [
        {"title": "링", "desc": "저주받은 비디오 테이프와 공포의 이야기",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"},
        {"title": "도쿄 이블", "desc": "도쿄를 배경으로 한 스릴러 공포",
         "img": "https://images.unsplash.com/photo-1542744095-1e3b3f6f4e5b"}
    ],
    "역사": [
        {"title": "킹덤", "desc": "중국 전국시대 전쟁 이야기",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"},
        {"title": "베르사유의 장미", "desc": "프랑스 혁명을 배경으로 한 역사 로맨스",
         "img": "https://images.unsplash.com/photo-1542744095-1e3b3f6f4e5b"}
    ],
    "SF": [
        {"title": "플루토", "desc": "아톰 시리즈를 기반으로 한 SF 추리",
         "img": "https://images.unsplash.com/photo-1519681393784-1e3b3f6f4e5b"},
        {"title": "은하철도 999", "desc": "우주 여행과 인간 이야기",
         "img": "https://images.unsplash.com/photo-1542744095-1e3b3f6f4e5b"}
    ]
}

# --- Streamlit 앱 UI ---
st.title("📚 만화책 추천기 (장르별)")

# 장르 선택
genre = st.sidebar.selectbox("장르 선택", list(manga_data.keys()))

# 추천 버튼
if st.button("추천 받기"):
    choice = random.choice(manga_data[genre])
    st.subheader(f"✅ 추천 만화: {choice['title']}")
    st.image(choice["img"], caption=choice["title"], use_column_width=True)
    st.write(choice["desc"])
else:
    st.info("👉 장르를 선택하고 '추천 받기' 버튼을 눌러주세요!")
