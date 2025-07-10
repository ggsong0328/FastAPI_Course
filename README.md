# FastAPI 소셜 미디어 API

이 프로젝트는 FastAPI를 사용하여 구축된 간단한 소셜 미디어 애플리케이션의 백엔드 API입니다. 사용자 인증, 게시물 생성/읽기/업데이트/삭제(CRUD), 투표 기능을 제공합니다.

## 주요 기능

- JWT 토큰 기반의 사용자 인증 (로그인)
- 사용자 생성 및 정보 조회
- 게시물 CRUD 기능
- 게시물에 대한 투표 (좋아요/싫어요)

## 기술 스택

- **프레임워크**: FastAPI
- **데이터베이스**: PostgreSQL
- **ORM**: SQLAlchemy
- **데이터베이스 마이그레이션**: Alembic
- **데이터 유효성 검사**: Pydantic
- **테스팅**: Pytest
- **컨테이너화**: Docker, Docker Compose

## 프로젝트 설정 및 실행

### 1. 저장소 복제

```bash
git clone <repository-url>
cd fastapi
```

### 2. 가상 환경 생성 및 활성화

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate  # Windows
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

### 4. 환경 변수 설정

프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 아래와 같이 데이터베이스 설정을 추가합니다.

```
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=your_password
DATABASE_NAME=fastapi
DATABASE_USERNAME=postgres
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. 데이터베이스 마이그레이션

Alembic을 사용하여 데이터베이스 스키마를 최신 상태로 업데이트합니다.

```bash
alembic upgrade head
```

### 6. 애플리케이션 실행

Uvicorn을 사용하여 개발 서버를 실행합니다.

```bash
uvicorn app.main:app --reload
```

## 테스트 실행

Pytest를 사용하여 자동화된 테스트를 실행합니다.

```bash
pytest
```

## Docker를 이용한 실행

Docker Compose를 사용하여 개발 및 프로덕션 환경을 실행할 수 있습니다.

**개발 환경:**

```bash
docker-compose -f docker-compose-dev.yml up -d --build
```

**프로덕션 환경:**

```bash
docker-compose -f docker-compose-prod.yml up -d --build
```

## API 엔드포인트

- **인증 (`/auth`)**:
  - `POST /login`: 사용자 로그인 및 JWT 토큰 발급
- **사용자 (`/users`)**:
  - `POST /`: 새로운 사용자 생성
  - `GET /{id}`: 특정 사용자 정보 조회
- **게시물 (`/posts`)**:
  - `GET /`: 모든 게시물 조회
  - `POST /`: 새로운 게시물 생성
  - `GET /{id}`: 특정 게시물 조회
  - `DELETE /{id}`: 게시물 삭제
  - `PUT /{id}`: 게시물 수정
- **투표 (`/vote`)**:
  - `POST /`: 게시물에 투표
