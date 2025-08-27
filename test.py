import streamlit as st

st.set_page_config(page_title="미술사 탐색기", page_icon="🖼️", layout="wide")

# ---------------------------
# 데이터: 시대 → 화가 → 작품(제목, 연도, 이미지)
# ---------------------------
art_data = {
    "르네상스": {
        "레오나르도 다 빈치": [
            {"title": "모나 리자", "year": "c.1503–1506",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/400px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg"},
            {"title": "최후의 만찬", "year": "1495–1498",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/%C3%9Altima_Cena_-_Da_Vinci_5.jpg/400px-%C3%9Altima_Cena_-_Da_Vinci_5.jpg"},
        ],
        "미켈란젤로": [
            {"title": "천지창조 (아담의 창조)", "year": "c.1512",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg/400px-Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg"},
            {"title": "다비드", "year": "1501–1504",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/%27David%27_by_Michelangelo_Fir_JBU001.jpg/400px-%27David%27_by_Michelangelo_Fir_JBU001.jpg"},
        ],
        "라파엘로": [
            {"title": "아테네 학당", "year": "1509–1511",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Sanzio_01.jpg/400px-Sanzio_01.jpg"},
            {"title": "시스틴의 성모", "year": "1512",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Raffael_067.jpg/400px-Raffael_067.jpg"},
        ],
    },
    "바로크": {
        "카라바조": [
            {"title": "성 마태오의 소명", "year": "1599–1600",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Caravaggio_-_The_Calling_of_Saint_Matthew.jpg/400px-Caravaggio_-_The_Calling_of_Saint_Matthew.jpg"},
            {"title": "바쿠스", "year": "c.1595",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Caravaggio_-_Bacchus.jpg/400px-Caravaggio_-_Bacchus.jpg"},
        ],
        "렘브란트": [
            {"title": "야경", "year": "1642",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/The_Nightwatch_by_Rembrandt.jpg/400px-The_Nightwatch_by_Rembrandt.jpg"},
            {"title": "툴프 박사의 해부학 강의", "year": "1632",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Rembrandt_-_The_Anatomy_Lesson_of_Dr_Nicolaes_Tulp.jpg/400px-Rembrandt_-_The_Anatomy_Lesson_of_Dr_Nicolaes_Tulp.jpg"},
        ],
        "루벤스": [
            {"title": "십자가 올리기", "year": "1610–1611",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Rubens_-_The_Elevation_of_the_Cross_-_WGA20257.jpg/400px-Rubens_-_The_Elevation_of_the_Cross_-_WGA20257.jpg"},
            {"title": "십자가에서 내림", "year": "1612–1614",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Peter_Paul_Rubens_-_Descent_from_the_Cross_-_WGA20175.jpg/400px-Peter_Paul_Rubens_-_Descent_from_the_Cross_-_WGA20175.jpg"},
        ],
    },
    "인상파": {
        "클로드 모네": [
            {"title": "인상, 해돋이", "year": "1872",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Claude_Monet%2C_Impression%2C_soleil_levant.jpg/400px-Claude_Monet%2C_Impression%2C_soleil_levant.jpg"},
            {"title": "수련", "year": "1916",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Monet_Water_Lilies_1916.jpg/400px-Monet_Water_Lilies_1916.jpg"},
        ],
        "오귀스트 르누아르": [
            {"title": "물랭 드 라 갈레트의 무도회", "year": "1876",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Auguste_Renoir_-_Dance_at_Le_Moulin_de_la_Galette_-_Google_Art_Project.jpg/400px-Auguste_Renoir_-_Dance_at_Le_Moulin_de_la_Galette_-_Google_Art_Project.jpg"},
        ],
        "에드가 드가": [
            {"title": "발레 수업", "year": "c.1871–1874",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Edgar_Degas_-_The_Ballet_Class_-_Google_Art_Project.jpg/400px-Edgar_Degas_-_The_Ballet_Class_-_Google_Art_Project.jpg"},
        ],
    },
    "후기 인상파": {
        "빈센트 반 고흐": [
            {"title": "별이 빛나는 밤", "year": "1889",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/400px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"},
            {"title": "해바라기", "year": "1888",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Vincent_Willem_van_Gogh_128.jpg/400px-Vincent_Willem_van_Gogh_128.jpg"},
        ],
        "폴 고갱": [
            {"title": "설교 후의 환상", "year": "1888",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Paul_Gauguin_-_Vision_After_the_Sermon_%28Jacob_Wrestling_with_the_Angel%29.jpg/400px-Paul_Gauguin_-_Vision_After_the_Sermon_%28Jacob_Wrestling_with_the_Angel%29.jpg"},
            {"title": "우리는 어디서 왔는가, 우리는 무엇인가, 어디로 가는가", "year": "1897–1898",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/D%27où_venons-nous_Que_sommes-nous_Où_allons-nous.jpg/400px-D%27où_venons-nous_Que_sommes-nous_Où_allons-nous.jpg"},
        ],
        "폴 세잔": [
            {"title": "카드놀이 하는 사람들", "year": "c.1894–1895",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Paul_C%C3%A9zanne%2C_The_Card_Players%2C_c._1894%E2%80%965.jpg/400px-Paul_C%C3%A9zanne%2C_The_Card_Players%2C_c._1894%E2%80%965.jpg"},
            {"title": "몽 생트 빅투아르", "year": "c.1904–1906",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Paul_Ce%CC%81zanne_-_Mont_Sainte-Victoire.jpg/400px-Paul_Ce%CC%81zanne_-_Mont_Sainte-Victoire.jpg"},
        ],
    },
    "근대 미술": {
        "파블로 피카소": [
            {"title": "아비뇽의 처녀들", "year": "1907",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Les_Demoiselles_d%27Avignon.jpg/400px-Les_Demoiselles_d%27Avignon.jpg"},
            {"title": "게르니카", "year": "1937",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Guernica.jpg/400px-Guernica.jpg"},
        ],
        "앙리 마티스": [
            {"title": "춤", "year": "1910",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Henri_Matisse%2C_1910%2C_La_Danse%2C_oil_on_canvas%2C_260_x_391_cm%2C_Hermitage%2C_St_Petersburg.jpg/400px-Henri_Matisse%2C_1910%2C_La_Danse%2C_oil_on_canvas%2C_260_x_391_cm%2C_Hermitage%2C_St_Petersburg.jpg"},
            {"title": "모자를 쓴 여인", "year": "1905",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Matisse-Woman-with-a-Hat.jpg/400px-Matisse-Woman-with-a-Hat.jpg"},
        ],
    },
    "낭만주의": {
        "외젠 들라크루아": [
            {"title": "민중을 이끄는 자유", "year": "1830",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Eug%C3%A8ne_Delacroix_-_La_libert%C3%A9_guidant_le_peuple.jpg/400px-Eug%C3%A8ne_Delacroix_-_La_libert%C3%A9_guidant_le_peuple.jpg"},
        ],
        "J. M. W. 터너": [
            {"title": "전함 테메레르", "year": "1839",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Joseph_Mallord_William_Turner_-_The_Fighting_Temeraire%2C_tugged_to_her_last_berth_to_be_broken.jpg/400px-Joseph_Mallord_William_Turner_-_The_Fighting_Temeraire%2C_tugged_to_her_last_berth_to_be_broken.jpg"},
            {"title": "비, 증기 그리고 속도", "year": "1844",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/JMW_Turner_-_Rain_Steam_and_Speed_-_The_Great_Western_Railway.jpg/400px-JMW_Turner_-_Rain_Steam_and_Speed_-_The_Great_Western_Railway.jpg"},
        ],
        "프란시스코 고야": [
            {"title": "1808년 5월 3일", "year": "1814",
             "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/El_Tres_de_Mayo%2C_by_Francisco_de_Goya%2C_from_Prado_thin_black_margin.jpg/400px-El_Tres_de_Mayo%2C_by_Francisco_de_Goya%2C_from_Prado_thin_black_margin.jpg"},
        ],
    },
}

# ---------------------------
# UI
# ---------------------------
st.title("🖼️ 시대별 · 화가별 대표 작품 보기")

# 1) 시대 선택
era = st.sidebar.radio("시대를 선택하세요", list(art_data.keys()))

# 2) 화가 선택 (시대에 따라 동적으로 목록 변경)
painters = list(art_data[era].keys())
painter = st.sidebar.selectbox("화가를 선택하세요", painters)

st.markdown(f"### {era} · **{painter}**의 주요 작품")

# 3) 작품 카드 그리드 표시
works = art_data[era][painter]
cols = st.slider("한 줄에 보여줄 작품 수", min_value=2, max_value=4, value=3, help="화면 폭에 맞춰 조절하세요")
grid = st.columns(cols)

for i, work in enumerate(works):
    with grid[i % cols]:
        st.image(work["img"], use_container_width=True, caption=work["title"])
        st.caption(f"📅 {work['year']} · {painter}")

# (선택) 작품 수가 많아질 경우 대비해 간단한 검색 필터를 붙이려면 아래 주석을 해제하세요.
# keyword = st.text_input("작품 제목 검색")
# if keyword:
#     works = [w for w in works if keyword.strip() in w["title"]]
