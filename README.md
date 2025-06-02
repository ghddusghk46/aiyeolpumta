# AI 열품타

## 📌 주요 기능
- ⏱️ 공부 시간 타이머 기록
- 📋 목표 달성률 기반 피드백 (Rule-based)
- 🧠 KMeans 기반 공부 스타일 자동 분류 (AI 기능)
- ✅ 사용자별 투두리스트
- 📊 앱 내 공부 현황 시각화

## 🛠️ 사용 기술
- Python 3.12.7
- Django 4.2.7
- scikit-learn (AI 클러스터링)
- pandas, joblib, gunicorn, whitenoise
- GitHub 협업 (각자 브랜치 → PR 병합)

## 처음 실행 방법 
📦 1. Python 3.10.12 설치
⬇ CMD(명령 프롬프트)에 아래 명령어 복사해서 붙여넣기

curl -o python-3.10.12-amd64.exe https://www.python.org/ftp/python/3.10.12/python-3.10.12-amd64.exe

🔧 설치 시 주의사항
설치창에서 반드시 ✅ "Add Python 3.10 to PATH" 체크

그대로 "Install Now" 클릭

📁 2. GitHub에서 프로젝트 클론

git clone https://github.com/ghddusghk46/aiyeolpumta.git

cd aiyeolpumta

🛠️ 3. 가상환경 생성 및 실행

python -m venv venv

venv\Scripts\activate     # (Mac은 source venv/bin/activate)

→ 터미널에 (venv) 표시가 뜨면 성공

📦 4. 필요한 라이브러리 설치

pip install -r requirements.txt

→ Django, pandas, scikit-learn 등 자동 설치됨

🚀 5. 서버 실행

python manage.py runserver

→ 웹 브라우저에 아래 주소 입력:

http://127.0.0.1:8000

✅ 확인사항
항목	기대 결과
python --version	→ Python 3.10.12
가상환경 활성화됨	→ (venv) 표시됨
접속 확인	→ 로컬서버에 Django 페이지 나옴

## 변경 사항 커밋 방법 (브랜치 만든 후 처음 기준)
# [1] github에서 최신 변경사항 받아오기
git pull origin main

# [2] 내 작업 시작 (vscode 내에서 파일 변경 등)

# [3] 변경된 파일 git에 등록
git add .

# [4] 변경한 내용 설명과 함께 커밋
git commit -m "변경한 내용 설명 예: 로그인 페이지 추가"

# [5] 내 브랜치에 푸시 (처음 push일 경우)
git push --set-upstream origin feature/본인 이름 (지원: jiwon, 가영: gayeong)

# [6] 위에서 push 오류가 날 때
git pull origin main --rebase  # main의 최신 커밋을 내 브랜치에 재정렬

# [7] 다시 푸시 시도
git push origin feature/login

# [8] (rebase 중 충돌 수정 후) 다시 add
git add .

# [9] rebase 재개
git rebase --continue

# [10] 최종 푸시
git push origin feature/login


## 이후에 커밋 방법 
# 1. github에서 최신 main 내용 받아오기
git pull origin main

# 2. 작업 후
git add .

# 3. 커밋
git commit -m "로그인 폼 레이아웃 수정"

# 4. 푸시 (처음이 아니므로 짧게)
git push


## 브랜치 확인하기 (내가 지금 어떤 브랜치에 있는지)
git branch -vv
-> 출력 예시: feature/login ~!#@~!#~

# 나중에 실행할 때


venv\Scripts\activate # (venv) 표시가 앞에 뜨면 성공

# mac이나 리눅스는 아래처럼 입력
cd ~/ai열품타

source venv/bin/activate

python3 manage.py runserver



# 이후 bash에서 뜨는 링크 컨트롤+클릭 후 서버 주소 뒤에 + / 자기 페이지 이름 추가해서 실행하세요
