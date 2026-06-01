# 딥다이브 리서치 노트 — 2026-06-01
## 테마: Physical AI 원년 — COMPUTEX 2026, AI가 클라우드를 벗어나 몸을 얻다
## 유형: 📡 테크 트렌드 (월요일)

---

## 1차 자료 인용 건수: 7건 ✅

1. IFR 세계 로봇 보고서 (World Robotics 2025 / IFR 2026 Trends)
2. NVIDIA FY2026 Annual Report / Earnings (SEC EDGAR NVDA 10-K / IR)
3. TrendForce 중국 휴머노이드 로봇 시장 보고서 (2026-04-09)
4. MarketsandMarkets Physical AI Market Report (2026-04-21 PRNewswire)
5. NVIDIA Investor Relations 공식 보도자료 (Physical AI models, GR00T, Cosmos)
6. NVIDIA + 한국 공식 보도자료 (South Korea AI Infrastructure Partnership)
7. NVIDIA Vera Rubin 플랫폼 공식 기술 문서 (developer.nvidia.com / Tom's Hardware)

---

## 선정 이유
오늘 6/1 KST 12:00 Jensen Huang이 COMPUTEX 2026 타이베이 뮤직센터에서 기조연설. "Physical AI" — AI가 데이터센터를 벗어나 로봇·공장·자동차·개인 디바이스로 확산. 훈련(Training) 중심 AI 인프라 슈퍼사이클 1막이 끝나고, 추론(Inference) + 물리 세계 배포 2막이 열리는 구조적 전환점.

---

## 팩트 (출처 필수)

### COMPUTEX 2026 키노트
1. Jensen Huang, 6/1 오전 11시(현지) 타이베이 뮤직센터 기조연설. GTC Taipei 2026 + COMPUTEX 병행 (6/1~5) — 출처: https://www.nvidia.com/en-tw/gtc/taipei/keynote/
2. 키노트 3대 테마: Agentic AI, Physical AI, AI Factory — 출처: https://www.fool.com/investing/2026/05/31/nvda-stock-jensen-huang-keynote-computex/
3. "Five Layer Cake" 전략: 에너지 → 칩 → 데이터센터/클라우드 → AI 모델 → 애플리케이션. NVIDIA가 5개 레이어 모두에 포지셔닝 — 출처: https://www.newsbytesapp.com/news/science/nvidia-ceo-jensen-huang-outlines-5-layer-cake-powering-ai/tldr, https://finance.biggo.com/news/CAqos50BvthpMgHBOlhD

### Physical AI 신제품 (COMPUTEX/GTC Taipei 2026)
4. Cosmos 3: 세계 파운데이션 모델, mixture-of-transformers 아키텍처. 1인칭/3인칭으로 물리 세계 시뮬레이션, 텔레오퍼레이션·시뮬레이션·리프로젝션 비디오 학습. 비전 추론·세계 시뮬레이션·액션 생성 벤치마크 최고 성능 — 출처: https://nvidianews.nvidia.com/news/nvidia-releases-new-physical-ai-models-as-global-partners-unveil-next-generation-robots
5. GR00T N1.7: 3B 파라미터 VLA(Vision-Language-Action) 모델. 20,000시간 EgoScale 인간 비디오 데이터 사전학습. 상업 라이선스 출시. MolmoSpaces·RoboArena 1위 — 출처: https://huggingface.co/blog/nvidia/gr00t-n1-7
6. GR00T N2 프리뷰: DreamZero 리서치 기반 월드-액션 모델. 기존 최고 VLA 대비 새 환경 작업 성공률 2배 이상. 연내 출시 예정 — 출처: https://nvidianews.nvidia.com/news/nvidia-releases-new-physical-ai-models-as-global-partners-unveil-next-generation-robots
7. Isaac GR00T Reference Humanoid = Unitree H2 Plus(약 183cm) + Sharpa 5지 손 + NVIDIA Jetson Thor. Jetson Thor 스펙: 2,070 FP4 TFLOPS, 128GB 통합 메모리, 40~130W, Blackwell GPU + 14코어 Arm CPU. 스탠퍼드·ETH 취리히 등 연구기관 배포 — 출처: https://www.prnewswire.com/news-releases/unitree-announces-h2-plus-an-nvidia-isaac-gr00t-reference-humanoid-robot-for-academic-research-302786748.html, https://www.cnbc.com/2026/06/01/nvidia-unitree-humanoid-robotics-system-researchers.html

### RTX Spark (엣지 AI / 개인 AI 컴퓨팅)
8. RTX Spark 슈퍼칩: Blackwell GPU(6,144 CUDA 코어) + Arm N1X CPU(20코어) + 최대 128GB LPDDR4X(300 GB/s). 1 PFLOP FP4 AI 성능. 120B 파라미터 모델 로컬 실행 가능. MediaTek과 공동 설계 — 출처: https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory
9. 탑재 파트너: Dell, HP, Lenovo, Microsoft, Asus, MSI. 랩탑 30종+ + 데스크탑 10여 종. 2026년 가을 출시 — 출처: https://www.nvidia.com/en-us/geforce/news/computex-2026-nvidia-geforce-rtx-announcements/
10. DGX Station: GB300 Grace Blackwell Ultra, 748GB 코히런트 메모리, 20 petaflops FP4 — 출처: Computex 2026 live coverage

### Vera Rubin (차세대 데이터센터)
11. Vera Rubin GPU: 336억 트랜지스터. 50 PFLOPs NVFP4 추론 (Blackwell 대비 5배). HBM4 최대 288GB/GPU, 22 TB/s 대역폭 — 출처: https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/
12. Vera Rubin NVL72: 72 GPU + 36 Vera CPU, 3.6 EFLOPS NVFP4 추론. Blackwell 대비 토큰 비용 10배 절감. 2H 2026 양산 — 출처: https://www.tomshardware.com/pc-components/gpus/nvidia-launches-vera-rubin-nvl72-ai-supercomputer-at-ces-promises-up-to-5x-greater-inference-performance-and-10x-lower-cost-per-token-than-blackwell-coming-2h-2026

### NVIDIA 재무 데이터 (1차 자료: SEC EDGAR / IR)
13. NVIDIA FY2026 총 매출: $215.9B (+65% YoY) — 출처: https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000038/a2026-annualxreportxwebxfi.pdf (SEC EDGAR ARS FY2026)
14. 데이터센터 매출: $193.7B (+68% YoY), 총 매출의 89.7%. 네트워킹(NVLink) +142% — 출처: 동일
15. Physical AI 매출(FY2026): $6B / TTM 기준 $9B+ — 출처: https://www.fool.com/investing/2026/03/04/buy-nvidia-stock-physical-ai-transformation-2035/ (어닝콜 언급 인용)
16. Blackwell 시스템: 2026년 상반기까지 매진, GPU당 약 $40,000 — 출처: https://futurumgroup.com/insights/nvidia-q4-fy-2026-earnings-highlight-durable-ai-infrastructure-demand/
17. NVIDIA $1조 AI 칩 수요 선언 (2027년까지 확정 주문 기준) — 출처: https://www.datacenterknowledge.com/data-center-chips/gtc-2026-nvidia-unveils-vera-rubin-ai-platform-eyes-1t-by-2027

### 한국 파트너십
18. NVIDIA + 한국 4대 그룹 "Korea Partner Night" 6/1 타이베이 다안구. 반도체 공급 + Physical AI 플랫폼(Omniverse·Isaac) 논의 — 출처: https://en.sedaily.com/finance/2026/05/31/jensen-huang-to-meet-koreas-top-4-conglomerates-on-ai-chips
19. 한국 NVIDIA GPU 배치 260,000개: 삼성(50,000+), SK(50,000+), 현대차(50,000+), 네이버(60,000+). 총 투자액 ₩14.8조 (~$7.8~10.4B) — 출처: https://www.datacenterdynamics.com/en/news/nvidia-to-deploy-more-than-250000-gpus-across-south-korea-with-samsung-sk-group-and-hyundai-all-announcing-ai-factories/
20. 현대차-NVIDIA Physical AI 파트너십 $3B 규모. 제조 AI + 자율주행 학습/검증/배포 통합 — 출처: https://nvidianews.nvidia.com/news/south-korea-ai-infrastructure
21. Jensen Huang, 6/5경 한국 방문 예정. 최태원·정의선·구광모·이해진 면담 — 출처: https://en.sedaily.com/finance/2026/05/28/jensen-huang-to-visit-korea-next-month-for-possible-second

### 글로벌 시장 (1차 자료: IFR, TrendForce, MarketsandMarkets)
22. IFR: 2024년 산업용 로봇 542,000대 설치 (역대 최고), 가동 재고 4,664,000대, 시장 $16.7B. 중국 54% 점유. 2028년 700,000대 예상 (CAGR ~7%) — 출처: https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
23. Physical AI 시장: $1.5B(2026) → $15.24B(2032), CAGR 47.2%. 아태 50.4% 최대 — 출처: https://www.prnewswire.com/news-releases/physical-ai-market-worth-15-24-billion-by-2032---exclusive-report-by-marketsandmarkets-302732794.html
24. AI 기반 산업 로봇: $17.9B(2026) → $33.3B(2035), CAGR 7.1% — 출처: https://www.gminsights.com/industry-analysis/ai-powered-industrial-robot-market

### 중국 휴머노이드 로봇 (TrendForce)
25. 중국 2026년 휴머노이드 생산 +94% 급증. Unitree + AgiBot = 전체 80% 점유 — 출처: https://www.trendforce.com/presscenter/news/20260409-13007.html
26. Unitree: 2025년 5,500대 출하, 2026년 목표 10,000~20,000대. 생산능력 75,000대/년 — 출처: 동일
27. AgiBot: 2026년 3월 10,000번째 로봇 출하. 월 1,000→10,000대로 3개월 내 10배 확장 — 출처: 동일
28. 글로벌 휴머노이드 출하 2026년 50,000대+ (+700% YoY) — 출처: https://www.dqindia.com/esdm/chinas-humanoid-robot-output-to-surge-94-in-2026-unitree-and-agibot-to-capture-nearly-80-market-share-11727677

### NVIDIA 로봇 생태계
29. "Android of Robotics" 전략: GR00T + Isaac + Cosmos가 스마트폰의 Android처럼 로봇 표준 플랫폼 목표 — 출처: https://techcrunch.com/2026/01/05/nvidia-wants-to-be-the-android-of-generalist-robotics/
30. Isaac 로봇 개발자 200만 명. Hugging Face LeRobot 통합으로 Hugging Face 1,300만 AI 빌더와 연결 — 출처: 동일
31. 파트너: ABB, Agility, AGIBOT, Boston Dynamics, Caterpillar, FANUC, Figure, Hexagon, KUKA, Medtronic, Universal Robots, World Labs, YASKAWA — 출처: https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world

---

## 직접 인용

1. "AI isn't just in the cloud anymore. We're in the era of physical AI — intelligence that can perceive, reason, and act in the physical world." — Jensen Huang, COMPUTEX 2026 keynote (paraphrase, 정확한 원문은 영상 확인 필요) — 출처: Motley Fool 정리
2. "Nvidia wants to be the Android of generalist robotics." — TechCrunch 헤드라인 (2026-01-05) — 출처: https://techcrunch.com/2026/01/05/nvidia-wants-to-be-the-android-of-generalist-robotics/
3. "Inference demand is surging as multiple exponential forces converge, with models becoming more capable and agents built on these models able to reason, plan, and solve complex problems." — NVIDIA (Futurum 인용) — 출처: https://futurumgroup.com/insights/nvidia-gtc-2026-day-1-can-nvidias-ecosystem-accelerate-the-inference-inflection/

---

## 숫자 데이터

| 지표 | 수치 | 출처 |
|------|------|------|
| NVIDIA FY2026 총 매출 | $215.9B (+65% YoY) | SEC EDGAR |
| NVIDIA 데이터센터 매출 | $193.7B (+68% YoY) | SEC EDGAR |
| NVIDIA Physical AI 매출(FY2026) | $6B / TTM $9B+ | 어닝콜 |
| Vera Rubin 추론 성능 | 50 PFLOPs (Blackwell 5배) | NVIDIA 기술 블로그 |
| Vera Rubin 토큰 비용 절감 | Blackwell 대비 10배 | Tom's Hardware |
| RTX Spark 로컬 실행 | 120B 파라미터 모델 | NVIDIA/Tom's Hardware |
| Physical AI 시장(2026→2032) | $1.5B → $15.24B (CAGR 47.2%) | MarketsandMarkets |
| 글로벌 산업 로봇(2024) | 542,000대 / $16.7B | IFR |
| 중국 휴머노이드 생산 증가(2026) | +94% | TrendForce |
| 글로벌 휴머노이드 출하(2026) | 50,000대+ (+700% YoY) | TrendForce |
| 한국 NVIDIA GPU 배치 | 260,000개 | DCD / NVIDIA IR |
| 한국 총 투자액 | ₩14.8조 (~$7.8~10.4B) | Reuters / DCD |
| 현대차-NVIDIA Physical AI 계약 | $3B | NVIDIA IR |
| Unitree 2026 생산 목표 | 10,000~20,000대 | TrendForce |
| NVIDIA 로봇 개발자 수 | 200만 명 | NVIDIA |

---

## 관련 종목
- $NVDA — Physical AI OS 플랫폼 + Jetson Thor 직접 수혜
- $ISRG — 의료용 Physical AI (da Vinci → AI 강화)
- 현대차 (005380.KS) — Boston Dynamics + Jensen Huang $3B 파트너십
- 삼성전자 (005930.KS) — HBM + AI 팩토리 50K GPU
- SK하이닉스 (000660.KS) — HBM4 Vera Rubin 공급
- $AVGO — Physical AI ASIC 수요 (D+2 6/3 어닝)
- $MRVL — 커스텀 AI 칩 수요

---

## 반론/리스크

1. Physical AI 매출은 아직 NVIDIA 전체의 3%: $6B vs 데이터센터 $194B. 의미있는 매출 비중이 되려면 2030년 이후 — 출처: https://www.fool.com/investing/2026/03/04/buy-nvidia-stock-physical-ai-transformation-2035/
2. ASP 구조 문제: H100/H200 $40,000+인데 로봇용 Jetson Thor는 수십~수백 달러. 볼륨 확대 → ASP 하락. 스마트폰 AP 역사 반복 우려
3. 중국 경쟁: 글로벌 휴머노이드 80% = 중국. Unitree G1 $16,000(저가). 하드웨어 레이어 빠른 상품화 가능
4. 기술 성숙도: 로봇이 실제 공장·병원에서 안전하게 작동하는 수준까지 수 년 필요. 현재는 연구 단계
5. 에너지/냉각: Physical AI 확산 따른 추가 전력·냉각 수요가 배포 속도 제한 가능
