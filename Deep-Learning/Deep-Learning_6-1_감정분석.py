# 감정분석
# 정의 : 문서, 단락, 문장 안에서의 [긍정, 부정, 중립]을 감지하는 텍스트로 나누어 분석하는 것
# 사용 : 감정 데이터는 제품이나 서비스의 [의견, 평가, 태도]을 정량화 할 수 있다.
# 목적 : 새로운 제품과 서비스 개발 가능.
#        기존 제품과 서비스의 개선
#        우리 브랜드 편판의 개선

# 필요성 : 대량의 데터 처리 가능 - 직접 문서를 읽는 것 보다 빠르다.
#         추출의 일관성 - 감정을 지정한 텍스트로 분류해서 결과의 신뢰도가 높다.
#         실시간 분석 가능 - 제품이나 서비스의 편판을 빠르게 수집하고 반영할 수 있다.

# 활용 예시 : 브랜드 모니터링 - 뉴스나 게시글 등을 크롤링 해서 브랜드 이미지 반영
#            VOC(Voice of Customer) - 제품이나 서비스의 리뷰, 사용후기, 개인 게시 글, 설문조사 자료 수집해서 개선 및 잠재 고객 찾기

# 감정 분석 유형 : 1. 감정 탐지 - 좋다, 싫다, 별로 같은 단어로 인간의 감정을 탐지
#                              감정 사전 기반 분석 or 머신러닝, 딥러닝 알고리즘 사용
#                   문제점 - 문맥의 이해가 어려워 분석 자체에 오류 발생 EX)음식 맛이 1등이에요, 맛없는 순서로!

#                 2. 특성기반 감정 분석 - 텍스트 내에서 특성 기준으로 감정 분석
#                                       EX)음식 맛은 좋은데, 양이 적어요!  == 좋은데 / 적어요

# 감정분석법 3가지--------------------------------------------------------------
# Lexicon-based Approach    (감정 평가 사전이 필요)-------------------------------
# 정의 : 기존 완성된 감정 사전을 활용해 감정 평가.
#        우수한 감정 사전일 수 록 신뢰도가 높음.
# 문제점 : 단순하게 단어만으로는 감정 분석이 어렵다.
#         광범위한 사용 불가 - 도메인(국가, 지역, 직업)의 사용 용어가 다르면 사용불가 EX)서울말 사전은 부산말에 적용 불가.
#         데이터량 문제 - 한국어 사전의 데이터량이 적다.

# 감정 평가 사전의 생성 법 3가지
# 1. 전문가 레이블링 - 얻고자하는 도메인의 전문가들이 직접 읽고 긍정, 부정을 구분한 사전. 신뢰도가 높다.
# 2. 시장 데이터 사용 - 시장에 나온 공공 데이터를 활용 EX)한국은행 경제 연구원에서 발간하는 [BOK 경제 연구에 금리 인상, 금리 하락 사전이 사용 됨]
# 3. seed propagation - 단어의 유사성을 가지고 네트워크를 만들어, 단어간 가까우면 점수를 주어 사전을 만드는 것

# Machine Learning Approach (레이블링 된 데이터셋 필요)-------------------------------
# Naive Bayes 감정분석
#나이브 베이즈 분류기 활용 감정 분석 -감정 레이블이 부착된 학습 데이터에 '나이브 베이즈의 분류모델'을 사용해 감정분석
# 과정 : 새로운 데이터 - 분류모델 가동 - [사전확률 - 분유모델 - 사후확률 - 분류모델 - 사전확률] 반복~~
# 의사결정이나 확률을 구할 때 계속 업데이트 시키기 때문에 머신러닝, 인공지능 분야에 사용
# 사용 분야 : 스팸메일 분류

# Deep Learning Approach    (레이블링 된 데이터셋 필요)-------------------------------
# RNN 감정분석 : 시계열 데이터의 시간 흐름을 반영할 수 있는 모델
# 사용 : 이미지 캡셔닝, 기계번역 모델, 감정 분석 등 활용
# 한계점 : 문장이 길면 오류난다.
#         학습 과정에 단어에 부여된 가중치에 따라 오류가 난다.

#정의 끝





