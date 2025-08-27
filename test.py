import streamlit as st
import random

# --- 만화 장르별 추천 데이터 ---
manga_data = {
    "액션": [
        {"title": "나루토", "desc": "닌자의 세계에서 펼쳐지는 성장과 우정의 이야기", 
         "img": "https://upload.wikimedia.org/wikipedia/en/9/94/NarutoCoverTankobon1.jpg"},
        {"title": "원피스", "desc": "해적왕을 꿈꾸는 루피와 동료들의 대모험", 
         "img": "https://upload.wikimedia.org/wikipedia/en/2/2c/OnePieceVol61Cover.jpg"},
        {"title": "진격의 거인", "desc": "거인과 인류의 생존 전쟁", 
         "img": "https://upload.wikimedia.org/wikipedia/en/7/70/Attack_on_Titan_cover.jpg"}
    ],
    "로맨스": [
        {"title": "너의 이름은", "desc": "운명처럼 얽히는 두 소년소녀의 이야기", 
         "img": "https://upload.wikimedia.org/wikipedia/en/0/0b/Your_Name_poster.png"},
        {"title": "오렌지", "desc": "편지를 통해 미래를 바꾸려는 고등학생들의 이야기", 
         "img": "https://upload.wikimedia.org/wikipedia/en/7/73/Orange_Volume_1.jpg"},
        {"title": "토라도라!", "desc": "작지만 무서운 소녀와 순진한 소년의 러브코미디", 
         "img": "https://upload.wikimedia.org/wikipedia/en/5/5b/Toradora%21_light_novel_volume_1_cover.jpg"}
    ],
    "판타지": [
        {"title": "풀메탈 알케미스트", "desc": "연금술 형제가 잃어버린 것을 되찾기 위한 여정", 
         "img": "https://upload.wikimedia.org/wikipedia/en/2/2a/Fullmetal_vol_1.jpg"},
        {"title": "블리치", "desc": "사신의 힘을 얻은 소년의 전투와 성장", 
         "img": "https://upload.wikimedia.org/wikipedia/en/7/72/Bleach_cover_01.jpg"},
        {"title": "Re:제로부터 시작하는 이세계 생활", "desc": "죽음을 반복하며 운명을 개척하는 소년의 이야기", 
         "img": "https://upload.wikimedia.org/wikipedia/en/8/8c/Re_Zero_light_novel_volume_1.jpg"}
    ],
    "스포츠": [
        {"title": "슬램덩크", "desc": "농구를 통해 성장하는 청춘들의 이야기", 
         "img": "https://upload.wikimedia.org/wikipedia/en/0/04/Slam_Dunk_volume_1_cover.jpg"},
        {"title": "하이큐!!", "desc": "배구를 향한 열정과 팀워크의 이야기", 
         "img": "https://upload.wikimedia.org/wikipedia/en/8/86/Haikyu_volume_1.jpg"},
        {"title": "아이실드 21", "desc": "미식축구를 통해 성장하는 소년의 도전", 
         "img": "https://upload.wikimedia.org/wikipedia/en/3/37/Eyeshield21_vol01_Cover.jpg"}
    ]
}

# --- Streamlit 앱 ---
st.title("📚 만화책 추천기")

# 사이드바에서 장르 선택
genre = st.sidebar.radio("장르를 선택하세요", list(manga_data.keys()))

# 버튼 누르면 추천
if st.button("추천 받기"):
    choice = random.choice(manga_data[genre])
    st.subheader(f"✅ 추천 만화: {choice['title']}")
    st.image(choice["img"], caption=choice["title"], use_column_width=True)
    st.write(choice["desc"])
else:
    st.info("👉 사이드바에서 장르를 고르고 '추천 받기' 버튼을 눌러보세요!")
