# 공모전 포털 & 자유게시판 웹 애플리케이션

> Django 기반의 공모전 등록 및 자유게시판 기능이 포함된 웹 애플리케이션 
> 공모전 정보를 등록하고, 포스터 이미지를 업로드하며, 디데이 계산 및 자유로운 의견 교환 가능

---

## 실행 방법

### 1. 프로젝트 클론 및 가상환경 설정

```bash
git clone https://github.com/foreverwon/kg_2
cd contest-portal

# 가상환경 생성 (최초 1회만)
python -m venv kg_2

# 가상환경 활성화 (매번 작업 시)
source kg_2/bin/activate  # Windows: kg_2\Scripts\activate
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

## contest 앱 소개

공모전 플랫폼을 구성하는 핵심 앱  
사용자 유형에 따라 사용할 수 있는 기능이 달라지며, 공모전 등록, 출품, 심사 등 다양한 역할을 처리가능

---

## 사용자 유형 및 기능

### 1. 일반 사용자 (`user`)
- 공모전 목록 조회 (`contest_list`)
- 출품작 등록 및 제출 (Entry 기능)
- 일반 심사 참여 (Score 모델의 `score_type='user'`)
- 심사 항목: 기획력, 창의성, 실현가능성, 완성도

#### 제한:
- 공모전 등록 불가
- 사업자 심사 불가

---

### 2. 사업자 (`business`)
- 공모전 등록 (`register_contest`)
- 등록 시 상태는 기본적으로 `대기중`으로 설정됨
- 제출된 출품작 목록 조회 및 심사 참여 (`score_type='business'`)
- 상태 변경 가능 (모집중 → 심사중 → 종료 등)

#### 제한:
- 출품작 제출 불가

---

### 3. 심사위원 (또는 등록된 사용자 중 역할 분리 가능)
- 출품작 심사 기능 가능
- 점수는 `Score` 모델에 저장
- 항목: 기획력, 창의성, 실현가능성, 완성도
- `score_type`에 따라 일반/사업자 심사 구분 가능

---

## 관련 모델 요약


`Contest` : 공모전 정보 (주최자, 상태, 등록일 등)
`Entry` : 출품작 정보 (공모전에 소속됨)
`Score` : 심사 점수 저장 (심사자, 출품작, 항목별 점수, 심사 유형)

---

## 사용자 흐름 예시

- 일반 사용자 : 로그인 → 공모전 목록 → 출품작 등록 → 일반 심사 참여
- 사업자 : 로그인 → 공모전 등록 → 출품작 확인 → 심사 점수 입력
