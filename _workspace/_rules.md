# 머뉴 콘텐츠 선정 규칙 v2 (2026-05-08)

이 파일은 오늘의 픽 / 뉴스 큐레이션 / 딥다이브 테마 선정의 **구조적 다양화 규칙**입니다.
모든 트리거(오전/오후/딥다이브 A)는 Step 0에서 이 파일을 읽고 본문 단계에서 참조합니다.

---

## 1. 오늘의 픽 — 와치리스트 제외 + 발굴 전용

### 절대 규칙: 와치리스트 9종목 픽 금지
다음 9개 종목은 **오늘의 픽으로 절대 선정하지 않습니다**:
$TSLA, $GOOGL, $OKLO, $NVDA, $COIN, $NFLX, $OHI, $SPY, $QQQ

이유: 이들은 매일
- (a) Step 2의 '관심 종목 현황' 표에서 가격/변동/목표가/한줄로 모니터링되고
- (b) Step 4의 '기업 뉴스' 섹션에서 3섹션 깊이(이야기→배경→전망)로 분석됩니다.

오늘의 픽까지 차지하면 정보 중복이며 발굴 슬롯을 낭비합니다. 픽은 **새 종목 발견(discovery)** 전용입니다.

### 카탈리스트 필수
각 픽은 **14일 이내 dated 카탈리스트** 1개 이상을 보유해야 합니다. 카탈리스트 예:
- 실적 발표 (오늘~D+14)
- FDA PDUFA / 임상 결과 발표
- 컨퍼런스/제품 출시 (CES, GTC, WWDC, GPU 콘퍼런스 등)
- 가이던스 업데이트 / 자사주매입 / 배당 인상 발표
- M&A 클로징 / 분사 / IPO
- 입법/규제 결정 / 대형 정부 계약
- 임원 변동 / 행동주의 투자자 진입
- 신제품/신서비스 런칭 일정 확정

카탈리스트 없는 종목은 점수와 무관하게 **후보 탈락**. "왠지 좋아 보임"으로 픽하지 않습니다.

### 신선도 가산
`_workspace/_recent.md`의 지난 14일 [AM]/[PM] 항목에 등장하지 않은 종목 = **종합 점수에 +1 가산**.

---

## 2. 요일별 테마 클러스터

오늘 무슨 요일인지 확인하세요(`date +%u`: 1=월, 2=화, 3=수, 4=목, 5=금, 6=토, 7=일).

| 요일 | 테마 클러스터 | 발굴 풀 예시 (와치리스트 외, 가이드용) |
|------|--------------|----------------------------------------|
| 월 | AI 인프라/반도체 | AVGO, AMD, ASML, TSM, MU, ARM, MRVL, AMAT, LRCX, KLAC, SMCI, ANET |
| 화 | EV/자율주행/모빌리티 | RIVN, LCID, CHPT, JOBY, LIDR, INVZ, AUR, MBLY, UBER, HTZ, NIO |
| 수 | 에너지/원자력/친환경 | CCJ, NRG, FSLR, ENPH, NEE, BWXT, VST, CEG, LEU, BE, RUN, SEDG |
| 목 | 핀테크/결제/크립토 | SQ, PYPL, AFRM, MARA, RIOT, HOOD, SOFI, NU, MSTR, COIN_제외 |
| 금 | 헬스케어/바이오/의료기기 | LLY, MRNA, BMRN, INSP, ISRG, VRTX, REGN, GILD, BNTX, AMGN |
| 토 | 소비재/미디어/엔터 | DIS, RBLX, EA, SBUX, NKE, LULU, CMG, MELI, SPOT, ABNB |
| 일 | 산업재/인프라/방산 | LMT, RTX, GE, CAT, VMC, URI, ETN, PWR, MLM, BA |

위 풀은 **가이드용 예시**입니다. 실제 픽은 그날 스크리너 통과 + 카탈리스트 보유 종목으로 결정합니다.

오늘의 테마는 **픽 + 뉴스 + (가능하면) 딥다이브의 주축**이 됩니다. 시장 분위기가 그날 테마와 어긋날 때(예: 수요일인데 매크로 충격이 시장 지배)는 본문에서 짧게 "왜 어긋나는가"를 1~2문장 언급하고 방향을 조정합니다.

---

## 3. 7종 스크리너 풀 + 요일별 3개 회전

### 스크리너 풀
| # | 이름 | 설정 / 데이터 소스 |
|---|------|---------------------|
| 1 | 과매도(역추세) | finviz `f=ta_rsi_os30,ta_sma200_pa,sh_avgvol_o300` |
| 2 | 신고가돌파(모멘텀) | finviz `f=sh_relvol_o2,ta_highlow52w_b0to10h,sh_avgvol_o300` |
| 3 | 내부자매수 클러스터 | openinsider.com/latest-insider-trading |
| 4 | 어닝서프라이즈 위너 | WebSearch "earnings surprise today" + finviz earnings calendar |
| 5 | 공매도+거래량 (스퀴즈) | finviz `f=sh_short_o20,sh_relvol_o2,sh_avgvol_o300` |
| 6 | 배당인상+자사주 (가치) | WebSearch "dividend hike buyback announcement today" |
| 7 | 신저가+내부자(딥밸류) | finviz `f=ta_highlow52w_a0to10l,sh_avgvol_o300` × openinsider 교차 |

### 요일별 3개 선택
| 요일 | 스크리너 조합 | 컨셉 |
|------|---------------|------|
| 월 | #1 + #5 + #6 | 역추세 + 스퀴즈 + 가치 (주초 안전 + 기회) |
| 화 | #2 + #3 + #4 | 모멘텀 + 내부자 + 어닝 (성장 추세) |
| 수 | #1 + #6 + #7 | 역추세 + 가치 + 딥밸류 (거꾸로 보기) |
| 목 | #2 + #3 + #4 | 모멘텀 + 내부자 + 어닝 (실적 시즌 활용) |
| 금 | #1 + #5 + #6 | 역추세 + 스퀴즈 + 가치 (주말 진입) |
| 토 | #2 + #3 + #7 | 모멘텀 + 내부자 + 딥밸류 (장기 시각) |
| 일 | #1 + #4 + #7 | 역추세 + 어닝 + 딥밸류 (다음 주 준비) |

같은 요일이라도 시장 상황이 극단적이면(VIX>30 등) 조합 일부를 즉흥 변경 가능. 본문에서 변경 이유 명시.

---

## 4. 점수 체계 (개편)

| 차원 | 만점 | 비고 |
|------|------|------|
| 기술적 | 3 | RSI 반등(+1), 골든크로스(+1), 거래량급증(+1) |
| 수급 | 3 | 이상옵션(+1), 내부자매수(+1.5), 기관진입(+0.5) |
| **카탈리스트** | **2** | **0점이면 자동 탈락 (필수)** |
| 펀더멘털 | 2 | ROE>15%(+1), 매출성장(+1) |
| 신선도 | +1 | `_recent.md` 지난 14일 미등장 종목에 가산 |

**최종 자격 (모두 만족 필요)**:
1. 종합 7점+ (신선도 가산 후)
2. 카탈리스트 1점+ (필수)
3. 와치리스트 9종목 외

위 자격 충족하는 종목 2~3개를 픽으로 선정합니다. 부족하면 2개로 그치고, 정 없으면 1개로 끝내고 "오늘은 발굴 후보가 부족했음"을 짧게 언급합니다. **억지로 채우지 않습니다.**

---

## 5. 뉴스 쿼리 — 요일 테마 우선 + 정적 쿼리 보조

### 메인 쿼리 (오늘 테마 클러스터 기반, 메인 뉴스 비중 50%+)

| 요일 | 핵심 쿼리 4~6개 |
|------|-----------------|
| 월 | "AI infrastructure today", "반도체 오늘", "AI chip demand", "data center capex 2026", "TSMC AVGO AMD news", "GPU shortage" |
| 화 | "EV news today", "자율주행 오늘", "robotaxi update", "EV battery supply chain", "Waymo Cruise Mobileye", "Korean EV makers" |
| 수 | "energy stocks today", "원자력 발전 오늘", "uranium price today", "renewable energy news", "natural gas LNG", "small modular reactor SMR" |
| 목 | "fintech news today", "크립토 오늘", "Bitcoin price action", "stablecoin regulation", "neobank earnings", "buy now pay later" |
| 금 | "biotech news today", "FDA decision today", "clinical trial results", "GLP-1 update", "pharma earnings", "medical device approval" |
| 토 | "consumer stocks today", "media earnings", "streaming subscriber numbers", "luxury retail trend", "gaming industry news" |
| 일 | "industrial stocks today", "defense contractor news", "infrastructure bill update", "construction equipment", "aerospace deals" |

### 보조 쿼리 (비중 50% 미만)
- "미국 증시 오늘", "한국 증시 오늘"
- "ARK Invest trades today", "hedge fund news"
- "Elon Musk", "Bill Ackman"
- "자율주행 오늘" (테마 클러스터가 EV/자율주행이 아닐 때만)

### 발행일 검증 (변경 없음)
24시간(오전) / 12시간(오후) 초과 = 무조건 제외. WebSearch의 "X hours ago" 표기 우선 활용. 모호하면 WebFetch로 publish_time 메타 확인.

---

## 6. 딥다이브 테마 — 요일 테마 정렬 + 5유형 회전

### 6-1. 요일별 테마 클러스터 정렬
오늘이 화요일이면 EV/자율주행/모빌리티 관련 딥 테마를 우선 고려합니다.
단, 그날 더 큰 빅 이슈(매크로 쇼크, 대형 M&A, 정치적 사건 등)가 있으면 그 이슈를 따르되, 본문에서 "오늘 요일 테마와의 연결고리"를 1~2문장 짧게 언급합니다.

`_workspace/_recent.md`의 지난 7일 [DEEP] 항목과 정렬되지 않게 — **연속 동일 테마 절대 금지** (5/4·5/5·5/6 로보택시 3일 연속 같은 패턴 재발 방지).

### 6-2. 5유형 요일 회전 (분석 각도 다양화)
"오늘 뉴스에 적합한 자동 선택" 폐기. 요일별 강제 매핑:

| 요일 | 분석 유형 | 컨셉 |
|------|----------|------|
| 월 | 📡 테크 트렌드 | 여러 기업 같은 방향 → 산업 흐름 조망 |
| 화 | 📊 종목 해부 | 한 종목 완전 분해 (관심종목 외 발굴) |
| 수 | 🔮 미래 전망 | 시나리오 분석 (Bull/Base/Bear) |
| 목 | 🎤 보이스 컴필 | 주요 인사 발언 3개+ 교차 분석 |
| 금 | 🔍 딥 리서치 | 특정 이슈 소스 5개+ 기획기사 |
| 토 | 📊 종목 해부 | 주말 시간 들여 한 종목 깊게 |
| 일 | 🔮 미래 전망 | 다음 주 시나리오 |

같은 테마라도 매일 다른 분석 각도 → 자연스럽게 신선도 확보.

---

## 7. 딥다이브 분량 + 5섹션 의무 구조

### 7-1. 분량
**4,000~6,000자** (기존 2,000~3,000자에서 확대). 슬랙 가독성 한계선 고려.

### 7-2. 5섹션 의무 (모두 필수, 누락 시 자동 Major)
| # | 섹션 | 분량 | 내용 |
|---|------|------|------|
| 1 | **이야기** | 600~900자 | 그날 사건 — 스토리텔링 리드 |
| 2 | **시계열** | 800~1200자 | 1년·3년·10년 데이터로 본 추세, 패턴, 변곡점 |
| 3 | **국제 비교** | 800~1200자 | 미국 ↔ 한국·중국·유럽·일본 등 동일 분야 비교 |
| 4 | **반대 시각** | 600~900자 | Bull/Bear 양면 — 이 내러티브가 틀릴 수 있는 이유, 카운터-시나리오 |
| 5 | **시사점** | 600~900자 | 투자자 관점 — 구체적 종목, 진입/이탈 신호, 리스크 |

각 섹션은 매력적인 소제목으로 시작. 단순 "시계열 분석"이 아닌 "10년 차트가 보여주는 단 하나의 진실"식.

### 7-3. 출처 섹션
글 끝에 `## 출처` 필수. 인용한 모든 1차 자료 + 보조 자료 URL 명시.

---

## 8. 1차 자료 검색 의무

리서처는 다음 1차 자료 소스 중 **반드시 3종 이상 사용**. WebSearch로 끝나면 안 됨.

### 8-1. 1차 자료 소스 풀
| 소스 | 검색법 |
|------|--------|
| **SEC EDGAR** (10-K, 10-Q, 8-K) | WebFetch `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=[ticker]&type=10-K&dateb=&owner=include&count=10` |
| **어닝콜 트랜스크립트** | WebSearch `"[ticker] earnings call transcript Q[N] 2026"` 또는 fool.com, seekingalpha.com (단 SA는 paywall) |
| **학술자료 / 논문** | WebSearch `"[topic] site:arxiv.org"`, `"[topic] research paper 2026"`, Google Scholar |
| **정부/규제 보고서** | WebSearch `"[topic] FDA"`, `"[topic] DOE"`, `"[topic] Treasury"`, `"[topic] congressional report"` |
| **IR 슬라이드** | WebFetch `investor.[company].com` 또는 `ir.[company].com`의 최신 deck PDF |
| **컨퍼런스 키노트 트랜스크립트** | WebSearch `"GTC 2026 keynote transcript"`, CES, Computex, WWDC, Davos 등 |
| **산업 협회 데이터** | SIA(반도체), AIA(자동차), IEA(에너지), AAMI(의료기기) 등 협회 자료 |

### 8-2. 검증 기준
- research.md에 **1차 자료 인용 ≥ 3건** 명시 (소스명 + URL)
- 부족하면 작가는 글을 시작하지 않음 — 추가 수집

### 8-3. 차별 포인트
일반 뉴스레터에 이미 다뤄질 수준의 정보(Bloomberg/Reuters 헤드라인 수준)는 **축소**. 딥다이브만 제공할 수 있는 깊이(테크니컬 디테일, 장기 시계열, 자료 교차 분석)에 집중.

---

## 9. 에디터 7차원 검수 + 자동 차단선

### 9-1. 7차원 스코어링 (각 1~10)
| # | 차원 | 핵심 질문 |
|---|------|----------|
| 1 | 논리 흐름 | 섹션 간 인과/논리가 자연스러운가? |
| 2 | 문체 품질 | 더밀크/머니네버슬립 수준의 가독성/매력? |
| 3 | 숫자 맥락 | 의미와 함께 제시? 단순 나열 아님? |
| 4 | 투자 시사점 | 구체적 종목·진입신호·Bull/Bear? |
| 5 | 독자 가치 | 시간 들일 가치 있는 인사이트? |
| 6 | 환각 안전 | research.md 출처에 모두 근거? |
| 7 | **신선도(NEW)** | 지난 7일 경쟁 매체(머니네버슬립·더밀크·블룸버그) 대비 차별화된 시각? |

### 9-2. 자동 Major 판정 (점수와 무관하게 즉시 Major)
다음 중 **하나라도 해당되면 자동 Major**:
- ☐ 1차 자료 인용 < 3건
- ☐ 시계열 분석 섹션 누락 또는 부실 (300자 미만)
- ☐ 국제 비교 섹션 누락 또는 부실
- ☐ 반대 시각(Bull/Bear) 양면 미존재
- ☐ 신선도 점수 < 6
- ☐ 환각 안전 점수 < 7
- ☐ 본문 분량 < 3,500자

### 9-3. 판정
- 평균 7+ AND 자동 Major 조건 0개 → **Accept** (경미한 수정만)
- 평균 7+ AND 자동 Major 조건 0개지만 개선점 3개+ → **Minor** (직접 수정)
- 자동 Major 조건 1개+ OR 평균 7- → **Major** (재작성 1회)

### 9-4. 재작성 한도
Major 판정 시 1회 재작성. 그 후에도 자동 차단선 통과 못하면 발행 보류 (final.md에 "발행 보류 — 품질 미달" 기록).

---

## 10. 트리거 분리 구조 (참고)

딥다이브는 race condition 방지 + 시간 여유 확보 위해 2개 트리거로 분리:

| 트리거 | 시간 (KST) | 역할 |
|--------|-----------|------|
| 딥 테마 선정 | 09:00 | theme.md 생성 (요일 클러스터 + 5유형 적용 + 다양성 가드). 가벼움 ~5분 |
| 딥 작성+검수+발행 | 14:00 | theme.md 읽고 → 1차 자료 리서치 → 5섹션 작성 → 7차원 검수 → 발행. 단일 트리거 = race 없음. ~50분 가능 |

기존 14:30 KST "딥다이브 B" 트리거는 비활성화 (race condition 원인이었음).

---

## 변경 이력
- **2026-05-08 v3**: 딥다이브 5유형 요일 회전, 4-6K자 분량, 5섹션 의무, 1차 자료 ≥3건, 7차원 검수 + 자동 차단선, 트리거 통합 구조
- **2026-05-08 v2**: 와치리스트 9종목 픽 제외, 요일별 테마 클러스터, 7종 스크리너 회전, 카탈리스트 필수화, 14일 신선도 가산, 뉴스 쿼리 요일 테마화
- **2026-05-07 v1**: dedup 메커니즘 도입 (`_published/topics_log.md` 기반)
