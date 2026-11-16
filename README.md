# 머신러닝 학습 웹앱

## Windows / Anaconda에서 시작

1. ZIP을 모두 압축 해제합니다. ZIP 안에서 직접 실행하지 마세요.
2. Anaconda PowerShell Prompt를 엽니다.
3. 아래 순서로 실행합니다. 경로는 압축을 푼 폴더로 바꿉니다.

```powershell
conda activate mynewproject
cd "C:\Users\carat\OneDrive\바탕 화면\iris_streamlit_app"
python -m pip install -r requirements.txt
python -m streamlit run run.py
```

기존 환경이 없다면 먼저 `conda create -n mynewproject python=3.10`으로 만드세요.
Python 3.10 이상을 사용하세요. 검증 환경: Python 3.12.
설치 후에는 환경을 켜고 이 폴더로 이동한 다음 `start_windows.bat`을 실행해도 됩니다.
브라우저가 자동으로 열리지 않으면 터미널의 Local URL을 여세요.
사용 중에는 터미널을 켜둡니다. 종료는 Ctrl+C입니다.

## 파일 구성

- run.py: 첨부 원본을 바이트 단위로 보존한 실행파일
- data.csv, ml.txt: 첨부 원본 부속 파일
- pages/0_머신러닝의개념.py: 마크다운, 반응형 CSS, 학습 방식·윤리·SVM 설명
- pages/1_머신러닝사례.py: 9개 사례, 분야 필터, 입력·출력·주의점, 성찰 활동
- pages/2_머신러닝시뮬레이터.py: 네 특징 입력, SVM 예측, 평가, 산점도와 기록
- iris_model.py: 학습·평가 분리와 표준화/SVM 파이프라인
- ui.py: 학습 페이지 공통 디자인
- .streamlit/config.toml: 테마 설정
- requirements.txt: 필요한 라이브러리 버전
- start_windows.bat: 실행 위치를 이 폴더로 맞추는 실행 도우미

pages 폴더와 각 파일의 위치를 유지하세요. 홈페이지에서 `ml.txt`를 상대 경로로
읽는 원본 동작을 보존하기 위해 반드시 run.py가 있는 폴더에서 실행해야 합니다.
기존 프로젝트에 적용할 때는 새 패키지 전체를 별도 폴더에 풀어 실행하는 것이 간단합니다.
원본 홈페이지에는 외부 YouTube 영상이 있어 재생에 인터넷이 필요합니다.
새 학습 페이지는 외부 폰트·이미지·데이터 다운로드 없이 동작하며, Iris 데이터는
scikit-learn에 포함되어 있습니다. 예측 기록은 현재 브라우저 세션에서 최근 20회 보관합니다.

## 수업에서 사용하기

왼쪽 메뉴: 머신러닝의개념 → 머신러닝사례 → 머신러닝시뮬레이터.
시뮬레이터에서 네 값(cm)을 입력하고 ‘붓꽃의 종 예측하기’를 누릅니다.
setosa / versicolor / virginica 중 하나를 출력합니다. 이것은 씨앗의 형태를
분석하는 모델이 아니라 꽃받침·꽃잎 측정으로 붓꽃의 종을 분류하는 모델입니다.

학습 120개 / 평가 30개, 층화 분리, random_state=42.
StandardScaler → SVC(kernel='rbf', C=1.0, gamma='scale').
표준화와 학습에는 학습 데이터만 사용합니다. 평가는 동일 모델의 미관측 30개 결과입니다.
평가 정확도는 개별 입력의 정답 확률을 의미하지 않습니다.
입력의 UI 범위는 0.1~20.0cm이며 관측 범위 밖의 값에는 경고를 표시합니다.
예시값은 실제 데이터의 행이므로 독립적인 성능 검증에 사용하지 마세요.

## 참고 자료

- https://scikit-learn.org/stable/getting_started.html
- https://scikit-learn.org/stable/common_pitfalls.html
- https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
- https://scikit-learn.org/stable/modules/svm.html
- https://docs.streamlit.io/get-started/installation/anaconda-distribution

## 검증 결과

- 원본 run.py 바이트 비교 일치(SHA-256: 5a6d8f4e7a47d60fb801fe4442b0595c022dfe2a52db683c906b9b983c79c0f5)
- Streamlit AppTest로 홈페이지와 세 페이지 실행 및 페이지 전환 확인
- 세 종의 예시 입력 각각 예측 확인
- 관측 범위 밖 입력의 경고 및 예측 기록 확인
- 학습/평가 인덱스 분리, 표준화 학습 샘플 수 120 확인
- 고정 평가 집합 30개 중 29개 정답(96.7%)
- 외부 YouTube의 실제 재생 가능 여부는 네트워크와 영상 제공자 정책에 따라 달라집니다.
