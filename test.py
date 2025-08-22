
import streamlit as st

# 동물별 주 먹이 사전
animal_foods = {
    "사자": "고기 (주로 초식동물)",
    "호랑이": "고기 (사슴, 멧돼지 등)",
    "코끼리": "풀, 나뭇잎, 과일",
    "기린": "나뭇잎 (특히 아카시아)",
    "판다": "대나무",
    "토끼": "풀, 당근, 채소",
    "늑대": "고기 (사냥한 동물)",
    "곰": "잡식 (연어, 꿀, 열매 등)",
    "닭": "곡식, 곤충, 벌레",
    "고양이": "고기 (작은 동물, 생선 등)",
    "강아지": "잡식 (사료, 고기 등)"
}

# Streamlit 앱
st.title("🐾 동물 먹이 검색기")
st.write("동물 이름을 입력하면 그 동물의 주 먹이를 알려드립니다!")

# 사용자 입력
animal_name = st.text_input("동물 이름을 입력하세요:")

# 결과 출력
if animal_name:
    food = animal_foods.get(animal_name)
    if food:
        st.success(f"✅ {animal_name}의 주 먹이는 **{food}** 입니다!")
    else:
        st.warning(f"❌ '{animal_name}'의 정보를 찾을 수 없습니다. 다른 동물을 입력해보세요.")
