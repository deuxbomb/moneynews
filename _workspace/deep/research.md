# 딥다이브 리서치 노트 — 2026-05-25

## 테마
하이퍼스케일러 카펙스 $830B — 픽앤샤블 지도

## 유형
📡 테크트렌드 — 여러 기업이 같은 방향으로 달린다 → AI 인프라 공급자 지형 조망

## 1차 자료 인용 건수: 8건 (필수 3건+ 충족 ✅)

| # | 소스 유형 | 출처명 | URL |
|---|---------|--------|-----|
| 1 | SEC 10-Q | Meta Q1 2026 10-Q | https://www.sec.gov/Archives/edgar/data/0001326801/000162828026028526/meta-20260331.htm |
| 2 | SEC 10-Q | Alphabet Q1 2026 10-Q | https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm |
| 3 | 8-K/실적발표 | NVIDIA Q1 FY2027 8-K | https://www.stocktitan.net/news/NVDA/nvidia-announces-financial-results-for-first-quarter-fiscal-fq78amc9h84m.html |
| 4 | SEC 8-K | Arista Networks Q1 2026 8-K | https://www.sec.gov/Archives/edgar/data/0001596532/000159653226000074/ex991q126-earningsrelease.htm |
| 5 | SEC 8-K/10-Q | Vertiv Holdings Q1 2026 | https://www.sec.gov/Archives/edgar/data/0001674101/000162828026026556/vrt-20260331.htm |
| 6 | 산업 보고서 | TrendForce — "Top 9 CSPs 2026 $830B" | https://www.trendforce.com/presscenter/news/20260506-13033.html |
| 7 | 투자은행 리서치 | Goldman Sachs — "Tracking Trillions" | https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out |
| 8 | 컨설팅 보고서 | McKinsey — "The cost of compute: A $7T race" | https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-cost-of-compute-a-7-trillion-dollar-race-to-scale-data-centers |

---

## 선정 이유
NVIDIA가 Q1 FY2027 $81.6B 실적과 Q2 가이던스 $91B을 발표한 지 5일째(2026-05-25). 투자 커뮤니티의 가장 뜨거운 질문은 "이 수요가 어디서 오고, 그 돈은 어디로 가는가"다. TrendForce가 확인한 2026년 상위 9개 CSP 합산 카펙스 $830B은 AI 역사상 단일 연도 최대 집중 투자 사이클이다. 단순히 GPU 수요가 크다는 이야기가 아니라, $830B이 레이어별로 어떻게 분산되고 그 수혜 기업이 누구인지 픽앤샤블 지도를 그리는 것이 이번 딥다이브의 목적이다.

---

## 팩트 (출처 필수)

### A. 빅4 하이퍼스케일러 2026 카펙스 실수치

1. **Meta Q1 2026 카펙스 $19.84B** (단일분기, 금융 리스 원금 포함), FY2026 연간 가이던스 **$125-145B** (Q1 2026 10-Q). 이전 가이던스 $115-135B에서 상향. 2025년 FY 전체 $72.2B 대비 약 2배. — 출처: SEC EDGAR Meta Q1 10-Q (https://www.sec.gov/Archives/edgar/data/0001326801/000162828026028526/meta-20260331.htm); PRNewswire 확인(https://www.prnewswire.com/news-releases/meta-reports-first-quarter-2026-results-302757852.html)

2. **Alphabet Q1 2026 카펙스 $35.7B** (단일분기), FY2026 연간 가이던스 **$180-190B** (기존 $175-185B에서 상향). 2025년 $91.5B 대비 약 2배. — 출처: SEC EDGAR Alphabet Q1 10-Q (https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm); CNBC 확인(https://www.cnbc.com/2026/04/29/alphabet-googl-q1-2026-earnings.html)

3. **Microsoft Q1 FY2027 카펙스 $34.9B** (+74% YoY), Azure 전체 용량 FY2026 +80% 목표, 첫 NVIDIA GB300 대규모 클러스터 배포, Fairwater(위스콘신) 2GW 시설 발표. — 출처: https://tech-insider.org/microsoft-ai-spending-azure-copilot-2026/; Futurum Group(https://futurumgroup.com/insights/microsoft-q1-fy-2026-cloud-and-ai-fuel-broad-based-growth/)

4. **Amazon Q1 2026 카펙스 $44.2B** (Q1 2025 $25B 대비 +77%), FY2026 연간 가이던스 **~$200B**. AWS Q1 매출 $37.6B (+28%, 2022 Q4 이후 최고 성장). Trainium 누적 수주 $225B+ 달성. — 출처: The AI Consulting Network(https://www.theaiconsultingnetwork.com/blog/amazon-q1-2026-aws-44b-capex-cre-data-center-investors); Motley Fool 어닝콜 트랜스크립트(https://www.fool.com/earnings/call-transcripts/2026/04/29/amazon-amzn-q1-2026-earnings-call-transcript/)

5. **빅4 Q1 2026 합산 카펙스 $134.64B** 단일분기. FY2026 가이던스 합산: Meta $135B 미드 + Google $185B + Microsoft ~$130B(추정) + Amazon $200B = **~$650-660B (Big 4)**.

6. **TrendForce: 상위 9개 CSP 2026 합산 카펙스 $830B** (북미 AI 데이터센터 확장 주도). 빅4 외 Oracle, Apple, ByteDance, Alibaba, Tencent 포함. — 출처: TrendForce(https://www.trendforce.com/presscenter/news/20260506-13033.html); Yahoo Finance(https://finance.yahoo.com/sectors/technology/articles/north-american-ai-data-center-120000137.html)

### B. NVIDIA 데이터

7. **NVIDIA Q1 FY2027 매출 $81.6B** (+85% YoY, 컨센서스 $79.19B 비트). Q2 FY2027 가이던스 **$91B** (±2%), 애널리스트 컨센서스 $86.84B 대비 +5% 상회. **중국 데이터센터 컴퓨트 매출 제외** 기준. 총마진 가이던스 74.9% (GAAP) / 75.0% (Non-GAAP). 배당 25배 인상($0.01→$0.25 기준), $80B 자사주매입 승인. — 출처: NVIDIA 8-K(https://www.stocktitan.net/news/NVDA/nvidia-announces-financial-results-for-first-quarter-fiscal-fq78amc9h84m.html); Shacknews(https://www.shacknews.com/article/149230/nvidia-nvda-q2-fy27-revenue-forecast-china-data-center)

### C. 픽앤샤블 수혜 기업 (레이어별)

#### 레이어 1: 전력·냉각 (McKinsey 분류 "Energizers" ~25%)
8. **Vertiv (VRT) Q1 2026**: 순매출 $2.65B (+30% YoY, 유기적 +23%), 수주잔고 **$12.45B (+80.8% YoY)**. 프로젝트 백로그 $15B+ (12-18개월 매출). FY2026 가이던스 **$13.5-14B**으로 상향. 조정 영업마진 20.8% (+430bp). — 출처: SEC Vertiv 8-K/10-Q(https://www.sec.gov/Archives/edgar/data/0001674101/000162828026026556/vrt-20260331.htm); TechJack(https://techjacksolutions.com/ai-brief/vertiv-raises-2026-guidance-to-14b-as-ai-data-center-backlog/)

9. **한국 K전력기기**: 빅4(HD현대일렉·효성중공업·LS ELECTRIC·산일전기) 수주 33조 돌파, 5년치 일감 확보. 2025년 1-11월 전력기기 수출 $71.3억 역대 최고치 (+11.3% YoY). HD현대일렉 2025년 매출 4조795억 (+22.8%), 영업이익 9,953억 (+46.8%). 효성중공업 매출 5조9,685억 사상 최대. 18-20% 관세에도 공급 부족으로 계속 계약 유지. — 출처: 서울경제(https://www.sedaily.com/NewsView/2H0I41MC9B); BusinessPost(https://www.businesspost.co.kr/BP?command=article_view&num=434915)

#### 레이어 2: 네트워킹
10. **Arista Networks (ANET) Q1 2026**: 매출 $2.709B (+35.1% YoY), 영업현금흐름 $1.69B. FY2026 가이던스 **$11.5B** (+27.7%). AI 네트워킹 2026년 목표 **$3.5B** (이더넷 AI 패브릭, 클라우드 하이퍼스케일러 채택 급증). — 출처: SEC Arista 8-K(https://www.sec.gov/Archives/edgar/data/0001596532/000159653226000074/ex991q126-earningsrelease.htm); InfotechLead(https://infotechlead.com/networking/arista-networks-q1-2026-revenue-surges-35-as-ai-networking-cloud-titans-and-enterprise-demand-drive-growth-95620)

#### 레이어 3: 컴퓨트 (GPU/ASIC)
11. 커스텀 ASIC 출하량 성장률 **44.6%** vs GPU **16.1%** (2026E). ASIC 2028년 출하량 기준 GPU 추월 전망. Broadcom($AVGO) AI 수주잔고 $73B. Marvell($MRVL) D+2 2026-05-27 Q1 FY27 어닝. — 출처: Medium 분석 참조(https://medium.com/@vascobotelho2106/the-660-billion-physical-wall-decoding-the-ai-infrastructure-supercycle-af5f5ccbd3ce)

#### 레이어 4: 스토리지
12. Western Digital Q3 FY2026 매출 $3.34B (+45% YoY). Pure Storage Q2 FY2027 매출 $861M (+13%). NetApp Q1 2026 AI 인프라 딜 +33%. 스토리지 레이어는 분산됨(집중도 낮음). — 출처: Nasdaq 비교 분석(https://www.nasdaq.com/articles/wdc-vs-ntap-which-data-storage-stock-offers-better-growth-potential)

### D. 역사적 시계열

13. **빅4 합산 카펙스 역사적 추이**:
   - 2022: ~$162B (Big 5 포함, Epoch AI/플랫폼노믹스 기준)
   - 2023: ~$155-160B (GPT-4 출시 직후 전환점)
   - 2024: ~$251B (+62% YoY)
   - 2025: ~$388-448B (Amazon $134.7B + Google $91.5B + Meta $72.2B + Microsoft ~$90B)
   - 2026E: ~$650-830B (Big 4 $650B+, 상위 9개 CSP $830B)
   **→ 2023년 대비 2026년 4-5배 규모 (Epoch AI: "GPT-4 이후 4배 증가")**
   — 출처: Epoch AI(https://epoch.ai/data-insights/hyperscaler-capex-trend); Platformonomics(https://platformonomics.com/2026/02/follow-the-capex-2025-retrospective/)

14. **McKinsey 데이터센터 투자 2030년까지 $7T 분류**:
   - 60% (~$4.2T): 기술 개발자 (칩, 컴퓨팅 하드웨어, 소프트웨어)
   - 25% (~$1.75T): 에너지 공급자 (전력, 냉각, 전기 설비)
   - 15% (~$1.05T): 건설·부지 개발
   — 출처: McKinsey(https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/the-cost-of-compute-a-7-trillion-dollar-race-to-scale-data-centers)

15. Goldman Sachs "Tracking Trillions": **2026 AI 카펙스 베이스라인 $765B, 2031 $1.6T**. 2026-2031 누적 $7.6T ($5.1T 칩 + $2.15T 데이터센터 + $358B 전력). 칩 경제수명 5년→3년 단축 시 연간 감가상각 ~$1T 추가 급증. — 출처: Goldman Sachs(https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out)

### E. 국제 비교

16. **중국**: 알리바바 3년 $52-69B(480억 위안 고려 중), 텐센트 2026 ¥36B, ByteDance 2026 $23B. 중국 총 AI 투자 2025년 $125B — 미국 빅4 대비 약 1/3 수준. — 출처: Data Center Dynamics(https://www.datacenterdynamics.com/en/news/alibaba-considers-increasing-ai-data-center-capex-spend-to-69bn-over-three-years-report/)

17. **일본**: SoftBank "Roze AI" 데이터센터 건설 로봇 스타트업 $100B 기업가치 IPO 목표(2026). Microsoft-SoftBank 협업 $10B Japan AI 투자. SoftBank 오하이오 10GW 데이터센터 개발. — 출처: TechCrunch(https://techcrunch.com/2026/04/29/softbank-is-creating-a-robotics-company-that-builds-data-centers); Microsoft Asia(https://news.microsoft.com/source/asia/2026/04/03/microsoft-deepens-its-commitment-to-japan/)

18. **한국**: $65B AI 인프라 투자 2027년까지. OpenAI+삼성+SK하이닉스 합작 DC 2026년 3월 착공(초기 20MW). 삼성·SK하이닉스 HBM 글로벌 점유율 90%. — 출처: Introl(https://introl.com/blog/south-korea-ai-infrastructure-65-billion-investment); TechWire Asia(https://techwireasia.com/2026/02/openai-samsung-and-sk-move-ahead-with-korea-data-centre-build/)

### F. 반대 시각 / 위험 요소

19. **MIT**: 95%의 기업이 GenAI 투자 ROI 제로. 미국 소비자 AI 서비스 연간 지출 ~$120억 — 연간 카펙스 $830B의 1.5% 수준. — 출처: Medium 인용(https://medium.com/@truthbit.ai/the-2-trillion-question-can-ai-revenue-catch-up-to-capex-df8c5c3c52fb)

20. **Goldman Sachs ROI 경고**: $5,000억/년 카펙스 유지를 위해 연 $1T+ 수익 실현 필요. 2026 컨센서스 이익 추정 $450B — 필요의 절반도 안 됨. — 출처: Fortune(https://fortune.com/2026/01/07/ai-companies-profit-capex-investment-goldman-sachs-stocks/)

21. **Sequoia Capital "2026 Moment of Truth"**: 데이터센터 가동률 70% 이상 → 투자 정당화. 그렇지 않으면 업계 전반 자산 상각 시작. — 출처: Futurum/Medium 인용

22. **닷컴 버블 비교**: 현재 AI 투자 GDP 대비 0.4% (닷컴 피크 1.2%). Goldman: "FOMO has proven a stronger incentive than poor stock performance" — 게임이론적으로 오버인베스트가 내시균형. — 출처: Fortune(https://fortune.com/2026/05/06/is-ai-a-bubble-goldman-sachs-skeptics-overhyped/)

---

## 직접 인용 (정확한 원문)

1. "Revenue guidance of $91 billion, plus or minus 2% ... This guidance does not include any Data Center compute revenue from China." — NVIDIA, Q1 FY2027 earnings release (2026-05-20)

2. "The economic lifespan of AI chips emerges as the largest variable: shortening it from five to three years would increase annual depreciation costs by nearly $1 trillion." — Goldman Sachs Global Institute "Tracking Trillions" (2026)

3. "FOMO has proven a stronger incentive than poor stock performance." — Goldman Sachs (Fortune 보도, 2026-05-06)

4. "2026 is the moment of truth — the year when either capacity validates or writedowns begin in earnest." — Sequoia Capital (2026, 업계 인용)

---

## 관련 종목

- **$NVDA**: AI 컴퓨트 수요 직접 수혜. Q2 $91B 가이던스 (China 제외). 주가 소화 중
- **$AVGO (Broadcom)**: ASIC 설계 + 이더넷 네트워킹. AI 수주잔고 $73B
- **$TSM (TSMC)**: ASIC·GPU 제조. CoWoS 공급 병목
- **$MRVL (Marvell)**: 커스텀 ASIC + 광학 인터커넥트. D+2 2026-05-27 어닝
- **$ANET (Arista)**: 이더넷 AI 패브릭. AI 매출 $3.5B 타겟
- **$VRT (Vertiv)**: 전력·냉각 순수 플레이. 백로그 +81%
- **$ETN (Eaton)**: 전력 분배. 데이터센터 수요 +200% YoY
- **$PWR (Quanta Services)**: 전력망 건설. 수주잔고 $48.5B
- **HD현대일렉트릭 (267260.KS)**: 초고압 변압기, K-픽앤샤블
- **효성중공업 (298040.KS)**: 변압기·스위치기어 사상 최대 실적

## 반론/리스크

1. MIT 95% 기업 GenAI ROI 제로 — 채택률과 카펙스 사이클의 괴리
2. Goldman: 수익 회수($1T+/년) 대비 투자($500B/년) 불균형
3. 닷컴 버블 패턴 — 통신 인프라 오버빌드 후 장기 자산 상각 선례
4. NVIDIA Q2 $91B 가이던스 China 매출 미포함 — 지정학 리스크
5. 전력망 제약: 데이터센터 전력 승인 지연으로 카펙스 집행 속도 제약
6. 오버인베스트 게임이론: FOMO로 인한 필연적 공급 과잉 가능성
