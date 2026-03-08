from dotenv import load_dotenv
load_dotenv()

from google import genai

client = genai.Client()

def calculate_calories(image_path):
    load_dotenv()
    client = genai.Client()

    MODEL_ID = "gemini-3-flash-preview"

    if not os.path.exists(image_path):
        print(f"[오류] 지정한 이미지 파일({image_path})울 찾을 수 없습니다")
        return

    print("이미지 데이터 전송중...")
    img_file = client.files.upload(file=image_path)

    prompt = (
        "당신은 정밀한 데이터 분석을 수행하는 영양학 전문가입니다."
        "첨부된 음식 사진을 기반으로 다음 정보를 냉철하고 객관적으로 분석하십시오. \n\n"
        "1. 구성 요소 식별: "
    )

    print("모델 분석 진행중...")
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[
            prompt,
            img_file
        ]
    )

    print("=" * 30)
    print("분석 결과 보고서")
    print("=" * 30)
    print(response.text)

calculate_calories("data\food_image.jpg")