# AI가 몸을 얻는다 — 젠슨 황의 COMPUTEX 선언, Physical AI가 열어젖힌 반도체 2막

**2026년 6월 1일 | 머뉴 딥다이브 | 📡 테크 트렌드**

---

## 타이베이 뮤직센터, 오늘 오전 11시: 세상이 조용히 바뀐 순간

오늘 아침 11시, 타이베이 뮤직센터. 젠슨 황이 무대에 올랐다. 검은 가죽 재킷은 여전하지만, 그가 꺼낸 메시지는 지난 4년과 달랐다. "AI가 더 이상 클라우드에만 있지 않습니다. 물리 세계를 인식하고, 추론하고, 행동하는 시대가 왔습니다." Physical AI의 선언이었다.

COMPUTEX 2026은 기술 쇼케이스가 아니다. 이번 행사는 AI 역사의 2막이 어디서 시작되는지를 온 세계에 알리는 무대다. 젠슨 황은 세 가지 테마를 제시했다: Agentic AI(자율 에이전트), Physical AI(물리 세계), AI Factory(AI를 찍어내는 공장). 그리고 이 모든 것을 관통하는 "Five Layer Cake" — 에너지, 칩, 데이터센터, AI 모델, 애플리케이션의 5층 구조에서 NVIDIA는 모든 레이어에 자신의 이름을 새겼다.

오늘 발표된 것들을 보자. **Cosmos 3** — AI가 물리 세계를 1인칭으로 시뮬레이션하는 세계 파운데이션 모델. **GR00T N1.7** — 30억 파라미터짜리 로봇 두뇌로, 상업 라이선스까지 즉시 공개됐다. 그리고 **Isaac GR00T Reference Humanoid** — Unitree의 183cm 휴머노이드 로봇 몸통에 NVIDIA의 Jetson Thor 두뇌를 얹은, 세계 첫 오픈 휴머노이드 레퍼런스 디자인. 스탠퍼드대, ETH 취리히 연구소에 납품이 시작된다.

여기에 더해 **RTX Spark** — 120억 파라미터 모델을 노트북에서 로컬로 돌리는 Arm+Blackwell 슈퍼칩도 공개됐다. AI는 이제 데이터센터를 벗어나 당신의 책상 위, 공장 바닥, 로봇의 몸속으로 들어가고 있다.

---

## 10년의 탈출 — AI가 데이터센터 바깥을 꿈꾼 역사

이 순간을 이해하려면 10년을 돌아봐야 한다. 2012년, NVIDIA GPU가 처음으로 이미지 인식 대회에서 인간을 앞질렀다. AlexNet의 승리다. 그때 NVIDIA의 데이터센터 매출은 존재하지 않았다. 칩은 게임용이었고, AI는 학계의 장난감이었다.

2016년 알파고가 이세돌을 꺾었다. AI가 게임을 정복했지만, 여전히 좁은 영역의 이야기였다. 2022년 ChatGPT가 터지면서 세상이 바뀌었다. 클라우드 AI 시대의 개막이었고, NVIDIA는 그 중심에 있었다. FY2023 데이터센터 매출은 $47B, FY2024엔 $93B, FY2026엔 **$193.7B**으로 폭발했다. 3년 만에 4배. 연간 성장률 68%.

하지만 이 숫자는 모두 "클라우드 안에서" 일어난 일이다. 훈련(Training)이 AI 산업의 전부인 시절이었다. GPT를 훈련시키기 위해 수만 개의 GPU를 데이터센터에 쌓았다. 그리고 지금, 구조가 바뀌고 있다. 추론(Inference)이 훈련을 앞지르는 시대가 됐다. AI를 쓰는 비용이 만드는 비용보다 커지는 전환점이다. NVIDIA가 직접 "인퍼런스 인플렉션"이라 부르는 이 변곡점에서, AI의 다음 물리적 목적지는 세 곳이다: **로봇, 공장, 개인 디바이스**.

Physical AI 매출은 FY2026 기준 **$6B**. 총 매출 $215.9B의 3%에 불과하다. 하지만 지금의 스마트폰 AP 시장을 보라. 2007년 아이폰이 처음 나왔을 때, 스마트폰 프로세서 시장은 PC 시장의 소수점이었다. 10년 뒤, 퀄컴의 ARM칩은 인텔의 x86보다 더 많이 팔렸다. MarketsandMarkets 예측에 따르면 Physical AI 시장은 2026년 **$1.5B에서 2032년 $15.24B**으로 성장하며, CAGR 47.2%를 기록할 전망이다. AI 기반 산업용 로봇만 따로 보면 2026년 $17.9B에서 2035년 $33.3B으로 두 배 가까이 성장한다(GMInsights).

Vera Rubin은 이 전환의 인프라다. NVIDIA가 2026년 하반기 양산을 시작하는 차세대 플랫폼으로, 336억 트랜지스터, 50 PFLOPs 추론 성능(Blackwell 대비 5배), HBM4 최대 288GB. NVL72 랙 하나가 3.6 EFLOPS의 추론 성능을 내면서 토큰 비용을 Blackwell 대비 **10배 낮춘다**. 추론 시대가 오면 이 숫자가 AI 경제학의 핵심이 된다.

---

## 로봇 패권 지도: 미국이 OS를 쥐고, 중국이 몸통을 만들고, 한국이 열쇠를 쥔 자리

Physical AI 지도는 기묘하게 분열되어 있다. 미국은 플랫폼을, 중국은 하드웨어를, 한국은 그 사이에 끼어 있다.

**미국**: NVIDIA가 로봇 OS를 장악하려 한다. Isaac + Cosmos + GR00T 스택은 구글 Android가 스마트폰을 점령한 방식을 모방한다. 로봇 개발자 200만 명이 이미 Isaac 플랫폼 위에 있고, NVIDIA가 Hugging Face의 LeRobot과 통합하면서 1,300만 AI 빌더를 로봇 개발 생태계로 끌어들였다. Figure, Agility, Boston Dynamics, FANUC, KUKA, ABB, Universal Robots, YASKAWA까지 — 전 세계 로봇 기업들이 NVIDIA 스택을 표준으로 받아들이고 있다. TechCrunch가 "NVIDIA wants to be the Android of generalist robotics"라 쓴 건 농담이 아니다.

**한국**: 오늘 타이베이에서 가장 바빠진 나라다. 젠슨 황은 오늘 저녁 "Korea Partner Night"를 열어 삼성·SK·현대차·LG·네이버 대표단을 한자리에 불러모은다. 이미 확정된 숫자들이 있다: 한국 기업들이 NVIDIA GPU **26만 개**를 배치한다. 삼성 5만 개+, SK 5만 개+, 현대차 5만 개+, 네이버 6만 개+. 총 투자액은 ₩14.8조(약 $7.8~10.4B)다. 이 중 현대차-NVIDIA Physical AI 파트너십만 **$3B**으로 따로 발표됐다. 제조 자동화, 자율주행, 로봇을 한 번에 학습·검증·배포하는 통합 시스템이다. 코스피는 이 소식에 8,500, 이어 8,600을 돌파했다.

한국은 왜 중요한가. Boston Dynamics는 현대차 계열사다. Atlas 전기형의 2026년 생산분은 이미 전량 현대차·Google DeepMind 파트너에 배정됐다. 현대차는 2028년까지 연 3만 대 규모 로봇 생산 공장을 미국에 짓는다. 삼성전자는 HBM(고대역 메모리)을 만드는데, Jetson Thor부터 Vera Rubin까지 모든 NVIDIA AI 칩의 핵심 부품이 HBM이다. SK하이닉스는 Vera Rubin에 들어가는 HBM4를 공급한다. LG는 올해 초 CES에서 가사도우미 휴머노이드 CLOi를 공개했고, 이번 협상에서 Physical AI 플랫폼 채택을 논의 중이다.

**중국**: 하드웨어는 이미 중국이 지배하고 있다. TrendForce 보고서(2026년 4월)에 따르면 글로벌 휴머노이드 로봇 2026년 출하 50,000대+에서 Unitree + AgiBot이 **80%를 점유**한다. 중국 전체 생산량은 올해 **+94%** 급증 중이다. Unitree는 2025년에 5,500대를 팔았고, 2026년엔 1만~2만 대를 목표로 한다. G1 로봇 가격은 $16,000. 미국 경쟁사들의 1/5 수준이다. 그리고 오늘 NVIDIA가 Unitree를 선택해 첫 오픈 휴머노이드 레퍼런스 파트너로 삼았다. 아이러니하게도, 미국의 AI OS가 중국의 로봇 몸통에 얹혀 세계 시장을 공략하는 구도다.

**일본·유럽**: FANUC, YASKAWA(일본), ABB, KUKA(독일·스위스)는 산업용 로봇의 오랜 강자들이다. IFR 데이터를 보면 2024년 글로벌 산업 로봇 설치 54만 2,000대, 가동 재고 466만 대, 시장 가치 **$16.7B**이다. 이 기업들이 NVIDIA Isaac 위로 올라오고 있다는 게 핵심이다. FANUC은 GTC에서 NVIDIA 스택 위에 AI 로봇을 시연했고, ABB와 KUKA도 Physical AI 파트너십에 합류했다. 전통 산업 로봇 강자들의 AI 업그레이드가 시작됐다.

---

## 3%의 역설 — 이 내러티브가 틀릴 수 있는 이유

Physical AI를 두고 가장 솔직한 반론은 숫자에서 나온다. NVIDIA FY2026 Physical AI 매출은 **$6B**. 전체 $215.9B의 **2.8%**다. 데이터센터 $193.7B에 비하면 소수점 수준이다. Motley Fool이 직접 제목으로 "Physical AI Is Less Than 3% of Nvidia's Revenue"를 달았다.

세 가지 구조적 우려가 있다.

**첫째, ASP(평균 판매가) 딜레마.** H100 GPU 한 장이 $40,000이다. Blackwell이 매진이라는 뉴스가 NVIDIA 주가를 올린 이유다. 그런데 로봇에 들어가는 Jetson Thor는 수십~수백 달러 레인지에 있다. 로봇 100만 대가 팔려도 GPU 수만 장 파는 데이터센터 매출엔 한참 못 미친다. 스마트폰 프로세서의 역사가 증거다. ARM칩이 전 세계 스마트폰에 깔렸지만, 퀄컴의 마진은 데이터센터 칩만큼 두껍지 않다.

**둘째, 중국 하드웨어 상품화 리스크.** Unitree G1이 $16,000인데, 앞으로 양산이 붙으면 $8,000, $5,000이 될 수 있다. 하드웨어가 상품화되면 소프트웨어가 가치를 흡수하는 게 정상적인 사이클이지만, 중국은 Huawei Ascend로 자체 AI 스택 구축도 진행 중이다. 미국 제재 속에서도 중국이 완전한 독자 Physical AI 생태계를 만든다면 NVIDIA의 "Android 전략"은 중국 시장에서 작동하지 않는다.

**셋째, 기술 성숙도.** 오늘 COMPUTEX에서 공개된 GR00T N1.7은 상업 라이선스가 나왔지만, 실제 공장·병원·가정에서 *안전하게* 작동하는 수준은 다른 이야기다. GR00T N2는 여전히 "연내 출시 예정"으로, 개발 중이다. 산업 현장 배포는 안전 검증만으로도 2~3년이 더 걸린다. "Physical AI 원년"은 상징이지, 매출 원년은 아닐 수 있다.

그리고 마지막으로 에너지다. AI가 모든 물리 장치에 탑재되면 전력 소비가 기하급수적으로 늘어난다. 지금도 데이터센터 전력 수요는 IEA 기준 2025년 대비 2030년 두 배가 전망된다. 여기에 수백만 대의 로봇이 추론을 돌리면 그리드가 버티는가. Physical AI의 속도는 결국 에너지 인프라가 결정할 수 있다.

---

## 머뉴가 보는 투자 지도: OS를 사거나, 부품을 사거나

Physical AI에 베팅하는 방법은 크게 세 가지다.

**① 플랫폼(OS)에 베팅: $NVDA**
Cosmos, Isaac, GR00T의 "Android of Robotics" 전략이 실현되면, 로봇 1대당 몇 달러짜리 칩보다 로봇 1대당 수십~수백 달러의 소프트웨어·플랫폼 수수료가 더 클 수 있다. 단기 카탈리스트는 6/3(D+2) Blackwell 수요·Physical AI 가이던스가 포함될 $AVGO Q2 어닝. Vera Rubin이 2H 2026 양산에 돌입하면 2027년 $1T 수요의 물꼬가 열린다. 단, 현재 $NVDA의 데이터센터 193.7B vs Physical AI 6B 구도를 잊지 말 것. 지금 주가는 Physical AI 프리미엄을 얼마나 반영하는가를 먼저 따져야 한다.

**② 부품·픽앤샤블: 삼성전자·SK하이닉스·$AVGO·$MRVL**
로봇에 AI가 들어가든, 데이터센터가 커지든 모두 HBM이 필요하다. Vera Rubin은 HBM4, Jetson Thor는 128GB 통합 메모리다. SK하이닉스는 NVIDIA HBM4 최대 공급사이고, 삼성은 AI 팩토리 5만 개 GPU를 직접 운용하면서 제조 AI 노하우까지 쌓는다. 한국은 플랫폼 게임에서 지더라도 부품 게임에선 이미 이기고 있다.

**③ Physical AI 직접 수혜주: 현대차 그룹**
Jensen Huang이 어제 한국 4대 그룹 중 특히 현대차 정의선 회장을 직접 만났다. Boston Dynamics + $3B NVIDIA 파트너십 + 2028년 연 3만 대 로봇 공장. 한국 기업 중 Physical AI 스토리가 가장 직접적이다. 단, 현재 주가에 이미 얼마나 선반영됐는지, 2028년 배포 타임라인이 예상대로 가는지가 진입 조건이다.

**체크포인트**: ① 6/3 $AVGO 어닝에서 Physical AI 파이프라인 수치 공개 여부 ② GR00T N2 정식 출시 타이밍 (연내) ③ Unitree H2 Plus 실제 배송 시작 (2026년 후반) ④ NVIDIA 내년 어닝에서 Physical AI 매출 비중 변화. 3%가 5%로 가는 순간, 이 이야기는 진짜가 된다.

AI가 몸을 얻는다. 오늘 타이베이에서 선언됐다. 이제 남은 질문은 하나다 — 그 몸이 수익을 내기까지 얼마나 기다려야 하는가.

---

## 출처

- [NVIDIA GTC Taipei 2026 Keynote](https://www.nvidia.com/en-tw/gtc/taipei/keynote/) — 키노트 공식 페이지
- [NVIDIA Newsroom — Physical AI Models & Partners](https://nvidianews.nvidia.com/news/nvidia-releases-new-physical-ai-models-as-global-partners-unveil-next-generation-robots) — Cosmos 3, GR00T N1.7 공식 발표
- [NVIDIA Newsroom — Physical AI Real World](https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world) — 글로벌 로봇 파트너
- [Hugging Face — GR00T N1.7 블로그](https://huggingface.co/blog/nvidia/gr00t-n1-7) — GR00T N1.7 스펙
- [Unitree H2 Plus PRNewswire](https://www.prnewswire.com/news-releases/unitree-announces-h2-plus-an-nvidia-isaac-gr00t-reference-humanoid-robot-for-academic-research-302786748.html) — Isaac GR00T Reference Humanoid
- [CNBC — Unitree 파트너십](https://www.cnbc.com/2026/06/01/nvidia-unitree-humanoid-robotics-system-researchers.html) — Unitree H2 Plus 상세
- [NVIDIA SEC ARS FY2026](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000038/a2026-annualxreportxwebxfi.pdf) — FY2026 재무 데이터 (1차 자료)
- [NVIDIA South Korea IR](https://nvidianews.nvidia.com/news/south-korea-ai-infrastructure) — 한국 파트너십 공식 발표 (1차 자료)
- [Seoul Economic Daily — Korea Partner Night](https://en.sedaily.com/finance/2026/05/31/jensen-huang-to-meet-koreas-top-4-conglomerates-on-ai-chips) — 한국 기업 미팅
- [Data Center Dynamics — Korea GPUs](https://www.datacenterdynamics.com/en/news/nvidia-to-deploy-more-than-250000-gpus-across-south-korea-with-samsung-sk-group-and-hyundai-all-announcing-ai-factories/) — 26만 개 GPU 배치
- [TrendForce — 중국 휴머노이드 2026](https://www.trendforce.com/presscenter/news/20260409-13007.html) — +94% 생산 증가 (1차 자료)
- [MarketsandMarkets — Physical AI Market](https://www.prnewswire.com/news-releases/physical-ai-market-worth-15-24-billion-by-2032---exclusive-report-by-marketsandmarkets-302732794.html) — $15.24B 시장 전망 (1차 자료)
- [IFR World Robotics 2025](https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years) — 산업 로봇 542K대, $16.7B (1차 자료)
- [IFR Top 5 Trends 2026](https://ifr.org/ifr-press-releases/news/top-5-global-robotics-trends-2026) — 2026 로봇 트렌드 (1차 자료)
- [Tom's Hardware — Vera Rubin NVL72](https://www.tomshardware.com/pc-components/gpus/nvidia-launches-vera-rubin-nvl72-ai-supercomputer-at-ces-promises-up-to-5x-greater-inference-performance-and-10x-lower-cost-per-token-than-blackwell-coming-2h-2026) — Vera Rubin 스펙
- [NVIDIA Developer Blog — Vera Rubin Platform](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/) — Vera Rubin 기술 문서 (1차 자료)
- [Tom's Hardware — RTX Spark](https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory) — RTX Spark 스펙
- [TechCrunch — Android of Robotics](https://techcrunch.com/2026/01/05/nvidia-wants-to-be-the-android-of-generalist-robotics/) — NVIDIA 로봇 전략
- [Motley Fool — Physical AI 3%](https://www.fool.com/investing/2026/03/04/buy-nvidia-stock-physical-ai-transformation-2035/) — 반대 시각 출처
