import streamlit as st

# --- 동물 데이터 (확장 + 썸네일 적용) ---
animal_data = {
    "포유류": {
        "사자": {"food": "고기 🥩 (주로 초식동물)", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/400px-Lion_waiting_in_Namibia.jpg"},
        "호랑이": {"food": "고기 🥩 (사슴, 멧돼지 등)", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Tiger.50.jpg/400px-Tiger.50.jpg"},
        "코끼리": {"food": "풀 🌱, 나뭇잎 🍃, 과일 🍎", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/African_Bush_Elephant.jpg/400px-African_Bush_Elephant.jpg"},
        "곰": {"food": "잡식 🐟🍯🍓 (연어, 꿀, 열매 등)", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Brown_bear_in_forest.jpg/400px-Brown_bear_in_forest.jpg"},
        "판다": {"food": "대나무 🎋", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Grosser_Panda.JPG/400px-Grosser_Panda.JPG"},
        "기린": {"food": "나뭇잎 🍃 (특히 아카시아)", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Giraffe_standing.jpg/400px-Giraffe_standing.jpg"},
        "여우": {"food": "잡식 🐭🍓 (작은 동물, 과일 등)", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/2010-british-red-fox.jpg/400px-2010-british-red-fox.jpg"},
        "늑대": {"food": "고기 🥩 (사슴, 토끼 등)", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Canis_lupus_laying.jpg/400px-Canis_lupus_laying.jpg"},
        "코알라": {"food": "유칼립투스 잎 🌿", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Koala_climbing_tree.jpg/400px-Koala_climbing_tree.jpg"},
        "캥거루": {"food": "풀 🌱, 나뭇잎 🍃", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Kangaroo_Australia_01.jpg/400px-Kangaroo_Australia_01.jpg"},
        "하마": {"food": "풀 🌱", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Hippopotamus_in_South_Africa_adjusted.jpg/400px-Hippopotamus_in_South_Africa_adjusted.jpg"},
        "치타": {"food": "고기 🥩 (영양, 토끼 등)", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Cheetah_with_cubs_2.jpg/400px-Cheetah_with_cubs_2.jpg"},
    },
    "조류": {
        "독수리": {"food": "고기 🥩 (사체, 작은 동물)", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Griffon_vulture_in_flight.jpg/400px-Griffon_vulture_in_flight.jpg"},
        "부엉이": {"food": "작은 동물 🐭, 새 🐦", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Eurasian_Eagle-Owl_RWD3.jpg/400px-Eurasian_Eagle-Owl_RWD3.jpg"},
        "참새": {"food": "씨앗 🌾, 곤충 🐛", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/House_Sparrow_mar08.jpg/400px-House_Sparrow_mar08.jpg"},
        "앵무새": {"food": "씨앗 🌾, 과일 🍎", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Ara_ararauna_Luc_Viatour.jpg/400px-Ara_ararauna_Luc_Viatour.jpg"},
        "펭귄": {"food": "물고기 🐟, 크릴 🦐", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Aptenodytes_forsteri_-Snow_Hill_Island%2C_Antarctica_-adults_and_juveniles-8.jpg/400px-Aptenodytes_forsteri.jpg"},
        "타조": {"food": "풀 🌱, 씨앗 🌾", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Common_ostrich_male.jpg/400px-Common_ostrich_male.jpg"},
        "공작": {"food": "씨앗 🌾, 곤충 🐛, 과일 🍎", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Peacock_Plumage.jpg/400px-Peacock_Plumage.jpg"},
        "백조": {"food": "수생식물 🌿, 곤충 🐛", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Cygnus_olor_AdPP.jpg/400px-Cygnus_olor_AdPP.jpg"},
    },
    "해양 동물": {
        "돌고래": {"food": "물고기 🐟, 오징어 🦑", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Dolphins_in_the_Red_Sea.jpg/400px-Dolphins_in_the_Red_Sea.jpg"},
        "상어": {"food": "물고기 🐟, 해양 포유류 🐋", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/White_shark.jpg/400px-White_shark.jpg"},
        "고래": {"food": "플랑크톤 🦠, 물고기 🐟", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Humpback_stellwagen_edit.jpg/400px-Humpback_stellwagen_edit.jpg"},
        "문어": {"food": "갑각류 🦐, 조개 🦪, 물고기 🐟", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Octopus2.jpg/400px-Octopus2.jpg"},
        "거북이": {"food": "해초 🌿, 해조류 🌱", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Green_turtle_swimming_over_coral_reefs_in_Kona.jpg/400px-Green_turtle_swimming_over_coral_reefs_in_Kona.jpg"},
        "해마": {"food": "플랑크톤 🦠, 작은 갑각류 🦐", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Hippocampus_seahorse.jpg/400px-Hippocampus_seahorse.jpg"},
        "물개": {"food": "물고기 🐟, 오징어 🦑", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Sealion2.jpg/400px-Sealion2.jpg"},
    },
    "파충류 & 양서류": {
        "악어": {"food": "고기 🥩 (물가 동물)", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/NileCrocodile.jpg/400px-NileCrocodile.jpg"},
        "뱀": {"food": "작은 동물 🐭, 새 🐦, 개구리 🐸", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Python_molurus_molurus.jpg/400px-Python_molurus_molurus.jpg"},
        "개구리": {"food": "곤충 🐛, 작은 절지동물 🦗", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Green_frog_in_pond.jpg/400px-Green_frog_in_pond.jpg"},
        "도마뱀": {"food": "곤충 🐛, 작은 동물 🐭", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Komodo_dragon_Varanus_komodoensis_edit2.jpg/400px-Komodo_dragon_Varanus_komodoensis_edit2.jpg"},
        "거북": {"food": "풀 🌱, 곤충 🐛", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Greek_tortoise_Male.jpg/400px-Greek_tortoise_Male.jpg"},
    },
    "곤충": {
        "벌": {"food": "꽃꿀 🍯, 꽃가루 🌸", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Honeybee_on_purple_coneflower.jpg/400px-Honeybee_on_purple_coneflower.jpg"},
        "개미": {"food": "잡식 🍞🪱 (설탕, 곤충, 식물 등)", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Ant_Oecophylla_smargdina.jpg/400px-Ant_Oecophylla_smargdina.jpg"},
        "무당벌레": {"food": "진딧물 🐛", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Coccinella_septempunctata01.jpg/400px-Coccinella_septempunctata01.jpg"},
        "잠자리": {"food": "작은 곤충 🦟", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Common_Darter_dragonfly.jpg/400px-Common_Darter_dragonfly.jpg"},
        "나비": {"food": "꽃꿀 🍯", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Monarch_Butterfly_Danaus_plexippus_Male_2664px.jpg/400px-Monarch_Butterfly.jpg"},
        "사마귀": {"food": "곤충 🦟, 작은 동물 🐭", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Mantis_religiosa_1_Luc_Viatour.jpg/400px-Mantis_religiosa_1_Luc_Viatour.jpg"},
        "매미": {"food": "수액 🌳", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Tibicen_chloromera_fg01.jpg/400px-Tibicen_chloromera_fg01.jpg"},
    }
}

# --- Streamlit 앱 ---
st.title("🌍 동물 백과사전 (먹이 & 사진)")

# 검색 입력창
search_query = st.text_input("🔍 동물 이름으로 검색하세요:")

if search_query:
    found = False
    for category, animals in animal_data.items():
        if search_query in animals:
            food = animals[search_query]["food"]
            img = animals[search_query]["img"]
            st.success(f"✅ [{category}] {search_query}의 주 먹이는 **{food}** 입니다!")
            st.image(img, caption=search_query, use_container_width=True)
            found = True
            break
    if not found:
        st.warning("❌ 해당 동물 정보를 찾을 수 없습니다. 카테고리에서 직접 선택해보세요!")

# --- 사이드바 탐색 ---
st.sidebar.title("📂 카테고리별 탐색")
category = st.sidebar.radio("카테고리 선택", list(animal_data.keys()))
animal_name = st.sidebar.selectbox("동물 선택", [""] + sorted(animal_data[category].keys()))

if animal_name:
    food = animal_data[category][animal_name]["food"]
    img = animal_data[category][animal_name]["img"]
    st.success(f"✅ [{category}] {animal_name}의 주 먹이는 **{food}** 입니다!")
    st.image(img, caption=animal_name, use_container_width=True)
