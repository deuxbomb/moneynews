# 머뉴 (MoneyNews) — 돈이 되는 모든 것에 대한 소식

자율주행 뉴스 + 미국 증시 동향 + 관심 종목 딥다이브 + 테크 팟캐스트 요약을 에이전트 팀이 협업하여 HTML 뉴스레터로 생성하는 하네스.

## 브랜딩
- **이름**: 머뉴 (MoneyNews)
- **태그라인**: "돈이 되는 모든 것에 대한 소식"
- **구독 해지 링크**: 포함하지 않음

## ⚠️ 링크 표기 규칙 (모든 에이전트 필수 준수)
- 링크 텍스트는 **해당 뉴스 매체명**으로 짧게 표기한다
- ❌ `https://techcrunch.com/2026/04/14/waymo-london...`
- ❌ `[Waymo opens robotaxi service in Nashville, partners with Lyft](https://techcrunch.com/...)`
- ✅ `[TechCrunch](https://techcrunch.com/2026/04/14/waymo-london...)`
- ✅ `[Bloomberg](https://bloomberg.com/news/...)`
- ✅ `[매경](https://mk.co.kr/news/...)`
- 복수 출처: `[TechCrunch](URL) · [Reuters](URL)`
- 이 규칙은 뉴스레터, 딥다이브, 팟캐스트 등 모든 산출물에 동일 적용

## ⚠️ 최신성 규칙 (모든 에이전트 필수 준수)
- **24시간 이내 뉴스만 포함**한다. 2일 이상 지난 기사는 절대 포함하지 않는다.
- 검색 시 반드시 **오늘 날짜**를 키워드에 포함한다 (예: "April 15 2026", "2026년 4월 15일", "today")
- 미국 증시 뉴스는 **오늘 날짜 + 전일 날짜 둘 다** 검색한다 (예: 한국 4/15이면 → "April 15 2026"과 "April 14 2026" 모두). 오늘자 프리마켓, 선물, 분석 기사를 우선하고, 전일 장 마감 뉴스를 보충한다.
- 블로그, 리스티클, 오래된 분석글이 아닌 **당일 뉴스 기사**를 우선한다
- 기사의 발행일을 반드시 확인하고, 발행일이 불명확한 글은 제외한다
- 실적 데이터, 주가, 옵션 데이터는 **가장 최근 거래일 기준**으로 수집한다

## 주제 및 언어 규칙
- **주제 1**: 자율주행 (자율주행차, ADAS, 라이다, 웨이모, 테슬라 FSD, 로보택시 등)
- **주제 2**: 미국 증시 (S&P 500, 나스닥, 다우, 거시경제, 섹터 동향)
- **주제 3**: 관심 종목 딥다이브 분석
- **주제 4**: 테크 팟캐스트 최신 에피소드 요약
- **검색 언어**: 한국어 + 영어 모두 검색
- **출력 언어**: 모든 산출물은 **한글**로 작성. 영문 뉴스는 한글로 번역·요약하되 원문 제목과 URL을 병기.
- **톤**: 머니네버슬립 스타일 — 전문적이면서 친근하고 위트 있는 한국어. 이모지 활용. 티커 심볼($TSLA 등) 사용.

## 관심 종목
| 티커 | 기업명 | 섹터 |
|------|--------|------|
| $TSLA | Tesla | EV/자율주행/AI |
| $GOOGL | Alphabet | 빅테크/AI/클라우드 |
| $OKLO | Oklo | 원자력/클린에너지 |
| $NVDA | NVIDIA | AI 반도체 |
| $COIN | Coinbase | 크립토/핀테크 |
| $NFLX | Netflix | 스트리밍/엔터 |
| $OHI | Omega Healthcare | 헬스케어 리츠 |
| $SPY | SPDR S&P 500 ETF | 시장 전체 |
| $QQQ | Invesco QQQ | 나스닥 100 |

## 구조

```
.claude/
├── agents/
│   ├── curator.md             — 뉴스 큐레이터 (한/영 뉴스 수집)
│   ├── copywriter.md          — 카피라이터 (머니네버슬립 스타일)
│   ├── analyst.md             — 뉴스레터 분석가 (A/B테스트, 발송 최적화)
│   ├── editor-in-chief.md     — 편집장 (톤 일관성, 최종 편집)
│   ├── quality-reviewer.md    — 품질 검증자 (교차 검증)
│   ├── options-analyst.md     — 옵션 플로우 분석가 (P/C, IV, 맥스페인)
│   ├── flow-tracker.md        — 기관 수급 추적 (13F, 다크풀, 내부자)
│   ├── earnings-analyst.md    — 실적 분석가 (서프라이즈, 가이던스)
│   ├── report-aggregator.md   — 셀사이드 리포트 수집가 (목표가, 투자의견)
│   ├── valuation-expert.md    — 밸류에이션 전문가 (DCF, 멀티플)
│   ├── scenario-planner.md    — 시나리오 분석가 (Bull/Base/Bear)
│   ├── financial-analyst.md   — 재무 분석 전문가 (P&L, 현금흐름)
│   └── market-analyst.md      — 시장 동향 분석 전문가
├── skills/
│   ├── newsletter-engine/     — 뉴스레터 풀 파이프라인
│   ├── stock-deep-dive/       — 종목 딥다이브 분석 파이프라인
│   ├── email-copywriting/     — 이메일 카피라이팅 전문 스킬
│   ├── audience-segmentation/ — 독자 세그멘테이션
│   └── deliverability-optimization/ — 도달률 최적화
└── CLAUDE.md                  — 이 파일
```

## 스킬

### `/newsletter-engine` — 뉴스레터 생성
자율주행 뉴스 + 미국 증시 동향을 수집하여 HTML 뉴스레터를 생성한다.

### `/stock-deep-dive` — 종목 딥다이브 분석
관심 종목의 옵션 플로우, 기관 수급, 실적, 셀사이드 리포트, 밸류에이션을 종합 분석한다.

## 통합 워크플로우 (일간 뉴스레터)

```
Phase 1: 뉴스 수집 (병렬)
  ├── curator → 자율주행 뉴스 (한/영)
  ├── curator → 미국 증시 뉴스 (한/영)
  └── 종목 딥다이브 (병렬):
      ├── options-analyst → 옵션 플로우
      ├── flow-tracker → 기관 수급
      ├── earnings-analyst → 실적 분석
      └── report-aggregator → 셀사이드 리포트

Phase 2: 종합 분석
  ├── valuation-expert → 밸류에이션
  └── scenario-planner → Bull/Base/Bear

Phase 3: 뉴스레터 작성
  ├── copywriter → HTML 뉴스레터 초안
  ├── editor-in-chief → 최종 편집
  └── quality-reviewer → 품질 검증

Phase 4: 전송
  └── 카카오톡 나에게 보내기 API
```

## 산출물

모든 산출물은 `_workspace/` 디렉토리에 저장:
- `00_input.md` — 사용자 입력 정리
- `01_curation_brief.md` — 자율주행 뉴스 큐레이션
- `01_us_market_brief.md` — 미국 증시 큐레이션
- `analysis/` — 종목 딥다이브 분석 리포트들
- `02_newsletter_draft.html` — HTML 뉴스레터
- `02_newsletter_draft.md` — 플레인텍스트 버전
