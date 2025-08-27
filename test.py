import streamlit as st

# --- 데이터 (시대 -> 화가 -> 작품) ---
art_data = {
    "르네상스": {
        "레오나르도 다빈치": {
            "모나리자": "https://raw.githubusercontent.com/nyan-png/art-images/main/mona_lisa.jpg",
            "최후의 만찬": "https://raw.githubusercontent.com/nyan-png/art-images/main/last_supper.jpg"
        },
        "미켈란젤로": {
            "천지창조": "https://raw.githubusercontent.com/nyan-png/art-images/main/creation_of_adam.jpg"
        }
    },
    "인상주의": {
        "모네": {
            "수련": "https://raw.githubusercontent.com/nyan-png/art-images/main/water_lilies.jpg"
        },
        "고흐": {
            "별이 빛나는 밤": "https://raw.githubusercontent.com/nyan-png/art-images/main/starry_night.jpg",
            "해바라기": "https://raw.githubusercontent.com/nyan-png/art-images/main/sunflowers.jpg"
        }
    }
}

# --- Streamlit 앱 ---
st.title("🎨 시대별 화가 작품 감상")

# 시대 선택
era = st.sidebar.radio("시대를 선택하세요", list(art_data.keys()))

# 화가 선택
artist = st.sidebar.selectbox("화가를 선택하세요", list(art_data[era].keys()))

# 작품 선택
artwork = st.sidebar.selectbox("작품을 선택하세요", list(art_data[era][artist].keys()))

# 결과 출력
img_url = art_data[era][artist][artwork]
st.subheader(f"{artist} - {artwork}")
st.image(img_url, caption=f"{artist}의 작품: {artwork}", use_column_width=True)
