# eda-repo-2 : 서울시내 아이를 키우기 가장 좋은 자치구 추천 서비스 (TEAM : I.GU)

> #### 기간 2025.03.24~2025.03.28

## Contents
1. Introduction
2. Responsibility
3. Design
4. Lay Out
5. EDA
6. Service
## 1. Introduction
### Subject
|**주제**|서울시에서 아이를 키우기 가장 좋은 자치구는 어디일까?|
|---|------------------------------|
|**배경**|서울에서 아이 키우기 좋은 자치구를 다룬 기사마다 1위가 다르게 선정되는 이유는 평가 기준이 제각각이기 때문입니다. 어떤 곳은 보육시설을, 어떤 곳은 교육 환경이나 주거 여건을 중점적으로 평가합니다. 이에 우리는 단순한 주관적 평가가 아닌, 크게 교육 인프라, 안전성, 공공시설 접근성 3가지 요소 종합적으로 고려한 객관적인 평가 지표를 만들고, 데이터를 기반으로 실질적으로 가장 육아 친화적인 자치구를 선정하고자 본 프로젝트를 시작했습니다.|

### 1.1 Technicals
|**분류**|**기술**|
|----|---------------------------|
|**개발환경**|![linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)|
|**언어**|![python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)|
|**데이터베이스**|![mysql](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white) ![aws](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)|
|**협업툴**|![confluence](https://img.shields.io/badge/confluence-%23172BF4.svg?style=for-the-badge&logo=confluence&logoColor=white) ![jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=Jira&logoColor=white) ![slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white) ![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)|

## 2. Responsibility
||**이름**|**역할**|
|--|---|---------------------------------|
|팀장|**김채연**|DB설계, 주소 데이터 수집, 공원 데이터 수집 및 시각화, 발표|
|팀원|**이건우**|의료시설 데이터 수집 및 시각화, 발표|
|팀원|**이동훈**|교육분야 데이터 수집 및 시각화, 서비스 코드 작성, 발표|
|팀원|**서동진**|안전분야 데이터 수집 및 시각화, 발표|


## 3. Design

### 3.1 Detailed Plan
1. 평가 지표 기준 정하기 &rarr; 교육, 안전, 공공시설
2. 교육 &rarr; 학교, 학원 데이터 + 진학률 상관관계 분석
3. 안전 &rarr; 범죄, 사고, 유흥시설 분석
4. 공공시설 &rarr; 생활인구 대비 공공시설(도서관,공원) 분석
5. 의료 &rarr; 생활인구 대비 소아과 비율 분석
6. 주거비 &rarr; 주거지 유형 별 가격대 분석

### 3.2 User Requirements
|**No.**|**요구사항**|**중요도**|
|----|----------------------------------------------|--|
|**UR1**|어느 자치구가 안전한 자치구인지 분석해 판별할 수 있어야한다.||
|**UR1_01**|발생한 범죄에서 사용자가 선택한 범죄율 조회 및 낮을 곳을 알 수 있어야한다.||
|**UR1_02**|외국인(한국 국적을 가지지 않은 자)수를 알 수 있고 그에 따른 범죄율을 알 수 있어야한다.||
|**UR1_03**|학교 주변 및 학생관련 시설 주변에 문제가 없는 곳인지 알 수 있어야한다.||
||||
|**UR2**|어느 자치구가 교육수준 면에서 높은 자치구인지 분석해 판별할 수 있어야한다.||
|**UR2_01**|초등,중등,고등학교 수를 분석하여 어느 자치구에 학교 비율이 많은지 판별할 수 있어야한다.||
|**UR2_02**|생활인구 중 학생인구 별 진학률을 분석하여 학생들의 교육 수준을 알 수 있어야한다.||
||||
|**UR3**|어느 자치구가 주변환경 및 시설의 질이 좋은지 분석해 판별할 수 있어야한다.||
|**UR3_01**|의료 시설의 수 및 소아과 비율이 높은 곳이 어딘지, 또한 의료 서비스가 잘 제공되고 있는 곳인지 알 수 있어야한다.||
|**UR3_02**|주변환경이 깨끗한 곳인지, 대기환경이 좋다던가 또는 소음공해가 적은 곳이 어딘지 분석해 판별할 수 있어야한다.||
|**UR3_03**|공용 복지시설(도서관, 공원)의 수나 사용률 또는 시설의 관리정도가 뛰어난 곳이 어딘지 알 수 있어야한다.||
||||
|**UR4**|조건에 맞는 자치구 중 주거비가 가장 낮은 곳이 어딘지 알 수 있어야한다.||

## 4. Lay Out

### 4.1 System Requirements
|**No.**|**기능이름**|**요구 데이터**|**수집 가능 여부**|**테이블명**|   |
|----|--------|----------|--------|--------|----|
|**SR_01**|교육 평가 지표|학교 데이터|   |school||
|||학원 데이터|   |academy||
|||도서관 데이터|   |learning_space||
|||진학률 데이터|   |university||
|**SR_02**|안전 평가 지표|범죄율 데이터|   |crime||
|||유흥 시설 데이터|   |unhealthy_facility||
|||교통 사고 데이터|   |traffic_accident||
|**SR_03**|의료 평가 지표|의료 시설 데이터|   |hospital||
|||소아과 데이터|   |hospital||
|SR_04|주거비 평가 지표|주거비 데이터|   |real_estate||

### 4.2 ER Diagram
>![Image](https://github.com/user-attachments/assets/fc336828-b3b1-4fc5-81cb-1cfef415093c)

#### (1) 주소 테이블
* 동 테이블과 도로 테이블이 구 테이블의 id를 참조

#### (2) 교육 지표 테이블
* 구 테이블의 id 참조

#### (3) 안전 지표 테이블
* 구 테이블의 id 참조

#### (4)공공시설 지표 테이블
* 구 테이블의 id 참조
* 병원 테이블은 동 테이블과 도로 테이블의 id 참조

#### (5) 서비스 테이블
* 구와 동의 순위를 매기기 위한 테이블
* 구, 동 테이블의 id를 참조


## 5. Exploratory Data Analysis (EDA)

### 5.1 교육
#### (1) 자치구별 학생 수 대비 학교 수
#### (2) 자치구별 학생 수 대비 입시학원 수
#### (3) 교육 지표 자치구 순위

### 5.2 안전
#### (1) 자치구별 면적 대비 범죄 발생 건수
#### (2) 자치구별 생활인구 대비 교통사고 발생 건수
#### (3) 자치구별 면적 대비 유흥시설 수
#### (4) 안전 지표 자치구 순위

### 5.3 공공시설
#### (1) 소아과 밀집도
#### (2) 병원 밀집도 대비 소아과 밀집도
#### (3) 생활인구 대비 도서관 수
#### (4) 1인당 공원 면적
#### (5) 전체 면적 대비 1인당 공원 면적 경향성과 오차
#### (6) 공공시설 지표 자치구 순위

### 5.4 종합 분석 및 시각화
#### (1) 종합 지표 자치구 순위

### 5.5 서비스위한 동 단위로의 범위 축소
#### (1) 성동구에서 면적 대비 월세가 가장 저렴한 법정동

## 6. Service

### 6.1 User Flow Chart
>![Image](https://github.com/user-attachments/assets/8f8698d7-27dd-4bdf-b4e4-769421f2eba4)

### 6.2 서비스 구동



   
