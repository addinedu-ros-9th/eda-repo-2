# eda-repo-2 : 서울시내 아이를 키우기 가장 좋은 자치구 추천 서비스 (TEAM : I.GU)

## 목차
1. Introduction
2. Responsibility
3. Plan

## Introduction
### Subject
|주제|서울시내에서 아이를 키우기 가장 좋은 자치구는 어디일까?|
|---|-------------------------------|
|:배경:|(주제 선정 배경)|

### Technicals
|:분류:|:기술:|
|----|---------------------------|
|개발환경|![linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)|
|언어|![python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)|
|데이터베이스|![mysql](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white) ![aws](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)|
|협업툴|![confluence](https://img.shields.io/badge/confluence-%23172BF4.svg?style=for-the-badge&logo=confluence&logoColor=white) ![jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=Jira&logoColor=white) ![slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white) ![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)|

## Responsibility
||:이름:|:역할:|
|--|---|---------------------------------|
|틴방|김채연||
|팀원|이동훈|교육분야 데이터 수집 및 시각화, 서비스 코드 작성, 발표|
|팀원|서동진||
|팀원|서건우||

## Design

### Detailed Plan
1. 평가 지표 기준 정하기 -> 교육, 안전, 공공시설
2. 교육 -> 학교, 학원 데이터 + 진학률 상관관계 분석
3. 안전 -> 범죄, 사고, 유흥시설 분석
4. 공공시설 -> 생활인구 대비 공공시설(도서관,공원) 분석
5. 의료 -> 생활인구 대비 소아과 비율 분석
6. 주거비 -> 주거지 유형 별 가격대 분석

### User Requirements
|:No.:|:요구사항:|:중요도:|
|----|----------------------------------------------|--|
|UR1|어느 자치구가 안전한 자치구인지 분석해 판별할 수 있어야한다.||
|UR1_01|발생한 범죄에서 사용자가 선택한 범죄율 조회 및 낮을 곳을 알 수 있어야한다.||
|UR1_02|외국인(한국 국적을 가지지 않은 자)수를 알 수 있고 그에 따른 범죄율을 알 수 있어야한다.||
|UR1_03|학교 주변 및 학생관련 시설 주변에 문제가 없는 곳인지 알 수 있어야한다.||
||||
|UR2|어느 자치구가 교육수준 면에서 높은 자치구인지 분석해 판별할 수 있어야한다.||
|UR2_01|초등,중등,고등학교 수를 분석하여 어느 자치구에 학교 비율이 많은지 판별할 수 있어야한다.||
|UR2_02|생활인구 중 학생인구 별 진학률을 분석하여 학생들의 교육 수준을 알 수 있어야한다.||
||||
|UR3|어느 자치구가 주변환경 및 시설의 질이 좋은지 분석해 판별할 수 있어야한다.||
|UR3_01|의료 시설의 수 및 소아과 비율이 높은 곳이 어딘지, 또한 의료 서비스가 잘 제공되고 있는 곳인지 알 수 있어야한다.||
|UR3_02|주변환경이 깨끗한 곳인지, 대기환경이 좋다던가 또는 소음공해가 적은 곳이 어딘지 분석해 판별할 수 있어야한다.||
|UR3_03|공용 복지시설(도서관, 공원)의 수나 사용률 또는 시설의 관리정도가 뛰어난 곳이 어딘지 알 수 있어야한다.||
||||
|UR4|조건에 맞는 자치구 중 주거비가 가장 낮은 곳이 어딘지 알 수 있어야한다.||

## Lay Out

### System Requirements
|:No.:|:기능이름:|:요구 데이터:|:수집 가능 여부:|:테이블명:||
|----|--------|----------|--------|--------|----|
|SR_01|교육 평가 지표|학교 데이터|   |school||
|||학원 데이터|   |academy||
|||도서관 데이터|   |learning_space||
|||진학률 데이터|   |university||
|SR_02|안전 평가 지표|범죄율 데이터|   |crime||
|||유흥 시설 데이터|   |unhealthy_facility||
|||교통 사고 데이터|   |traffic_accident||
|SR_03|의료 평가 지표|의료 시설 데이터|   |hospital||
|||소아과 데이터|   |hospital||
|SR_04|주거비 평가 지표|주거비 데이터|   |real_estate||

### ER Diagram

## Service

### User Flow Chart




   
