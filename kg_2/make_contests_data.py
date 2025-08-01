import pandas as pd
import random
from datetime import datetime, timedelta

# 카테고리 매핑
category_map = {
    "기획/아이디어": 1,
    "광고/마케팅": 2,
    "사진/영상/UCC": 3,
    "디자인/순수미술/공예": 4,
    "네이밍/슬로건": 5,
    "캐릭터/만화/게임": 6,
    "건축/건설/인테리어": 7,
    "과학/공학": 8,
    "예체능/패션": 9,
    "전시/페스티벌": 10,
    "문학/시나리오": 11,
    "해외": 12,
    "학술": 13,
    "창업": 14,
    "기타": 15
}

hosts = ["한국디자인진흥원", "청년창업재단", "한국콘텐츠진흥원", "중소벤처기업부", "서울시", "문화체육관광부"]
biz_types = ["공공기관", "중소기업", "협회", "대기업", "지자체"]
targets = ["대학생", "청소년", "제한 없음", "청년", "직장인"]
benefits = ["상장 및 상금", "인턴 기회 제공", "전시 기회", "해외 연수", "취업 가산점"]
extras = ["우수작 홍보 지원", "멘토링 제공", "상품화 지원", "없음"]

def generate_random_date():
    start = datetime.today() + timedelta(days=random.randint(-10, 10))
    end = start + timedelta(days=random.randint(7, 30))
    return start.strftime('%Y.%m.%d'), end.strftime('%Y.%m.%d')

data = []
for i, (cat, cat_id) in enumerate(category_map.items(), start=1):
    for j in range(2):
        start_date, end_date = generate_random_date()
        dday = (datetime.strptime(end_date, '%Y.%m.%d') - datetime.today()).days
        row = {
            "제목": f"{datetime.today().year} {random.choice(hosts)} {cat} 공모전",
            "디데이": f"D-{dday}" if dday >= 0 else "마감",
            "포스터 이미지": f"poster_{i}_{j+1}.png",
            "주최": random.choice(hosts),
            "기업형태": random.choice(biz_types),
            "참여대상": random.choice(targets),
            "시상규모": f"{random.randint(300, 1000)}만 원",
            "시작일": start_date,
            "마감일": end_date,
            "홈페이지": "https://linkareer.com/activity/example",
            "활동혜택": random.choice(benefits),
            "공모분야": cat,
            "카테고리ID": cat_id,
            "추가혜택": random.choice(extras),
            "상세내용": f"{cat} 분야의 창의적인 아이디어를 가진 참가자를 모집합니다."
        }
        data.append(row)

df = pd.DataFrame(data)
output_path = "data/contests_data.xlsx"
df.to_excel(output_path, index=False)

output_path
