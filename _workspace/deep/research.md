# 딥다이브 리서치 노트

## 테마
NVIDIA 광학 제국 건설 — 구리 시대의 종말과 포토닉스 AI 인프라의 부상

## 유형
🔍 딥 리서치 (소스 8개 이상 수렴, 구조적 산업 전환 기획기사)

## 선정 이유
NVIDIA가 2026년 3~5월, 3개월 사이에 광학/포토닉스 기업 3곳(Coherent, Lumentum, Corning)에 총 72억 달러 이상을 투자했다. 각각의 딜은 개별 뉴스로 보도됐지만, 묶어서 보면 AI 인프라의 물리적 한계(구리의 한계)를 해결하는 NVIDIA의 체계적 전략이 드러난다. 2026년 5월 6일 Corning 딜 발표 당일 이를 심층 분석할 최적의 타이밍.

---

## 팩트 (출처 필수)

### NVIDIA-Corning 딜 (2026년 5월 6일)
1. NVIDIA가 코닝(Corning)에 최대 32억 달러를 투자하는 장기 파트너십 계약 체결. 초기 5억 달러로 코닝 주식매수청구권(warrant) 확보: 주당 180달러에 최대 1,500만 주 매수 가능한 워런트 + 300만 주에 대한 사전납입 워런트. — 출처: [CNBC](https://www.cnbc.com/2026/05/06/nvidia-corning-optical-factories-nc-texas-ai.html) / [Bloomberg](https://www.bloomberg.com/news/articles/2026-05-06/nvidia-buys-500-million-of-rights-for-stock-in-corning)

2. 코닝은 노스캐롤라이나·텍사스에 3개의 신규 첨단 제조 공장 건설. 미국 내 광학 커넥티비티 제조 용량 **10배** 확대, 광섬유 생산 용량 **50% 이상** 확대. 신규 일자리 3,000개 이상 창출. — 출처: [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-and-corning-announce-long-term-partnership-to-strengthen-us-manufacturing-for-ai-infrastructure) / [Corning IR](https://investor.corning.com/news-and-events/news/news-details/2026/05/default.aspx)

3. 코닝 주가는 발표 당일 장중 최대 **+20.8%** 급등, 종가 기준 약 +14% 마감. 코닝 주가는 발표 전 1년간 이미 **250%** 이상 상승한 상태. — 출처: [Invezz](https://invezz.com/news/2026/05/06/corning-stock-surges-20-on-nvidia-deal-to-expand-ai-optical-manufacturing/) / [NAI500](https://nai500.com/blog/2026/05/beyond-the-nvidia-hype-corning-stock-has-trounced-top-semiconductor-peers-this-year/)

4. NVIDIA 주가는 발표 당일 **+5.41%** 상승. — 출처: [Yahoo Finance 검색결과](https://finance.yahoo.com/quote/NVDA/)

### NVIDIA의 광학 투자 패턴 (3개월 연속)
5. 2026년 3월 2일: NVIDIA가 Coherent와 Lumentum에 각각 **20억 달러, 총 40억 달러** 투자 발표. 다년간 구매 약정 + 생산 용량 우선 접근권 포함. Lumentum +12%, Coherent +15% 급등. — 출처: [CNBC](https://www.cnbc.com/2026/03/02/nvidia-investment-coherent-lumentum.html) / [SiliconANGLE](https://siliconangle.com/2026/03/02/nvidia-invests-4b-co-packaged-optics-suppliers-lumentum-coherent/)

6. 2026년 5월 4일: GlobalFoundries가 AI 데이터센터용 co-packaged optics 솔루션 'SCALE' 발표. 업계 최초 OCI MSA(Optical Compute Interconnect Multi-Source Agreement) 지원 플랫폼. — 출처: [GlobeNewswire](https://www.globenewswire.com/news-release/2026/05/04/3286711/0/en/globalfoundries-accelerates-adoption-of-co-packaged-optics-for-advanced-ai-data-centers-with-scale-optical-module-solution.html)

### Corning-Meta 선행 딜 (2026년 1월)
7. 2026년 1월 27일: Meta가 코닝과 최대 **60억 달러** 규모 다년간 광섬유 케이블 공급 계약 체결. 코닝이 노스캐롤라이나 히코리 공장을 대폭 확장. 2026년 3월 착공 시작. 코닝은 AI 데이터센터 전용 소형 고밀도 광섬유 케이블 'Contour' 출시. — 출처: [CNBC](https://www.cnbc.com/2026/01/27/apple-supplier-corning-wins-6-billion-from-meta-for-ai-optical-fiber.html) / [Corning](https://www.corning.com/worldwide/en/about-us/news-events/news-releases/2026/01/corning-and-meta-announce-multiyear-up-to-6-billion-agreement-to-accelerate-us-data-center-buildout.html)

### 기술 배경: 왜 구리에서 광섬유/CPO로
8. NVIDIA의 Vera Rubin 랙 스케일 시스템에는 현재 **구리 케이블 5,000개**가 내장. NVIDIA는 Corning의 광섬유 유리 케이블로 이를 교체하는 것을 목표로 함. — 출처: [CNBC 검색결과](https://www.cnbc.com/2026/05/06/nvidia-corning-optical-factories-nc-texas-ai.html) / [Tom's Hardware 검색결과](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-invests-usd300-million-in-corning-to-build-three-new-us-based-optical-fiber-plants-ai-infrastructure-deal-would-boost-fiber-production-capacity-by-over-50-percent)

9. Co-Packaged Optics(CPO): 광학 엔진을 칩 패키지 내부에 직접 통합하는 기술. 전기-광학 변환 병목 해소. NVIDIA CPO는 구리 대비 **전력 효율 5배** 개선. 광자(photon) 이동은 전자(electron) 이동 대비 **5~20배** 낮은 전력 사용. — 출처: [NVIDIA Technical Blog](https://developer.nvidia.com/blog/scaling-ai-factories-with-co-packaged-optics-for-better-power-efficiency/) / [EDN](https://www.edn.com/where-co-packaged-optics-cpo-technology-stands-in-2026/)

10. NVIDIA Quantum-X InfiniBand: 총 **115 Tb/s** 처리량, 800 Gb/s 포트 144개. NVIDIA Spectrum-X Ethernet Photonics: 2026년 하반기 상용화 예정. — 출처: [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-spectrum-x-co-packaged-optics-networking-switches-ai-factories)

### AI 인프라 물리적 한계 (배경 맥락)
11. AI 데이터센터가 미국 신규 전력 수요 증가분의 **50%** 차지. 구리 가격은 2026년 1월 파운드당 **6달러** 사상 최고 기록, 현재 5.61달러. 구리 공급 부족 2026년 15만 톤 예상(당초 20만 톤 흑자 전망에서 반전). — 출처: [Fortune](https://fortune.com/2026/04/20/us-data-center-electricity-demand-public-opinion/) / [Tom's Hardware 구리 기사](https://www.tomshardware.com/tech-industry/ai-data-center-buildout-pushes-copper-toward-shortages-analysts-warn)

12. 데이터센터 메가와트당 구리 **27톤** 필요. AI 데이터센터는 기존 클라우드 인프라보다 훨씬 많은 광섬유 필요. — 출처: [Tom's Hardware 구리 기사](https://www.tomshardware.com/tech-industry/ai-data-center-buildout-pushes-copper-toward-shortages-analysts-warn)

### 시장 전망
13. CPO 시장 규모: 2036년 **200억 달러** 초과 전망, 2026~2036년 CAGR **37%**. — 출처: [EDN CPO 분석](https://www.edn.com/where-co-packaged-optics-cpo-technology-stands-in-2026/)

14. McKinsey: 하이퍼스케일러가 2029년까지 백엔드 광학 장비의 **87%**를 800G 이상으로 전환 예상. 800G 트랜시버 공급이 2027년까지 수요의 40~60% 부족할 전망. — 출처: [Industrial Analyst Substack 검색결과](https://industrialanalyst.substack.com/p/the-backbone-of-ai-optical-networking)

15. 전 세계 반도체 매출 2026년 1분기 2,985억 달러, 전 분기 대비 **+25%**. 2026년 연간 9,750억 달러 예상. — 출처: [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/global-semiconductor-sales-hit-nearly-usd300-billion-in-q1-2026-chips-are-on-track-to-top-usd1-trillion-for-this-year-says-report)

---

## 직접 인용 (정확한 원문만)

1. "AI is driving the largest infrastructure buildout of our time – and a once-in-a-generation opportunity to reinvigorate American manufacturing and supply chains. Together with Corning, we are inventing the future of computing with advanced optical technologies – building the foundation for AI infrastructure where intelligence moves at the speed of light while advancing the proud tradition of Made in America." — Jensen Huang, NVIDIA CEO, NVIDIA-Corning 파트너십 발표, 2026년 5월 6일. 출처: [CNBC 검색결과](https://www.cnbc.com/2026/05/06/nvidia-corning-optical-factories-nc-texas-ai.html)

---

## 숫자 데이터 (검증 가능한 것만)

| 항목 | 수치 | 출처 |
|------|------|------|
| NVIDIA → Corning 투자 규모 | 최대 32억 달러 (초기 5억 달러 워런트) | CNBC, Bloomberg |
| NVIDIA → Coherent + Lumentum | 각 20억 달러 = 총 40억 달러 | CNBC |
| NVIDIA 광학 총 투자 (3개월) | 72억 달러+ | 합산 |
| Corning 미국 광학 생산 용량 확대 | 10배 | NVIDIA/Corning 보도자료 |
| Corning 광섬유 생산 용량 확대 | 50%+ | NVIDIA/Corning 보도자료 |
| Corning 신규 일자리 | 3,000개 이상 | NVIDIA/Corning 보도자료 |
| Corning 주가 당일 급등 | 장중 +20.8%, 종가 +14% | Invezz |
| Corning 1년 주가 상승 | +250%+ | NAI500 |
| NVDA 당일 주가 상승 | +5.41% | Yahoo Finance |
| Meta-Corning 딜 규모 | 최대 60억 달러 | CNBC |
| Vera Rubin 랙 구리 케이블 수 | 5,000개 | CNBC/Tom's Hardware |
| CPO 전력 효율 (vs 구리) | 5배 개선 | NVIDIA Technical Blog |
| 광자 vs 전자 전력 소비 | 5~20배 적음 | CNBC/Tom's Hardware |
| NVIDIA Quantum-X 처리량 | 115 Tb/s | NVIDIA Newsroom |
| CPO 시장 2036년 규모 | 200억 달러+ | EDN |
| CPO CAGR 2026~2036 | 37% | EDN |
| 800G 트랜시버 공급 부족 (2027) | 수요의 40~60% | McKinsey/산업 분석 |
| 구리 가격 최고점 (2026년 1월) | 파운드당 6달러 | Tom's Hardware |
| 구리 공급 부족 (2026) | 15만 톤 | Tom's Hardware |
| 데이터센터 메가와트당 구리 | 27톤 | Tom's Hardware |
| 미국 신규 전력 수요 중 데이터센터 비중 | 50% | Fortune |

---

## 관련 종목

- $NVDA (NVIDIA): 핵심 딜 주체. 광학 인프라 구축 리더
- $GOOGL (Alphabet): 하이퍼스케일러로 CPO 전환 수혜 기업
- Corning (GLW): 최대 수혜주, 미상장 관심 여부 무관하게 핵심 플레이어
- Lumentum (LITE): NVIDIA $20억 투자 수혜
- Coherent (COHR): NVIDIA $20억 투자 수혜

---

## 반론/리스크

1. CPO 기술 성숙도 문제: CPO는 아직 대규모 상용 배포 초기 단계. 수율, 신뢰성, 온도 관리 문제가 양산 확대 시 병목이 될 수 있음.
2. 공급 과잉 리스크: AI 인프라 투자 사이클이 꺾일 경우, 대규모 광학 설비 투자가 과잉 공급으로 전환 가능.
3. 코닝 딜 실행 불확실성: 최대 32억 달러 투자는 조건부. 초기 확약은 5억 달러 워런트. NVIDIA의 실제 구매 약정 규모에 따라 달라짐.
4. 경쟁 심화: 인텔, AMD, Broadcom 모두 광학 인터커넥트 솔루션 개발 중. NVIDIA 독주가 오래 지속되지 않을 수 있음.
