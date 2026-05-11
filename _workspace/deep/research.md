# 리서치 노트 — ASIC 슈퍼사이클: 빅테크의 NVIDIA 탈출과 AI 칩 다극화
## 작성일: 2026-05-11

---

## ✅ 1차 자료 인용 현황 (7건 / 최소 3건 기준 충족)

1. **Broadcom FY2025 10-K (SEC EDGAR)** — 2025-12-18 제출
   URL: https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm
   → 총매출 $63.9B (+24% YoY), 반도체 부문 +22%, AI 반도체 Q4 +74% YoY

2. **TSMC Q1 2026 실적발표 어닝콜 트랜스크립트** — 2026-04-16
   URL: https://www.investing.com/news/transcripts/earnings-call-transcript-tsmcs-q1-2026-shows-strong-growth-and-margin-gains-93CH-4617167
   → Q1 매출 $35.9B (+40.6% YoY), 총이익률 66.2%, FY2026 가이던스 >30% USD 성장
   → CC Wei: "아젠틱 AI 전환이 추론 토큰 소비를 급격히 늘려 최첨단 실리콘 수요를 지지"

3. **Google 공식 클라우드 블로그 — Ironwood TPU 발표** — 2025-11-06
   URL: https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads
   → 4.6 PFLOPS/칩, 9,216칩 Superpod=42.5 엑사플롭스, Anthropic 100만 TPU 계약

4. **Meta 공식 뉴스룸 — MTIA 커스텀 실리콘 확장 발표** — 2026-03-11
   URL: https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/
   URL: https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/
   → MTIA 300/400/450/500 4세대 동시 발표, 6개월 출시 주기, RISC-V, TSMC 제조

5. **Microsoft 공식 블로그 — Maia 200 발표** — 2026-01-26
   URL: https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/
   → TSMC 3nm, 140B 트랜지스터, 10 PFLOPS FP4, 216GB HBM3e, 750W, Iowa 배포 완료

6. **TrendForce 2026 Cloud AI Outlook 보고서**
   URL: https://www.trendforce.com/research/download/RP251105VO
   → ASIC 성장률 44.6% vs GPU 16.1% (2026), 2028년 ASIC 출하량이 GPU 추월

7. **Bloomberg Intelligence AI 가속기 시장 보고서**
   URL: https://www.bloomberg.com/company/press/ai-accelerator-market-looks-set-to-exceed-600-billion-by-2033-driven-by-hyperscale-spending-and-asic-adoption-according-to-bloomberg-intelligence/
   → AI 가속기 시장 $604B by 2033, ASIC 비중 8%(2024)→19%(2033), CAGR 27%

---

## 핵심 팩트 데이터베이스

### A. 시장 규모 및 성장률

| 지표 | 수치 | 출처 |
|------|------|------|
| AI 칩 시장 규모 (2024) | $85B | Statista |
| AI 칩 시장 규모 (2025) | $127.7B | 글로벌 리서치 |
| AI 칩 시장 규모 (2035 전망) | $745.8B | 코히어런트마켓인사이츠 |
| AI 가속기 시장 (2033 전망) | $604B | Bloomberg Intelligence |
| ASIC 성장률 2026 | 44.6% | TrendForce |
| GPU 성장률 2026 | 16.1% | TrendForce |
| ASIC 시장 비중 2024 | 8% | Bloomberg Intelligence |
| ASIC 시장 비중 2033 전망 | 19% | Bloomberg Intelligence |
| 2028년 ASIC가 GPU 출하량 추월 예상 | — | TrendForce |
| 하이퍼스케일러 2026 총 capex | $660~690B | 업계 추산 |
| 이 중 AI 인프라 비중 | 75% | 업계 추산 |

### B. NVIDIA 시장 점유율 변화

| 시기 | AI 가속기 점유율 | 주요 배경 |
|------|----------------|----------|
| 2024 peak | ~87% | Hopper H100 독점 |
| 2025 | ~80% | H200·Blackwell 전환기 |
| 2026 (전망) | ~75% | ASIC 본격화 |
| 2028 (전망) | 더 낮아질 것 | ASIC 출하량이 GPU 추월 |
| 훈련(Training) 점유율 | ~90% | CUDA 생태계 락인 |
| 추론(Inference) 점유율 | 60~75% | 커스텀 실리콘 압박 |

출처: Silicon Analysts, TrendForce, Bloomberg Intelligence

### C. 각 기업별 커스텀 칩 현황

**① Google Ironwood (TPU v7)**
- 칩당 성능: 4.6 PFLOPS FP8, 메모리: 192GB HBM3e, 7.4TB/s, TDP 600W
- Superpod: 9,216칩 → 42.5 엑사플롭스, HBM 1.77PB
- 이전 세대 대비: TPU v5p 대비 10배, v6e 대비 4배
- **핵심 고객**: Anthropic — 100만 TPU 계약 (400K 직구 ~$10B + 600K GCP $42B RPO)
- 출처: Google Cloud 공식 블로그 (2025-11-06)

**② Meta MTIA (2026-03-11 발표)**
- MTIA 300: 1.2 PFLOPS FP8, 216GB HBM, 800W, RISC-V, 현재 양산 중
- MTIA 400: 6.0 PFLOPS FP8, 288GB HBM, 1200W, 배포 임박
- MTIA 450: 7.0 PFLOPS FP8, 288GB HBM, 1400W, 2027년 초 양산
- MTIA 500: 10.0 PFLOPS FP8, 384~512GB HBM, 1700W, 2027년 초 양산
- 전략: 6개월 출시 주기, TSMC 제조, 동일 섀시/랙 호환
- 출처: Meta 공식 뉴스룸 (2026-03-11)

**③ Amazon Trainium 3 (2025-12 출시)**
- 공정: TSMC 3nm
- 성능: 2.52 PFLOPS FP8, 144GB HBM3e, 4.9TB/s
- UltraServer: 144칩 = 362 MXFP8 PFLOPS, 706TB/s, 20.7TB HBM3e
- Trainium 2 대비 4.4배 성능, 4배 에너지 효율

**④ Microsoft Maia 200 (2026-01-26)**
- 공정: TSMC 3nm, 140B 트랜지스터
- 성능: 10 PFLOPS FP4, 5 PFLOPS FP8, 216GB HBM3e, 7TB/s, 750W TDP
- HBM 독점 공급: SK하이닉스
- 배포: Iowa 데이터센터 → OpenAI GPT-5.2 구동 중
- Trainium 3 대비 FP4 3배, 기존 Azure 하드웨어 대비 가격성능비 30% 개선

**⑤ OpenAI 커스텀 ASIC (2026 H2 양산 예정)**
- Broadcom + TSMC 3nm, $10~18B 규모, 내부 추론 전용

### D. Broadcom (AVGO) 상세

| 지표 | 수치 | 비고 |
|------|------|------|
| FY2025 총매출 | $63.9B | +24% YoY |
| FY2025 AI 반도체 매출 (Q4) | +74% YoY | 최근 분기 |
| Q1 FY26 AI 매출 | $8.4B | +106% YoY |
| Q2 FY26 AI 매출 가이던스 | $10.7B | |
| FY2026 AI 매출 목표 | $40.4B | |
| AI 수주잔고 | $73B | 2026 현재 |
| ASIC 시장 점유율 | 60~70% | |
| 5번째 XPU 고객 | $1B 초기 주문 | 2026 H2 |
| TAM 목표 | $60B | 2026 기준 |

주요 고객: Google, Meta, Anthropic, OpenAI(예정), Apple(검토), xAI(검토)
출처: Broadcom FY2025 10-K (SEC EDGAR)

### E. TSMC

| 지표 | 수치 | 비고 |
|------|------|------|
| Q1 2026 매출 | $35.9B | +40.6% YoY |
| Q1 2026 총이익률 | 66.2% | +3.9%p QoQ |
| Q1 2026 영업이익률 | 58.1% | |
| Q2 2026 가이던스 | $39~40.2B | |
| 2026 capex 계획 | $52~56B (상단) | |
| 2026 전체 매출 성장률 | >30% USD | 가이던스 상향 |

### F. 한국 HBM — ASIC 슈퍼사이클의 숨은 수혜자

| 지표 | SK하이닉스 | 삼성전자 |
|------|-----------|---------|
| HBM 시장 점유율 (2025) | 62% (출하), 57% (매출) | 2위 |
| 2026 생산 증가율 | 4배 이상 투자 | ~50% 증산 |
| ASIC용 HBM 수요 증가율 | +82% 전망 | +82% 전망 |
| Maia 200 HBM 독점 공급 | SK하이닉스 | — |

출처: TrendForce (2026-01), Seoul Economic Daily (2026-03-12)

### G. 중국 화웨이 Ascend 현황

| 모델 | 성능 | 2026 생산 목표 | 비고 |
|------|------|--------------|------|
| Ascend 910C | H100 대비 ~80% (SMIC 7nm) | 60만 개 | 현재 주력 |
| Ascend 950PR | 1.56 PFLOPS FP4 (H20 대비 2.8배) | 75만 개 | ByteDance $5.6B 주문 |

SMIC 7nm 한계로 전력 효율 열세. 화웨이 CUDA 호환 소프트웨어 스택 개발 중.
출처: Bloomberg (2025-09-29)

### H. 추론 경제학 — ASIC 비용 우위의 실제 근거

1. 추론 = AI 컴퓨트의 2/3 차지 (2026), 2023년 1/3에서 급증 (Deloitte)
2. 추론 토큰 비용: $20/100만 토큰 (2022-11) → $0.07 (2024-10) = 99.6% 하락
3. 커스텀 ASIC TCO: 특정 워크로드 GPU 대비 30~50% 낮음
4. **Midjourney 실사례**: NVIDIA GPU → Google TPU 이전 후 월 비용 $210만 → $70만 (65% 절감)
5. ASIC 설계비: $1000만~$1억+ but 하이퍼스케일에서 1년 내 ROI
6. $1B 커스텀 칩 투자 → 5년간 $10B GPU 비용 절감 (10% GPU 절감 시)
출처: ARK Invest 리서치, Epoch AI Research, Silicon Analysts

### I. 미중 제네바 합의 (2026-05-10/11) — 반도체 영향

- 관세: 115%(= 91%+24%) → 30%, 90일 유예 합의
- 반도체 수출 통제: 별도 지속 (H20 이하 제한적 허용)
- TSMC 수혜: 하이퍼스케일러 공급망 불확실성 감소
- AVGO 수혜: 고객사 공급망 비용 절감
- ASML: 중국 매출 여전히 제한적이나 분위기 전환
출처: White House 브리핑 (2026-05-10), USTR

---

## 시계열 핵심 데이터 (1년/3년/10년)

### 10년 추이: NVIDIA 데이터센터 매출
- 2016: ~$0.3B (데이터센터 여명기)
- 2019: $2.9B (클라우드 GPU 수요 태동)
- 2022: $15.0B (ChatGPT 이전, 암호화폐+AI 혼재)
- 2023: $47.5B (ChatGPT 이후 대폭발)
- 2024 (FY25): $100B+ (B100 Blackwell 전환)
- 2026 (FY26): $130B+ (Blackwell 풀 램프)

### 3년 추이: ASIC 비중
- 2023: AI 가속기 시장 내 ASIC 비중 <5%
- 2024: ~8%
- 2026: ~12~15% 추정
- 2028 (전망): GPU 출하량 추월

### 1년 추이: Broadcom AI 매출 분기별
- Q4 FY24 (2024-11): $6.5B (전년比 +74%)
- Q1 FY25 (2025-02): AI 매출 성장 가속
- Q1 FY26 (2026-02): $8.4B (+106% YoY)
- Q2 FY26 (2026-05): 가이던스 $10.7B

### 추론 비용 곡선 (5년)
- 2022-11: $20/100만 토큰
- 2023: ~$5/100만 토큰
- 2024-10: $0.07/100만 토큰
- 2026 (추정): $0.01 미만

