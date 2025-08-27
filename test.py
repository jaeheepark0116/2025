import streamlit as st

# --- 시대별 화가와 작품 데이터 (GitHub raw 이미지 링크) ---
art_data = {
    "르네상스": {
        "레오나르도 다빈치": {
            "모나리자": "https://raw.githubusercontent.com/nyan-png/art-images/main/mona_lisa.jpg",
            "최후의 만찬": "https://raw.githubusercontent.com/nyan-png/art-images/main/last_supper.jpg",
            "비트루비우스 인간": "https://raw.githubusercontent.com/nyan-png/art-images/main/vitruvian_man.jpg"
        },
        "미켈란젤로": {
            "천지창조": "https://raw.githubusercontent.com/nyan-png/art-images/main/creation_of_adam.jpg",
            "피에타": "https://raw.githubusercontent.com/nyan-png/art-images/main/pieta.jpg"
        },
        "라파엘로": {
            "아테네 학당": "https://raw.githubusercontent.com/nyan-png/art-images/main/school_of_athens.jpg"
        }
    },
    "바로크": {
        "렘브란트": {
            "야경": "https://raw.githubusercontent.com/nyan-png/art-images/main/night_watch.jpg",
            "자화상": "https://raw.githubusercontent.com/nyan-png/art-images/main/rembrandt_self.jpg"
        },
        "카라바조": {
            "골리앗의 머리를 든 다윗": "https://raw.githubusercontent.com/nyan-png/art-images/main/david_goliath.jpg"
        },
        "베르메르": {
            "진주 귀걸이를 한 소녀": "https://raw.githubusercontent.com/nyan-png/art-images/main/girl_with_pearl.jpg"
        }
    },
    "인상주의": {
        "모네": {
            "수련": "https://raw.githubusercontent.com/nyan-png/art-images/main/water_lilies.jpg",
            "인상, 해돋이": "https://raw.githubusercontent.com/nyan-png/art-images/main/impression_sunrise.jpg"
        },
        "고흐": {
            "별이 빛나는 밤": "https://raw.githubusercontent.com/nyan-png/art-images/main/starry_night.jpg",
            "해바라기": "https://raw.githubusercontent.com/nyan-png/art-images/main/sunflowers.jpg",
            "밤의 카페 테라스": "https://raw.githubusercontent.com/nyan-png/art-images/main/cafe_terrace.jpg"
        },
        "르누아르": {
            "피아노 치는 소녀들": "https://raw.githubusercontent.com/nyan-png/art-images/main/girls_piano.jpg",
            "물랭 드 라 갈레트의 무도회": "https://raw.githubusercontent.com/nyan-png/art-images/main/moulin_de_la_galette.jpg"
        }
    },
    "근대": {
        "피카소": {
            "게르니카": "https://raw.githubusercontent.com/nyan-png/art-images/main/guernica.jpg",
            "아비뇽의 처녀들": "https://raw.githubusercontent.com/nyan-png/art-images/main/les_demoiselles.jpg"
        },
        "마티스": {
            "춤": "https://raw.githubusercontent.com/nyan-png/art-images/main/dance.jpg"
        },
        "달리": {
            "기억의 지속": "https://raw.githubusercontent.com/nyan-png/art-images/main/persistence_memory.jpg"
        }
    }
}

# --- Streamlit 앱 ---
st.title("🎨 시대별 명화 감상 앱")

# 사이드바: 시대 선택
era = st.sidebar.radio("시대를 선택하세요", list(art_data.keys()))

# 사이드바: 화가 선택
artist = st.sidebar.selectbox("화가를 선택하세요", list(art_data[era].keys()))

# 사이드바: 작품 선택
artwork = st.sidebar.selectbox("작품을 선택하세요", list(art_data[era][artist].keys()))

# 결과 출력
img_url = art_data[era][artist][artwork]
st.subheader(f"{artist} - {artwork}")
st.image(img_url, caption=f"{artist}의 작품: {artwork}", use_column_width=True)
