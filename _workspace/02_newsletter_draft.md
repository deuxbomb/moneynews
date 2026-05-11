# 당신의 Claude와 ChatGPT를 돌리는 칩은 이제 NVIDIA가 아니다 — ASIC 슈퍼사이클의 서막

**2026-05-11 | 테마: AI 인프라/반도체 | 유형: 📡 테크 트렌드**

---

## 🎬 1. 이야기: Midjourney가 서버실 이사를 결정한 날

2026년 봄, 이미지 생성 AI 스타트업 Midjourney는 조용한 결정을 내렸다. 수백만 달러짜리 NVIDIA GPU 서버에서 Google의 TPU 클라우드로 워크로드를 이전한 것이다. 이유는 단 하나 — 월 비용이 **$210만에서 $70만으로 65% 줄었다**.

이 한 줄의 숫자가 2026년 AI 반도체 시장에서 일어나고 있는 조용한 혁명을 압축한다.

2022년 11월, ChatGPT가 세상을 뒤흔들던 그 순간부터 NVIDIA는 AI 인프라의 절대 권력자였다. H100 GPU는 리스트 가격만 수만 달러를 호가해도 순식간에 매진됐다. 빅테크는 앞다퉈 'NVIDIA 우선' 전략을 세웠다. 하지만 2026년, 같은 빅테크 기업들이 직접 칩을 설계하기 시작했다.

구글은 7세대 TPU 'Ironwood'를 공개했다. 메타는 단 하루에 4세대 칩 로드맵을 발표했다. 아마존은 3나노 공정의 Trainium 3를 AWS에 올렸다. 마이크로소프트는 자사 데이터센터에서 OpenAI GPT-5.2 모델을 직접 개발한 'Maia 200'으로 돌리기 시작했다. 모두 NVIDIA GPU 없이.

이것은 단순한 기술 경쟁이 아니다. **추론(Inference)이 AI 컴퓨트의 2/3를 차지하는 시대**로 넘어오면서, 범용 GPU보다 특정 작업에 최적화된 전용 칩(ASIC)이 경제적으로 압도적 우위를 갖기 시작했다. 변곡점은 이미 지나쳤다. 지금은 그 파도가 얼마나 높이 치솟는지를 가늠하는 시간이다.

---

## 📈 2. 10년 차트가 보여주는 단 하나의 변곡점

**2016년 NVIDIA의 데이터센터 매출은 $3억이었다.**

10년이 지난 2026년, 그 숫자는 $1,300억(FY2026 전망)으로 불어났다. 약 430배. 인류 역사상 어떤 기업도 이 속도로 성장한 적이 없었다. NVIDIA의 AI 가속기 시장 점유율은 2024년 87%까지 치솟았다. 이것이 피크였다.

### 추론 비용의 폭락, 그리고 ASIC의 시간

동시에, 추론 토큰 비용의 역사적 붕괴가 진행됐다:

- **2022년 11월**: GPT-3.5급 성능에 $20/100만 토큰
- **2024년 10월**: $0.07/100만 토큰
- **2026년 (추정)**: $0.01 미만

2년 만에 **99.6% 하락**. Epoch AI Research가 추적한 이 곡선의 가속 원인 중 하나가 바로 커스텀 실리콘이다.

### ASIC의 시간표

TrendForce의 2026 Cloud AI Outlook에 따르면, 커스텀 ASIC의 성장률은 **44.6%**인 반면 GPU 성장률은 **16.1%**다. Bloomberg Intelligence는 AI 가속기 시장에서 ASIC의 비중이 2024년 8%에서 **2033년 19%**로 늘어날 것으로 전망했다. 그리고 결정적인 예측 하나: **2028년, ASIC 출하량이 GPU를 추월한다**.

### 왜 지금인가? — 추론의 지배

2023년, AI 컴퓨트에서 추론이 차지하는 비중은 1/3이었다. 2026년, 그 비중은 **2/3**가 됐다(Deloitte 전망). ChatGPT와 Claude를 수억 명이 쓰는 시대, 모델을 한 번 훈련시키는 비용보다 매초 수백만 건의 질문에 답하는 '추론' 비용이 훨씬 크다는 뜻이다. TSMC의 CC Wei CEO는 2026년 4월 어닝콜에서 이렇게 말했다: *"아젠틱 AI로의 전환이 추론에서 소비되는 토큰 수를 급격히 늘리고 있다. 이는 최첨단 실리콘에 대한 강력한 수요를 지지한다."*

그 '최첨단 실리콘'이 이제 반드시 NVIDIA일 필요는 없게 됐다. 추론 작업은 하나의 모델, 하나의 요청 패턴이 반복된다 — ASIC이 가장 잘하는 영역이다.

---

## 🌏 3. 미국, 한국, 중국, 유럽이 모두 다른 게임을 하고 있다

### 🇺🇸 미국: 빅테크 5사의 칩 군비경쟁

구글, 메타, 아마존, 마이크로소프트, OpenAI. 이 5개 기업이 2026년 집행할 AI 인프라 capex는 합산 **$660~690B**이며, 이 중 75%가 AI 인프라에 쏠린다. 그리고 이 돈의 점점 더 많은 부분이 NVIDIA가 아닌 자체 ASIC에 흐른다.

각 사의 최신 칩 성능을 NVIDIA H100 기준과 비교하면:

| 기업 | 칩 | 성능(FP8) | 공정 | 특징 |
|------|----|---------|------|------|
| **[기준] NVIDIA** | H100 SXM5 | 3.9 PFLOPS/칩 | TSMC 4nm | GPU 범용 추론+훈련 |
| Google | Ironwood TPU v7 | **4.6 PFLOPS/칩** | TSMC | Anthropic 100만 개 배포 |
| Meta | MTIA 400 | **6.0 PFLOPS/칩** | TSMC | 6개월 출시 주기 |
| Amazon | Trainium 3 | **2.52 PFLOPS/칩** | TSMC 3nm | UltraServer 362 PFLOPS |
| Microsoft | Maia 200 | **5.0 PFLOPS/칩** | TSMC 3nm | OpenAI GPT-5.2 구동 |

단순 스펙 비교만으로는 뉘앙스가 빠진다. 각 칩은 해당 회사의 소프트웨어 스택, 모델 아키텍처, 데이터센터 설계와 수직 통합돼 있어 **자사 AI 서비스만 돌리는 빅테크에게는 최적의 선택**이 된다.

픽앤샤블의 왕은 **Broadcom($AVGO)**이다. 구글 TPU, 메타 MTIA, Anthropic 칩 모두 Broadcom이 설계 파트너다. 2026년 Q1 AI 반도체 매출 $8.4B(+106% YoY), Q2 가이던스 $10.7B. AI 수주잔고만 $73B. Broadcom의 FY2025 10-K(SEC EDGAR 제출)에 따르면, 총매출 $63.9B 중 AI 반도체가 핵심 성장 동력으로 부상했다.

또 다른 픽앤샤블인 **Marvell($MRVL)**은 AWS Trainium과 Microsoft Maia의 네트워킹 ASIC을 담당하며 ASIC 시장 20~25%를 점유한다.

### 🇰🇷 한국: 보이지 않는 HBM 독점

이 모든 ASIC 칩에는 하나의 공통점이 있다 — **고대역폭메모리(HBM)**. 구글 Ironwood는 HBM3e 192GB, 메타 MTIA 400은 HBM 288GB, 마이크로소프트 Maia 200은 HBM3e 216GB. 이 메모리의 상업적 생산은 사실상 한국 두 기업이 독점한다.

**SK하이닉스**: 2025년 HBM 출하 점유율 62%, 매출 점유율 57%. Microsoft Maia 200의 HBM 독점 공급사. 2026년 투자 규모를 4배 이상 확대 예정.

**삼성전자**: Meta MTIA 공급 파트너. 2026년 HBM 생산 ~50% 증산.

TrendForce에 따르면, ASIC 기반 AI 칩 전용 HBM 수요는 **+82%** 급증할 전망이다. ASIC 슈퍼사이클의 가장 조용하고, 가장 확실한 수혜자다.

### 🇨🇳 중국: 화웨이의 고립된 생태계

미국의 수출 통제로 중국은 별도의 AI 칩 생태계를 구축 중이다. 화웨이의 Ascend 910C는 SMIC 7nm 공정에도 불구하고 NVIDIA H100의 약 80% 수준의 컴퓨트 성능을 낸다. 2026년 60만 개 생산 목표. 더 주목할 것은 **Ascend 950PR** — FP4 성능이 NVIDIA H20의 2.8배로 ByteDance가 $5.6B을 선주문했다.

중국은 TSMC와 ASML의 최신 장비에 접근할 수 없어 전력 효율에서 구조적 열세를 가진다. 하지만 국내 수요 규모만으로도 독자 생태계를 유지할 수 있는 거대 시장이다.

2026년 5월 10~11일 미중 제네바 합의(관세 115% → 30%, 90일 유예)는 전통적 수출 통제에는 큰 변화를 주지 않지만, TSMC와 Broadcom의 공급망 불확실성을 낮추는 긍정적 신호다.

### 🇪🇺 유럽: 리소스 없는 야망

유럽은 EU Chips Act로 2030년까지 세계 반도체 시장 점유율을 현재 10%에서 20%로 높이겠다는 목표를 세웠다. ASML의 High-NA EUV 장비는 세계 유일이며, IMEC(벨기에)의 NanoIC 파일럿 라인이 유럽의 희망이다. 그러나 유럽 감사원은 2025년 4월 이 목표가 "매우 달성하기 어렵다"고 평가했다. 유럽은 칩 제조 장비(ASML)는 독점하지만, 정작 커스텀 AI 칩을 설계·운영할 하이퍼스케일러가 없다.

---

## ⚖️ 4. NVIDIA가 틀릴 수 없는 이유, 그럼에도 틀릴 수 있는 이유

### 🐂 Bull: ASIC은 추론을, GPU는 훈련을 — 두 시장 모두 성장한다

가장 강력한 반론은 NVIDIA 자신이 제기한다. AI 훈련은 여전히 GPU의 영역이다. NVIDIA의 훈련 시장 점유율은 90%에 달하며, CUDA 소프트웨어 생태계는 15년 이상 쌓아온 방어벽이다. 빅테크가 자체 칩을 만들더라도 최첨단 모델 훈련에는 NVIDIA Blackwell이 필수다. 시장 전체가 커지는 중이니 NVIDIA의 절대 매출은 오히려 늘어날 수 있다 — 점유율이 87%에서 75%로 줄어도, 시장이 5배 커지면 절대 매출은 늘어난다.

게다가 NVIDIA는 Blackwell Ultra, Rubin 아키텍처를 준비 중이다. CUDA 생태계에서 벗어나는 비용은 천문학적이다. 수십만 개의 기존 AI 모델이 CUDA 최적화로 작성돼 있다.

### 🐻 Bear: 추론 = 돈, 그리고 돈은 ASIC으로 간다

카운터 시나리오는 간단하다. AI 시대에서 **돈을 버는 것은 추론**이다. 구글 검색, 메타 피드 알고리즘, 아마존 상품 추천 — 이 모든 것이 초당 수백만 건의 추론이다. 그리고 추론에서 ASIC은 GPU보다 30~50% 낮은 TCO를 제공한다. Midjourney의 사례처럼 65% 비용 절감이 현실이다. 하이퍼스케일러가 자체 칩 개발에 $1B을 투자하면 5년간 $10B의 GPU 비용을 절감할 수 있다 — ROI가 10배다.

더 날카로운 비판: NVIDIA의 Blackwell 시스템은 공급이 수요를 따라가지 못하는 상황이지만, 빅테크가 ASIC 생산을 가속하면 NVIDIA GPU 대기 수요가 단기간에 급감할 수 있다.

### 🃏 가장 의외의 리스크: ASIC도 GPU처럼 공급 부족

아이러니하게도, ASIC 붐의 가장 큰 위험은 ASIC 자체의 공급 제약이다. Broadcom이 설계하고, TSMC가 만들고, SK하이닉스가 HBM을 공급하는 이 체인 어디서든 병목이 생기면 사이클이 꺾인다. TSMC는 이미 N3 공정을 최대 가동 중이다. 하이퍼스케일러 모두가 동시에 ASIC을 원할 때 누가 먼저 얻는지가 새로운 경쟁이 된다.

---

## 💡 5. 투자자에게 남는 것: 칩 전쟁의 진짜 수혜자를 찾아라

### 📌 포지션 프레임

ASIC 슈퍼사이클에서 투자 기회를 구조적으로 정리하면:

**Tier 1 — 직접 수혜, 가시성 높음**

**$AVGO (Broadcom)** — 이 판의 진짜 픽앤샤블. 고객이 NVIDIA든 구글이든 메타든, 칩을 직접 만들려면 Broadcom이 필요하다. AI 수주잔고 $73B은 2027년 중반까지 매출 가시성을 제공한다. 5번째 XPU 고객 추가($1B 초기 주문) 확인. FY26 AI 매출 $40.4B 목표. 리스크: Apple이나 Amazon이 완전 내재화할 경우 고객 이탈.

**$TSM (TSMC)** — ASIC이든 GPU든 모두 TSMC가 만든다. FY2026 가이던스 >30% USD 성장, 역대 최고 수준의 총이익률 66.2%. ASIC 붐은 N3, N2 선단 공정 수요를 폭증시킨다. 미중 무역합의로 공급망 리스크 소폭 감소.

**Tier 2 — 간접 수혜, 성장 가시성**

**$MRVL (Marvell)** — AWS, Microsoft의 네트워킹 ASIC 파트너. ASIC 시장 20~25% 점유. 빅테크가 ASIC을 더 많이 만들수록 Marvell의 네트워킹 IC 수요도 비례 증가.

**$005930 KS / $000660 KS (삼성·SK하이닉스)** — HBM 없이는 ASIC도 없다. ASIC용 HBM 수요 +82% 전망. 국내 투자자에게는 ASIC 테마의 가장 직접적인 한국 플레이.

**Tier 3 — 관심 지속, 진입 조건 필요**

**$NVDA** — 단기 매도 근거 없음. AI 훈련 90% 점유 + 선단 GPU 독보적 위치. 다만 ASIC 점유율 잠식이 구조적 추세임을 인지하고 FY2027 가이던스 반응을 지켜볼 것. 추론 시장 대응으로 NIM 플랫폼, GB300 Ultra 동향 주시.

### ⚡ 카탈리스트 캘린더

- **5월 중순**: 미중 90일 유예 기간 내 구체적 실행 조건 공개 예정
- **6월 2~3일**: Microsoft Build 2026 — Maia 200 확장 발표 예상
- **6월 4~11일 (추정)**: Broadcom Q2 FY26 실적 발표 (가이던스 $10.7B 달성 여부)
- **2026년 H2**: OpenAI 커스텀 칩 양산 시작 → AVGO 6번째 XPU 고객 확인 가능성

### 🎯 핵심 체크 포인트

ASIC 슈퍼사이클 내러티브가 틀렸다는 신호:
- Broadcom이 주요 고객(구글, 메타)을 잃거나 계약을 갱신 못할 때
- TSMC N3 수율이 급격히 나빠져 ASIC 생산 차질 발생 시
- NVIDIA가 추론 전용 저전력 칩으로 ASIC 영역에 역침투할 때

---

Midjourney가 NVIDIA 서버실에서 짐을 쌌던 그 날, 사실 Midjourney만 이사한 게 아니었다. 이미 수조 달러의 capex가 새 주소를 향해 움직이기 시작했다. AI 칩 전쟁의 승자는 아직 정해지지 않았지만, **싸움의 본질이 '훈련'에서 '추론'으로 이동했다는 사실** 하나만큼은 확실하다. 추론을 가장 싸게 제공하는 자가 AI 시대의 인프라를 지배한다.

---

## 📚 출처

| 자료 | 유형 | URL |
|------|------|-----|
| Broadcom FY2025 10-K | SEC EDGAR (1차) | [SEC.gov](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm) |
| TSMC Q1 2026 어닝콜 | 실적발표 트랜스크립트 (1차) | [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-tsmcs-q1-2026-shows-strong-growth-and-margin-gains-93CH-4617167) |
| Google Cloud — Ironwood TPU | 기업 공식 블로그 (1차) | [Google Cloud](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads) |
| Meta — MTIA 발표 | 기업 공식 뉴스룸 (1차) | [about.fb.com](https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/) |
| Microsoft — Maia 200 발표 | 기업 공식 블로그 (1차) | [Microsoft Blog](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/) |
| TrendForce 2026 Cloud AI Outlook | 산업 리서치 보고서 (1차) | [TrendForce](https://www.trendforce.com/research/download/RP251105VO) |
| Bloomberg Intelligence AI 가속기 | 시장 조사 (1차) | [Bloomberg](https://www.bloomberg.com/company/press/ai-accelerator-market-looks-set-to-exceed-600-billion-by-2033-driven-by-hyperscale-spending-and-asic-adoption-according-to-bloomberg-intelligence/) |
| White House 미중 합의 브리핑 | 정부 성명 | [WhiteHouse.gov](https://www.whitehouse.gov/briefings-statements/2025/05/joint-statement-on-u-s-china-economic-and-trade-meeting-in-geneva/) |
| ARK Invest AI 인프라 리서치 | 투자 리서치 | [ARK Invest](https://www.ark-invest.com/articles/analyst-research/the-state-of-ai-infrastructure-demand-costs-custom-silicon) |
| SK하이닉스 2026 아웃룩 | 기업 공식 | [SK하이닉스](https://news.skhynix.com/2026-market-outlook-focus-on-the-hbm-led-memory-supercycle/) |
| Epoch AI Research 토큰 비용 | 학술 리서치 | [Epoch AI](https://epochai.org) |
| Meta MTIA 공식 블로그 | 기업 공식 블로그 (1차) | [ai.meta.com](https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/) |

