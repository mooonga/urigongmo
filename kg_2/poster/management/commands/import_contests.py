import pandas as pd
from poster.models import Poster
import os
from django.core.files import File
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Load contests from Excel"

    def handle(self, *args, **kwargs):
        #1. 엑셀 불러오기
        df = pd.read_excel("data/contests_data.xlsx")

        #2. 컬럼명 변경 (엑셀 → 모델 필드명)
        df.rename(columns={
            "제목": "title",
            "디데이": "d_day",
            "포스터 이미지": "image",
            "주최": "organization",
            "기업형태": "company_type",
            "참여대상": "target",
            "시상규모": "prize",
            "시작일": "start_date",
            "마감일": "end_date",
            "홈페이지": "website",
            "활동혜택": "benefits",
            "공모분야": "category",
            "추가혜택": "extra",
            "상세내용": "description",
            "카테고리ID": "category_id"
        }, inplace=True)

        #3. 각 행을 Poster 모델에 저장
        for _, row in df.iterrows():
            image_path = os.path.join("media", "poster_images", row["image"])
            if os.path.exists(image_path):
                with open(image_path, 'rb') as img_file:
                    poster = Poster(
                        title=row["title"],
                        d_day=row["d_day"],
                        organization=row["organization"],
                        company_type=row["company_type"],
                        target=row["target"],
                        prize=row["prize"],
                        start_date=pd.to_datetime(row["start_date"]),
                        end_date=pd.to_datetime(row["end_date"]),
                        website=row["website"],
                        benefits=row["benefits"],
                        category=row["category"],
                        category_id=row["category_id"],
                        extra=row["extra"],
                        description=row["description"],
                    )
                    poster.image.save(row["image"], File(img_file), save=True)
