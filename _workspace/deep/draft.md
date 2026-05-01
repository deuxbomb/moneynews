# ChatGPT도 DeepSeek도 무관하다 — 자율주행 트럭 상용화의 진짜 열쇠

> 🗓️ 2026년 5월 1일 | 머뉴 딥다이브

---

## AI 혁명의 한가운데서 나온 반직관적 발언

2026년, AI는 그 어느 때보다 빠르게 진화하고 있다. ChatGPT는 코드를 짜고, DeepSeek는 미국 빅테크를 긴장시켰고, Claude는 복잡한 추론을 해낸다. 그런데 자율주행 트럭 시장에서 가장 많은 주행 데이터를 보유한 기업의 CEO가 이런 말을 했다.

"LLM의 발전은 우리 배포 타임라인에 영향을 주지 않습니다. 상용화 목표는 여전히 2028년 중반입니다."

2026년 5월 1일, CNBC에 등장한 중국 자율주행 트럭 스타트업 Inceptio의 CEO Julian Ma의 발언이다. [CNBC](https://www.cnbc.com/2026/05/01/chinas-self-driving-truck-leaders-say-ai-breakthroughs-wont-accelerate-rollout-heres-why.html) AI 투자 열풍이 절정에 달한 시점에, 가장 현장에 가까운 사람이 정반대의 메시지를 던진 것이다.

이것이 단순한 겸손인지, 아니면 투자자들이 반드시 들어야 할 구조적 진실인지 — 오늘 파고든다.

---

## 50억 킬로미터라는 장벽, 그리고 '세계 모델'의 수학

이 역설을 이해하려면 자율주행 트럭이 실제로 어떻게 학습하는지를 알아야 한다.

일반 LLM은 인터넷에 있는 글과 코드를 학습한다. 텍스트는 무한히 복사할 수 있고, 스케일링 법칙에 따라 데이터가 많을수록 모델이 좋아진다. 그런데 자율주행 트럭의 '세계 모델'은 다르다. 고속도로에서 40톤 화물차가 마주치는 상황 — 갑작스러운 차선 변경, 짙은 안개, 도로 파손, 역주행 — 은 텍스트로 대체할 수 없다. **실제 바퀴가 도로를 굴러야** 데이터가 생긴다.

Inceptio가 제시한 수치가 이를 명확히 보여준다. 2026년 4월 기준 이 회사의 트럭들은 **7억 킬로미터**를 주행했다. 올해 말까지 10억 km를 목표로 한다. 그런데 L4 완전 자율주행 상용화에는 **50억 킬로미터**의 실주행 데이터가 필요하다고 한다. 세계 모델이 이 50억 km를 **500억 km의 가상 경험**으로 외삽해야 비로소 무인 트럭이 혼자 달릴 수 있는 수준에 도달한다는 것이다. [CNBC](https://www.cnbc.com/2026/05/01/chinas-self-driving-truck-leaders-say-ai-breakthroughs-wont-accelerate-rollout-heres-why.html)

숫자를 다시 보자. 현재 7억 → 목표 50억. 아직 **14%**도 채우지 못했다. AI 알고리즘이 아무리 좋아져도, 이 숫자는 물리적 시간의 함수다. 트럭이 도로를 달리는 속도보다 빠를 수 없다.

이것이 바로 Julian Ma의 발언이 의미하는 바다. ChatGPT가 더 똑똑해진다고 해서 이 7억이 8억이 되지는 않는다. 오직 트럭이 더 많이, 더 오래 달려야 한다.

---

## 28배 격차 — 중국이 데이터 전쟁에서 앞서고 있다

그렇다면 지금 누가 이 경쟁에서 앞서 있을까.

ARK Invest의 Big Ideas 2026 보고서가 적나라한 숫자를 보여준다. Inceptio의 누적 주행 거리는 약 **2억 5천만 마일(약 4억 km)**. 2위인 중국의 Pony.ai가 420만 마일, 미국 3개 기업(Aurora·Kodiak·Gatik)의 합산이 890만 마일이다. [CNBC](https://www.cnbc.com/2026/05/01/chinas-self-driving-truck-leaders-say-ai-breakthroughs-wont-accelerate-rollout-heres-why.html)

Inceptio가 미국 3사를 합쳐도 **28배**나 앞서 있다. 이 격차는 단순한 국가 경쟁이 아니다. 미래 AI 세계 모델의 기반이 되는 데이터 자산의 격차다.

물론 미국의 Aurora가 없는 건 아니다. Aurora는 2025년 4월 텍사스에서 상용 무인 운행을 개시한 이후 2026년 3월까지 **25만 마일 이상의 무사고 주행**을 기록했다. FedEx, Schneider, Hirschbach, Uber Freight와 함께 매일 화물을 실어나르고 있으며, 2026년 말까지 200대 이상의 트럭을 목표로 한다. [nationaltoday.com](https://nationaltoday.com/us/tx/dallas/news/2026/03/05/aurora-innovation-touts-250k-incident-free-driverless-miles-targets-200-trucks-in-2026/) 꾸준하고 진지한 전진이다. 하지만 Inceptio의 4억 km와 Aurora의 40만 km — 1,000배에 가까운 격차가 현실이다.

이 데이터 전쟁에서 앞선다는 것은 곧 세계 모델의 품질에서 앞선다는 뜻이다. 2028년 L4 상용화 경쟁에서 중국 기업들이 구조적으로 유리한 위치에 있다.

---

## 데이터만이 전부가 아니다 — 50년 된 삼각대 규정

AI와 데이터가 갖춰져도 트럭이 혼자 달리지 못하게 막는 게 있다. 규제다.

미국에서 자율주행 트럭 확산의 비기술적 최대 장벽 중 하나는 **50년 된 연방 규정**이다. 도로에서 트럭이 고장 나면 운전자가 직접 차에서 내려 10분 이내에 반사 삼각대를 설치해야 한다는 규정. 무인 트럭에는 구조적으로 불가능한 요건이다. [Automotive Fleet](https://www.automotive-fleet.com/10256891/2026-is-an-inflection-point-for-autonomy-if-policy-keeps-pace)

비슷한 규제 장벽이 곳곳에 있다. 미국은 연방 차원의 통일된 자율주행 정책이 없고, 캘리포니아·텍사스·애리조나 등 주별로 제각각이다. 다른 주를 가로지르는 장거리 화물 운송에서는 이 '규제 패치워크'가 치명적 장애물이 된다. AI가 아무리 완벽해도, 법이 허가하지 않으면 달릴 수 없다.

중국은 반대로 중앙집권적 규제 체계가 빠른 허가를 가능하게 한다. Inceptio가 ZTO Express에 400대를 납품하고 대규모 상업 운행을 할 수 있었던 배경에는 이런 규제 환경의 차이가 있다. [Yahoo Finance](https://finance.yahoo.com/news/china-inceptio-technology-delivers-400-105318794.html)

---

## 하드웨어 비용 전쟁 — 70% 절감의 의미

세 번째 병목은 하드웨어 비용이다. 라이다, 레이더, 카메라, 고성능 컴퓨팅 칩을 모두 탑재한 L4 트럭은 여전히 일반 트럭보다 훨씬 비싸다. 트럭이 1억 km를 아무리 달려도, 물류 기업이 경제적으로 도입할 수 없으면 상용화는 불가능하다.

여기서 눈에 띄는 숫자가 있다. Pony.ai가 2025년 11월 발표한 4세대 자율주행 트럭의 BOM(부품 비용)이 이전 세대 대비 **70% 절감**됐다는 것이다. [Pony.ai IR](https://ir.pony.ai/news-releases/news-release-details/pony-ai-inc-announces-gen-4-autonomous-trucks-set-mass) 2026년 천 대 단위 대량생산을 목표로 한다.

NVIDIA와 Plus AI의 접근도 이를 반영한다. Plus AI는 NVIDIA GTC 2026에서 발표한 SuperDrive 시스템에서 10억 파라미터 비전-언어-액션(VLA) 모델을 **0.5억 파라미터** 엣지 모델로 압축했다. 20배 경량화를 통해 자동차 등급 하드웨어에서 실시간 추론이 가능하게 한 것이다. International Motors와 함께 2027년 완전 무인 상용 운행을 목표로 한다. [autoconnectedcar.com](https://www.autoconnectedcar.com/2026/03/nvidia-autonomous-news-applied-intuition-deeproute-ai-tier-iv-isuzu-aeye-lyft-plusai-gatik-weride/)

이 세 개의 전선 — 데이터, 규제, 하드웨어 비용 — 이 동시에 해소될 때 비로소 자율주행 트럭의 진짜 상용화가 시작된다. AI 역량의 한계가 아니라, 이 세 가지 물리적 병목이 2028이라는 타임라인을 만들어낸 것이다.

---

## $NVDA·$TSLA·$AUR — 투자자가 진짜 봐야 할 지표

자율주행 트럭의 병목이 AI가 아니라 데이터·규제·비용이라면, 투자자는 무엇을 봐야 할까.

**$NVDA**: 데이터 병목의 최대 수혜자다. Alpamayo 기반 모델, DRIVE AGX Thor 플랫폼이 Inceptio·Plus AI·Mercedes-Benz 등 전방위에 공급된다. 자율주행 소프트웨어 시장이 2024년 18억 달러에서 2035년 70억 달러로 성장하는 과정에서 NVIDIA는 실리콘 공급자 포지션이다. [MarketsandMarkets](https://www.globenewswire.com/news-release/2026/04/29/3283912/0/en/Autonomous-Driving-Software-Market-worth-7-0-billion-in-2035-MarketsandMarkets.html) 핵심 지표: AV 칩 ASP(평균 판매가)와 DRIVE 플랫폼 채택 기업 수.

**$TSLA**: 가장 많은 실도로 주행 데이터를 가진 소비자 차량 기업이다. FSD 활성 구독자 128만 명, 전년 대비 51% 증가. [Tesla Q1 2026](https://www.cnbc.com/2026/04/22/tesla-tsla-q1-2026-earnings-report.html) Morgan Stanley는 마일당 비용을 $0.81로 추산해 Waymo($1.43)를 크게 밑돈다. 하지만 안전 데이터에서 Waymo 대비 열세다. 핵심 지표: FSD 구독 증가율과 감독 없는 FSD 주행 비율.

**$AUR (Aurora Innovation)**: 미국 L4 트럭 상용화의 현장 선두다. 무사고 25만 마일은 진지한 성과지만, 매출은 아직 수백만 달러 수준이다. 2026년 200대 목표 달성 여부와 안전 주행 마일 누적 속도가 핵심 지표다. 수익화까지 긴 길이 남아 있다.

세 종목 모두, AI 알고리즘의 발전보다 **실제 마일 누적 속도**와 **규제 승인 속도**를 봐야 한다. Inceptio CEO의 말을 뒤집어 읽으면: AI 역량보다 데이터를 더 빠르게 쌓는 기업이 이긴다.

---

## 머뉴's Advice

**① 자율주행 투자에서 "AI 발전 = 빠른 상용화" 등식을 버려라.** 실주행 데이터 누적량, 규제 허가 진척도, 하드웨어 BOM 감소율 — 이 세 가지가 진짜 이정표다. AI 능력 발표만 보고 들어가는 포지션은 타이밍 리스크가 크다.

**② $NVDA는 이 게임의 인프라 공급자다.** 중국이 이기든 미국이 이기든, L4 상용화 레이스에서 컴퓨팅 파워를 공급하는 건 NVIDIA다. 카지노를 짓는 것보다 카지노에 칩을 파는 게 더 안정적이다.

**③ 2028년을 달력에 표시해두자.** Inceptio가 50억 km 임계값에 도달하는 시점이 투자 타이밍의 신호탄이 된다. Aurora의 무사고 마일 100만 돌파도 주목할 이벤트다. AI 뉴스가 아니라 **킬로미터 카운터**가 당신의 투자 알람이어야 한다.

---

## 출처

- [CNBC](https://www.cnbc.com/2026/05/01/chinas-self-driving-truck-leaders-say-ai-breakthroughs-wont-accelerate-rollout-heres-why.html) — "China's self-driving truck leaders say AI breakthroughs won't accelerate rollout — here's why", 2026-05-01
- [nationaltoday.com](https://nationaltoday.com/us/tx/dallas/news/2026/03/05/aurora-innovation-touts-250k-incident-free-driverless-miles-targets-200-trucks-in-2026/) — "Aurora Innovation Touts 250K Incident-Free Driverless Miles, Targets 200+ Trucks in 2026", 2026-03-05
- [Pony.ai IR](https://ir.pony.ai/news-releases/news-release-details/pony-ai-inc-announces-gen-4-autonomous-trucks-set-mass) — "PONY AI Inc. Announces Gen-4 Autonomous Trucks, Set for Mass Production and Deployment in 2026", 2025-11-19
- [autoconnectedcar.com](https://www.autoconnectedcar.com/2026/03/nvidia-autonomous-news-applied-intuition-deeproute-ai-tier-iv-isuzu-aeye-lyft-plusai-gatik-weride/) — "NVIDIA Autonomous News: Applied Intuition, DeepRoute.ai, PlusAI, Gatik & WeRide", 2026-03
- [Yahoo Finance](https://finance.yahoo.com/news/china-inceptio-technology-delivers-400-105318794.html) — "China's Inceptio Technology delivers 400 autonomous trucks", 2024
- [Automotive Fleet](https://www.automotive-fleet.com/10256891/2026-is-an-inflection-point-for-autonomy-if-policy-keeps-pace) — "2026 Is an Inflection Point for Autonomy, If Policy Keeps Pace"
- [MarketsandMarkets / GlobeNewswire](https://www.globenewswire.com/news-release/2026/04/29/3283912/0/en/Autonomous-Driving-Software-Market-worth-7-0-billion-in-2035-MarketsandMarkets.html) — "Autonomous Driving Software Market worth $7.0 billion in 2035", 2026-04-29
- [CNBC](https://www.cnbc.com/2026/04/22/tesla-tsla-q1-2026-earnings-report.html) — "Tesla Q1 2026 earnings report", 2026-04-22
- [news.futunn.com](https://news.futunn.com/en/post/65942490/tesla-s-costs-are-40-lower-and-waymo-s-safety) — "Tesla's costs are 40% lower, and Waymo's safety is 7 times higher", 2026
