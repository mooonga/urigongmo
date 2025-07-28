# 공모전 포털 & 자유게시판 웹 애플리케이션

> Django 기반의 공모전 등록 및 자유게시판 기능이 포함된 웹 애플리케이션입니다.  
> 공모전 정보를 등록하고, 포스터 이미지를 업로드하며, 디데이 계산 및 자유로운 의견 교환이 가능합니다.

---

## 실행 방법

### 1. 프로젝트 클론 및 가상환경 설정

```bash
git clone https://github.com/yourname/contest-portal.git
cd contest-portal

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # (Windows는 venv\Scripts\activate)'''
```

### 2. 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. 마이그레이션 및 초기 데이터 세팅
```bash
python manage.py migrate
python manage.py loaddata data/admin_user.json
python manage.py loaddata data/initial_data.json'''
```

### 4. 서버 실행
```bash
python manage.py runserver
```
→ 브라우저 접속: http://127.0.0.1:8000
→ 브라우저 접속: http://127.0.0.1:8000/poster
→ 관리자 페이지: http://127.0.0.1:8000/poster/detail
→ 관리자 페이지: http://127.0.0.1:8000/admin