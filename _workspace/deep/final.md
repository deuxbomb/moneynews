# NVIDIA가 AI를 빛으로 연결한다 — 72억 달러로 시작된 구리 시대의 종말

> 2026년 5월 7일 | 머뉴 딥다이브 | 🔍 딥 리서치

---

## NVIDIA 랙 안에 구리 케이블 5,000개가 있다

NVIDIA의 차세대 AI 슈퍼컴퓨터 '베라 루빈(Vera Rubin)' 랙 한 대 안에는 구리 케이블이 5,000개 들어 있습니다. GPU와 GPU를, 칩과 칩을 연결하는 이 케이블들은 지금껏 AI 공장의 혈관 역할을 해왔죠. 그런데 이 혈관이 막히기 시작했습니다.

AI 모델이 커질수록, GPU 클러스터가 거대해질수록, 전기 신호를 구리 선을 통해 주고받는 방식의 물리적 한계가 드러났습니다. 데이터센터는 미국 신규 전력 수요 증가분의 절반을 홀로 집어삼키고 있고, 구리 가격은 2026년 1월 파운드당 6달러로 사상 최고를 찍었습니다. 업계는 올해 구리 공급이 15만 톤 부족할 것으로 전망하는데, 이는 불과 1년 전만 해도 20만 톤 흑자를 예상하던 것에서 완전히 방향이 바뀐 겁니다.

NVIDIA는 이 문제를 누군가 해결해주기를 기다리지 않았습니다. 지난 3개월 동안 72억 달러를 광학·포토닉스 기업 3곳에 직접 쏟아부었습니다 — 2036년 CPO 시장 전체 예상 규모(200억 달러)의 3분의 1 이상을 오늘의 공급망 선점에 미리 투입한 셈입니다. 구리의 시대를 끝내기 위해서요.

---

## 3개월 동안 쌓아 올린 광학 제국

젠슨 황이 광학 인프라 투자에 본격적으로 나선 건 2026년 3월 2일입니다. NVIDIA가 Coherent와 Lumentum에 각각 20억 달러씩, 총 40억 달러를 투자하겠다고 발표했죠. 단순한 지분 투자가 아니었습니다. 다년간 구매 약정과 생산 용량 우선 접근권이 묶인, 사실상 "이 회사 생산 라인을 내 것으로 쓰겠다"는 선언이었습니다. 발표 당일 Lumentum은 12%, Coherent는 15% 급등했습니다.

NVIDIA가 부품 공급망을 틀어쥐는 사이, 제조 생태계도 함께 움직이기 시작했습니다. 5월 4일, 반도체 파운드리 GlobalFoundries가 AI 데이터센터용 co-packaged optics 솔루션 'SCALE'을 공개하며 업계 최초로 OCI MSA(광학 컴퓨트 인터커넥트 다중 소스 협약) 지원 플랫폼임을 선언했습니다. 광학 인터커넥트 생태계가 속도를 내기 시작한 거죠.

그리고 이틀 뒤인 5월 6일. NVIDIA가 코닝(Corning)과의 장기 파트너십을 발표하며 시장을 다시 한 번 뒤흔들었습니다. 최대 32억 달러를 투자해 노스캐롤라이나와 텍사스에 첨단 제조 공장 3개를 세우겠다는 내용이었습니다. 코닝의 미국 내 광학 커넥티비티 제조 용량을 10배, 광섬유 생산 용량을 50% 이상 끌어올리는 게 목표입니다. 3,000개 이상의 신규 일자리도 약속됐습니다.

코닝 주가는 장중 20.8% 치솟았고, NVIDIA도 5.41% 올랐습니다. 코닝은 이미 지난 1년간 250% 이상 주가가 뛴 상태였는데도요.

---

## 젠슨 황이 말한 "빛의 속도"의 의미

젠슨 황 CEO는 이날 발표에서 이렇게 말했습니다.

> "AI는 우리 시대 최대의 인프라 구축을 이끌고 있습니다. 코닝과 함께 우리는 광학 기술로 컴퓨팅의 미래를 발명하고 있습니다 — 지능이 빛의 속도로 이동하는 AI 인프라의 토대를 쌓고 있죠."

*(원문: 영어 — 번역)*

"빛의 속도"는 수사가 아닙니다. 글자 그대로의 물리학입니다. 코닝이 만드는 광섬유 케이블은 데이터를 전자(electron) 대신 광자(photon)로 전달합니다. 광자를 움직이는 데 필요한 에너지는 전자 대비 5~20배 적습니다. 전력 효율이 5배 개선되는 겁니다. 수천 개의 GPU가 기가와트 단위 전력을 쓰는 AI 공장에서 이 차이는 어마어마합니다.

더 중요한 건 속도와 거리입니다. 광섬유는 구리보다 신호 손실이 훨씬 적어, 데이터센터 안에 수십만 개의 GPU가 빼곡히 들어설 때도 안정적인 통신을 유지할 수 있습니다. 구리 케이블은 길이가 길어질수록 신호 품질이 떨어지는 반면, 광섬유는 같은 용량으로 훨씬 먼 거리를 커버합니다.

---

## 구리의 한계, 광학의 기회: CPO가 뭔가요

이 혁명의 핵심 기술은 **CPO(Co-Packaged Optics, 공동 패키지 광학)**입니다. 어렵게 들리지만 핵심 아이디어는 간단합니다. 기존에는 GPU에서 나온 전기 신호가 '트랜시버'라는 별도 부품에서 광학 신호로 바뀌어 광섬유를 타고 이동했습니다. CPO는 이 변환 과정을 칩 패키지 내부로 집어넣습니다. 전기-광학 변환이 일어나는 경로를 극도로 단축해, 신호 손실과 전력 낭비를 동시에 줄이는 거죠.

NVIDIA의 Quantum-X InfiniBand 스위치는 이 방식으로 초당 115 테라비트(115 Tb/s)의 처리량을 실현합니다. 800 Gb/s 포트 144개를 동시에 운영하는 셈입니다. NVIDIA Spectrum-X Ethernet Photonics는 2026년 하반기 상용화가 예정돼 있습니다.

CPO는 NVIDIA만의 실험이 아닙니다. 브로드컴의 Tomahawk 6-Davisson은 TSMC의 COUPE(Compact Universal Photonic Engine) 기술로 포토닉 엔진을 스위칭 실리콘과 통합해 102.4 Tbps 용량으로 이미 양산 출하 중입니다. 전력 소비는 기존 플러거블 방식 대비 70% 감소. CPO는 이제 특정 기업의 실험적 기술이 아니라 AI 인프라의 새 표준으로 자리 잡고 있습니다.

시장 조사 기관들은 CPO 시장이 2026~2036년 연평균 37%로 성장해 2036년 200억 달러를 넘어설 것으로 전망합니다. McKinsey는 하이퍼스케일러들이 2029년까지 백엔드 광학 장비의 87%를 800G 이상으로 전환할 것으로 예상합니다. 문제는 공급이 수요를 못 따라간다는 거죠 — 800G 트랜시버 공급은 2027년까지 수요 대비 40~60% 부족할 전망입니다. NVIDIA가 Coherent, Lumentum, Corning에 72억 달러를 들이붓는 이유가 바로 여기 있습니다.

---

## 코닝, 왜 이 회사가 갑자기 AI 핵심 플레이어가 됐나

코닝(Corning)이라는 회사가 낯설 수 있습니다. 이 회사는 160년 역사의 유리 기업으로, 아이폰 화면에 쓰이는 고릴라 글래스로 알려져 있습니다. 그런데 AI 인프라 붐의 최대 수혜자 중 하나로 부상했습니다.

이유는 단순합니다. 광섬유의 핵심 소재가 '유리'이기 때문입니다. 코닝은 수십 년간 전 세계 통신 네트워크에 광섬유 케이블을 공급해 온 세계 최대 광섬유 제조사입니다. AI 붐이 오자, 코닝이 가진 설비와 기술이 갑자기 핵심 자산이 됐습니다.

그 흐름을 먼저 읽은 건 Meta였습니다. 2026년 1월, Meta는 코닝과 최대 60억 달러 규모의 다년간 광섬유 케이블 공급 계약을 맺었습니다. AI 데이터센터가 기존 클라우드 인프라보다 훨씬 많은 광섬유를 필요로 한다는 판단이었죠. 코닝은 이에 맞춰 AI 전용 소형 고밀도 광섬유 케이블 'Contour'를 출시했고, 노스캐롤라이나 히코리 공장 대규모 확장에 착공(2026년 3월)했습니다.

그리고 4개월 뒤, NVIDIA가 두드렸습니다. Meta가 다년간 최대 60억 달러 계약으로 코닝을 먼저 선점했다면, NVIDIA는 최대 32억 달러 파트너십으로 그 방향을 AI 인프라의 표준으로 봉인한 셈입니다. 코닝 주가가 1년 만에 250%+를 달성한 건 우연이 아닙니다.

---

## 이 판에서 투자자가 봐야 할 지형도

$NVDA 자체는 이미 충분히 알려진 이야기입니다. 여기서 흥미로운 건 '픽앤샤블(Pick & Shovel)' 투자 아이디어입니다. 골드러시에서 진짜 돈을 번 건 금을 캔 사람이 아니라 곡괭이와 삽을 판 사람이었다는 얘기죠. AI 인프라 붐에서 코닝이 그 역할을 하고 있습니다.

현재 시장 구도를 정리하면 이렇습니다:

- **NVIDIA($NVDA)**: 광학 인터커넥트 생태계 건설의 총사령관. 72억 달러+ 투자로 공급망 직접 장악.
- **Corning(GLW)**: AI 광섬유의 '삼성전자' 같은 위치. Meta + NVIDIA 양대 메가딜. 1년 +250%.
- **Lumentum(LITE) + Coherent(COHR)**: NVIDIA가 각각 20억 달러를 베팅한 CPO 레이저/부품 공급사.
- **하이퍼스케일러($GOOGL, Meta, AWS 등)**: 수요 측. 광학 인터커넥트 전환으로 전력 비용 대폭 절감 가능.

리스크도 있습니다. CPO는 아직 대규모 양산 초기 단계입니다. 수율과 온도 관리 문제는 여전히 해결 중이고, NVIDIA의 Corning 투자는 최대 32억 달러이지만 초기 확약은 5억 달러짜리 워런트입니다. AI 투자 사이클이 꺾이면 대규모 광학 설비가 과잉 공급으로 돌변할 수도 있습니다. 인텔, AMD, Broadcom도 모두 자체 광학 솔루션을 개발 중입니다.

그러나 큰 방향은 분명합니다. "5년 안에 AI 데이터센터 인터커넥트는 모두 광학으로 전환될 것"이라는 게 업계의 합의에 가깝습니다. 72억 달러짜리 베팅을 한 젠슨 황은 이미 자기 생각을 행동으로 보여줬습니다.

---

## 머뉴's Advice 💡

**1. 코닝(GLW)을 주목하세요.** 광학 인터커넥트 전환의 가장 직접적인 수혜주입니다. Meta 60억, NVIDIA 32억 — 연이은 메가딜이 수요 가시성을 확보해줬습니다. 1년 +250%이지만, AI 공장 건설이 계속되는 한 성장 여지는 남아 있습니다.

**2. $NVDA를 단순 'AI 반도체 주'로만 보지 마세요.** NVIDIA는 지금 AI 공장의 인프라 레이어 전체를 수직 통합하고 있습니다. GPU → 네트워킹 스위치 → 광학 인터커넥트 → 광섬유 공급망까지. 단기 주가보다 이 생태계 전략의 내구성에 베팅하는 관점이 유효합니다.

**3. AI 전력 대란과 광학 전환은 같은 이야기입니다.** 구리 대체가 빨라질수록, 데이터센터의 전력 효율이 올라갑니다. $OKLO 같은 에너지 주식에 관심이 있다면, 광학 인프라 전환의 속도가 AI 발전소 수요에도 영향을 준다는 점을 기억하세요. 에너지 절약이 되면 추가 확장 여력이 생깁니다.

구리에서 광자로. 이 전환의 속도와 범위에 베팅하는 포트폴리오를 지금 구성하고 있다면 — 당신은 어느 '삽' 회사를 들고 있나요?

---

## 출처

- [CNBC](https://www.cnbc.com/2026/05/06/nvidia-corning-optical-factories-nc-texas-ai.html) — NVIDIA-Corning 파트너십 상세 보도 (2026.05.06)
- [Bloomberg](https://www.bloomberg.com/news/articles/2026-05-06/nvidia-buys-500-million-of-rights-for-stock-in-corning) — Corning 워런트 딜 구조 (2026.05.06)
- [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-and-corning-announce-long-term-partnership-to-strengthen-us-manufacturing-for-ai-infrastructure) — 공식 보도자료 (2026.05.06)
- [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-strategic-partnership-with-lumentum-to-develop-state-of-the-art-optics-technology) — NVIDIA-Lumentum 파트너십 (2026.03)
- [CNBC](https://www.cnbc.com/2026/03/02/nvidia-investment-coherent-lumentum.html) — NVIDIA $4B 포토닉스 투자 (2026.03.02)
- [SiliconANGLE](https://siliconangle.com/2026/03/02/nvidia-invests-4b-co-packaged-optics-suppliers-lumentum-coherent/) — CPO 투자 배경 분석 (2026.03.02)
- [GlobeNewswire](https://www.globenewswire.com/news-release/2026/05/04/3286711/0/en/globalfoundries-accelerates-adoption-of-co-packaged-optics-for-advanced-ai-data-centers-with-scale-optical-module-solution.html) — GlobalFoundries SCALE 발표 (2026.05.04)
- [CNBC](https://www.cnbc.com/2026/01/27/apple-supplier-corning-wins-6-billion-from-meta-for-ai-optical-fiber.html) — Meta-Corning $6B 딜 (2026.01.27)
- [Invezz](https://invezz.com/news/2026/05/06/corning-stock-surges-20-on-nvidia-deal-to-expand-ai-optical-manufacturing/) — 코닝 주가 급등 (2026.05.06)
- [NVIDIA Technical Blog](https://developer.nvidia.com/blog/scaling-ai-factories-with-co-packaged-optics-for-better-power-efficiency/) — CPO 기술 설명
- [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-spectrum-x-co-packaged-optics-networking-switches-ai-factories) — Spectrum-X CPO 스위치 발표
- [Broadcom IR](https://investors.broadcom.com/news-releases/news-release-details/broadcom-announces-tomahawkr-6-davisson-industrys-first-1024) — Tomahawk 6-Davisson CPO 양산 출하 (2025.10.08)
- [Tom's Hardware](https://www.tomshardware.com/tech-industry/ai-data-center-buildout-pushes-copper-toward-shortages-analysts-warn) — 구리 부족 분석
- [Fortune](https://fortune.com/2026/04/20/us-data-center-electricity-demand-public-opinion/) — 데이터센터 전력 수요
