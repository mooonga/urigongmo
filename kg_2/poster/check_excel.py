import pandas as pd
import os
from django.conf import settings

# BASE_DIR/data/posters.xlsx 위치를 기반으로 경로 설정
excel_path = os.path.join(settings.BASE_DIR, 'data', 'posters.xlsx')

# 엑셀 파일 읽기
df = pd.read_excel(excel_path)

# 데이터 확인용 출력
print(df.columns)
print(df.head())
