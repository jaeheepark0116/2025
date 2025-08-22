import streamlit as st

# 동물별 주 먹이 & 이미지 사전
animal_data = {
    # 포유류
    "사자": {"food": "고기 🥩 (주로 초식동물)", "img": "https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg"},
    "호랑이": {"food": "고기 🥩 (사슴, 멧돼지 등)", "img": "https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg"},
    "표범": {"food": "고기 🥩 (작은 포유류, 새)", "img": "https://upload.wikimedia.org/wikipedia/commons/0/0f/African_leopard.jpg"},
    "치타": {"food": "고기 🥩 (가젤, 토끼 등)", "img": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Cheetah4.jpg"},
    "늑대": {"food": "고기 🥩 (사냥한 동물)", "img": "https://upload.wikimedia.org/wikipedia/commons/0/06/Canis_lupus_laying.jpg"},
    "여우": {"food": "잡식 🐭🍓 (작은 동물, 과일 등)", "img": "https://upload.wikimedia.org/wikipedia/commons/1/16/2010-british-red-fox.jpg"},
    "곰": {"food": "잡식 🐟🍯🍓 (연어, 꿀, 열매 등)", "img": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Brown_bear_in_forest.jpg"},
    "판다": {"food": "대나무 🎋", "img": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Grosser_Panda.JPG"},
    "코알라": {"food": "유칼립투스 잎 🍃", "img": "https://upload.wikimedia.org/wikipedia/commons/4/49/Koala_climbing_tree.jpg"},
    "코끼리": {"food": "풀 🌱, 나뭇잎 🍃, 과일 🍎", "img": "https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg"},
    "기린": {"food": "나뭇잎 🍃 (특히 아카시아)", "img": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Giraffe_standing.jpg"},
    "하마": {"food": "풀 🌱 (물속 식물 포함)", "img": "https://upload.wikimedia.org/wikipedia/commons/7/71/Hippo_in_water.jpg"},
    "고릴라": {"food": "풀 🌱, 과일 🍌", "img": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Male_gorilla_in_SF_zoo.jpg"},
    "원숭이": {"food": "과일 🍌, 곤충 🐛", "img": "https://upload.wikimedia.org/wikipedia/commons/b/b1/Macaca_mulatta_in_Guiyang.jpg"},
    "침팬지": {"food": "과일 🍌, 곤충 🐛, 작은 동물 🐭", "img": "https://upload.wikimedia.org/wikipedia/commons/2/27/Schimpanse_Zoo_Leipzig.jpg"},
    "고슴도치": {"food": "곤충 🐛, 지렁이 🪱", "img": "https://upload.wikimedia.org/wikipedia/commons/5/5c/European_hedgehog.jpg"},
    "두더지": {"food": "지렁이 🪱, 곤충 🐛", "img": "https://upload.wikimedia.org/wikipedia/commons/0/0d/Talpa_europaea_MHNT.jpg"},
    "박쥐": {"food": "곤충 🦟 (과일박쥐는 과일 🍌)", "img": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Common_fruit_bat.jpg"},

    # 조류
    "독수리": {"food": "고기 🥩 (사체, 작은 동물)", "img": "https://upload.wikimedia.org/wikipedia/commons/1/19/Griffon_vulture_in_flight.jpg"},
    "부엉이": {"food": "작은 동물 🐭, 새 🐦", "img": "https://upload.wikimedia.org/wikipedia/commons/4/48/Eurasian_Eagle-Owl_RWD3.jpg"},
    "참새": {"food": "씨앗 🌾, 곤충 🐛", "img": "https://upload.wikimedia.org/wikipedia/commons/7/70/House_Sparrow_mar08.jpg"},
    "앵무새": {"food": "씨앗 🌾, 과일 🍎", "img": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Ara_ararauna_Luc_Viatour.jpg"},
    "펭귄": {"food": "물고기 🐟, 크릴 🦐", "img": "https://upload.wikimedia.org/wikipedia/commons/9/9b/Aptenodytes_forsteri_-Snow_Hill_Island%2C_Antarctica_-adults_and_juveniles-8.jpg"},

    # 해양 동물
    "돌고래": {"food": "물고기 🐟, 오징어 🦑", "img": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Dolphins_in_the_Red_Sea.jpg"},
    "상어": {"food": "물고기 🐟, 해양 포유류 🐋", "img": "https://upload.wikimedia.org/wikipedia/commons/5/56/White_shark.jpg"},
    "고래": {"food": "플랑크톤 🦠 (수염고래), 물고기 🐟 (일부)", "img": "https://upload.wikimedia.org/wikipedia/commons/7/73/Humpback_stellwagen_edit.jpg"},
    "문어": {"food": "갑각류 🦐, 조개 🦪, 물고기 🐟", "img": "https://upload.wikimedia.org/wikipedia/commons/5/57/Octopus2.jpg"},
    "거북이": {"food": "풀 🌱, 해조류 🌿 (일부 잡식)", "img": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Green_turtle_swimming_over_coral_reefs_in_Kona.jpg"},

    # 파충류 & 양서류
    "악어": {"food": "고기 🥩 (물가 동물)", "img": "https://upload.wikimedia.org/wikipedia/commons/6/6b/NileCrocodile.jpg"},
    "뱀": {"food": "작은 동물 🐭, 새 🐦, 개구리 🐸", "img": "https://upload.wikimedia.org/wikipedia/commons/6/62/Python_molurus_molurus.jpg"},
    "개구리": {"food": "곤충 🐛, 작은 절지동물 🦗", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Green_frog_in_pond.jpg"},

    # 곤충
    "벌": {"food": "꽃의 꿀 🍯, 꽃가루 🌸", "img": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Honeybee_on_purple_coneflower.jpg"},
    "개미": {"food": "잡식 🍞🪱 (설탕, 곤충, 식물 등)", "img": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Ant_Oecophylla_smargdina.jpg"},
    "무당벌레": {"food": "진딧물 🐛", "img": "https://upload.wikimedia.org/wikipedia/commons/4/41/Coccinella_septempunctata01.jpg"},
    "잠자리": {"food": "작은 곤충 🦟", "img": "https://upload.wikimedia.org/wikipedia/commons/3/38/Common_Darter_dragonfly.jpg"},
    "나비": {"food": "꽃꿀 🍯", "img": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Monarch_Butterfly_Danaus_plexippus_Male_2664px.jpg"},
    "메뚜기": {"food": "풀 🌱, 잎사귀 🍃", "img": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Locust.jpg"},
    "사마귀": {"food": "곤충 🦗, 작은 동물 🐭", "img": "https://upload.wikimedia.org/wikipedia/commons/4/43/Mantis_religiosa_3_Luc_Viatour.jpg"},
}

# Streamlit 앱
st.title("🐾 동물 먹이 & 이미지 검색기")
st.write("동물을 선택하면 주 먹이와 이미지를 확인할 수 있습니다!")

# selectbox 사용
animal_name = st.selectbox("동물을 선택하세요:", [""] + sorted(animal_data.keys()))

# 결과 출력
if animal_name:
    food = animal_data[animal_name]["food"]
    img_url = animal_data[animal_name]["img"]

    st.success(f"✅ {animal_name}의 주 먹이는 **{food}** 입니다!")
    st.image(img_url, caption=f"{animal_name}", use_column_width=True)
