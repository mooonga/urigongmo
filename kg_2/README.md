# 공모전 포털 & 자유게시판 웹 애플리케이션

> Django 기반의 공모전 등록 및 자유게시판 기능이 포함된 웹 애플리케이션 
> 공모전 정보를 등록하고, 포스터 이미지를 업로드하며, 디데이 계산 및 자유로운 의견 교환 가능

---

## 실행 방법

### 1. 프로젝트 클론 및 가상환경 설정

```bash
git clone https://github.com/foreverwon/kg_2
cd kg_2 #복제된 디렉터리로 이동

# 가상환경 생성 (최초 1회만)
python -m venv kg_2

# 가상환경 활성화 (매번 작업 시)
source kg_2/bin/activate       # macOS/Linux
kg_2\Scripts\activate          # Windows
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

- 메인 페이지: http://127.0.0.1:8000

- 공모전 리스트: http://127.0.0.1:8000/poster

- 공모전 상세 페이지 예시: http://127.0.0.1:8000/poster/1

- 자유게시판: http://127.0.0.1:8000/freeboard

- 마이페이지 (미구현): http://127.0.0.1:8000/mypage

- 공모전 관리: http://127.0.0.1:8000/contest/

- 관리자 페이지: http://127.0.0.1:8000/admin

## 📦 앱 별 기능 소개
### common (공통 사용자 인증)
- 사용자 회원가입 및 로그인
- 사용자 유형 구분: 일반 사용자 / 사업자 / 관리자
- 로그인 후 사용자 유형에 따른 리다이렉트 처리
- Django 기본 User 모델 확장 (role 필드 포함)

---

### contest (공모전 운영 기능)
#### [공통]
- 공모전 홈 페이지 제공 (`/contest/`)
- 접근 권한 없는 사용자 처리 (`permission_denied.html`)

#### [일반 사용자]
- 출품작 제출: `/contest/user/entry/upload/`
- 내가 제출한 출품작 목록 확인: `/contest/user/entry/list/`

#### [사업자]
- 공모전 등록: `/contest/business/contest/register/`
- 내가 등록한 공모전 목록 확인: `/contest/business/contest/list/`
- 출품작 평가 (기획력/창의성/실현 가능성/완성도 기준):  
  `/contest/business/entry/<entry_id>/score/`

---

### `poster` (공모전 정보/포스터 관리)
- 포스터 이미지와 함께 공모전 요약 정보 표시
- 공모전 D-DAY 자동 계산 기능
- Excel 또는 크롤러 기반 자동 등록 기능 지원
- 이미지 업로드 및 저장 경로 자동 관리

---

### `freeboard` (자유게시판)
- 게시글 작성 / 수정 / 삭제 기능
- 댓글 작성 / 삭제 기능
- 최신 글 순 정렬 및 게시글 상세 페이지 제공

---

## 추가해야할 부분
### 마이페이지
- 로그인/회원가입 기능
### 템플릿 합치기