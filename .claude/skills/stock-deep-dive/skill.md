---
name: stock-deep-dive
description: "관심 종목 딥다이브 분석. 옵션 플로우, 기관 수급, 실적 분석, 셀사이드 리포트, 밸류에이션을 에이전트 팀이 협업하여 종합 투자 판단 자료를 생성한다. '종목 분석해줘', '투자 타이밍', '옵션 분석', '기관 수급', '실적 분석', '목표가', '밸류에이션' 등 종목 딥다이브 요청에 이 스킬을 사용한다."
---

# Stock Deep Dive — 종목 딥다이브 분석 파이프라인

관심 종목의 옵션 플로우, 기관 수급, 실적, 셀사이드 리포트, 밸류에이션을 에이전트 팀이 협업하여 종합 분석한다.

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

## 에이전트 구성

| 에이전트 | 파일 | 역할 |
|---------|------|------|
| options-analyst | `.claude/agents/options-analyst.md` | 옵션 플로우, P/C Ratio, IV, 맥스 페인 |
| flow-tracker | `.claude/agents/flow-tracker.md` | 13F, 다크풀, 내부자 거래, 공매도 |
| earnings-analyst | `.claude/agents/earnings-analyst.md` | 실적 서프라이즈, 가이던스, 컨센서스 |
| report-aggregator | `.claude/agents/report-aggregator.md` | 셀사이드 리포트, 목표가, 투자의견 |
| valuation-expert | `.claude/agents/valuation-expert.md` | DCF, 멀티플, 비교기업 밸류에이션 |
| scenario-planner | `.claude/agents/scenario-planner.md` | Bull/Base/Bear 시나리오 |
| quality-reviewer | `.claude/agents/quality-reviewer.md` | 교차 검증, 정합성 확인 |

## 워크플로우

### Phase 1: 준비
1. 사용자 입력에서 분석 대상 종목을 확인한다 (기본: 전체 관심 종목)
2. `_workspace/analysis/` 디렉토리를 생성한다
3. 분석 범위를 결정한다 (전체 딥다이브 vs 특정 영역)

### Phase 2: 데이터 수집 (병렬 실행)

| 순서 | 작업 | 담당 | 산출물 |
|------|------|------|--------|
| 1a | 옵션 플로우 분석 | options-analyst | `_workspace/analysis/options_flow_report.md` |
| 1b | 기관 수급 추적 | flow-tracker | `_workspace/analysis/flow_tracking_report.md` |
| 1c | 실적 분석 | earnings-analyst | `_workspace/analysis/earnings_report.md` |
| 1d | 셀사이드 리포트 | report-aggregator | `_workspace/analysis/sellside_report.md` |

**1a~1d는 병렬 실행** 가능하다.

### Phase 3: 종합 분석 (순차 실행)

| 순서 | 작업 | 담당 | 의존 | 산출물 |
|------|------|------|------|--------|
| 2 | 밸류에이션 | valuation-expert | 1c, 1d | `_workspace/analysis/valuation_report.md` |
| 3 | 시나리오 분석 | scenario-planner | 1a~1d, 2 | `_workspace/analysis/scenario_report.md` |
| 4 | 품질 검증 | quality-reviewer | 전체 | `_workspace/analysis/review_report.md` |

### Phase 4: 통합 리포트

모든 분석을 종합하여 **종목별 투자 판단 요약**을 생성한다:

`_workspace/analysis/stock_deep_dive_final.md`:

    # 종목 딥다이브 종합 리포트

    ## 종목별 투자 스코어카드
    | 종목 | 현재가 | 목표가 범위 | 옵션 시그널 | 수급 시그널 | 실적 트렌드 | 종합 판단 |
    |------|--------|-----------|-----------|-----------|-----------|---------|

    ## 종목별 상세 (각 종목)
    ### 1. 투자 판단 요약 (1문단)
    ### 2. Bull Case vs Bear Case
    ### 3. 핵심 카탈리스트 & 리스크
    ### 4. 추천 액션 (매수/보유/관망/매도)

## 작업 규모별 모드

| 요청 패턴 | 모드 | 투입 에이전트 |
|----------|------|-------------|
| "전체 종목 분석해줘" | **풀 딥다이브** | 7명 전원 |
| "테슬라 옵션만 봐줘" | **옵션 포커스** | options-analyst 단독 |
| "$NVDA 실적 분석해줘" | **실적 포커스** | earnings-analyst + report-aggregator |
| "수급 어떤지 봐줘" | **수급 포커스** | flow-tracker + options-analyst |
| "밸류에이션 점검해줘" | **밸류 포커스** | valuation-expert + scenario-planner |

## 에러 핸들링

| 에러 | 전략 |
|------|------|
| 웹 검색 실패 | 가용 데이터 범위를 명시하고 진행 |
| 소형주 데이터 부족 ($OKLO) | 유사 기업 벤치마크 활용, "제한적 데이터" 태그 |
| ETF 분석 ($SPY, $QQQ) | 구성 종목 기반 분석 + 펀드 플로우 중심 |
| 리포트 접근 제한 | 공개 요약 기반 작성, 원문 미확인 태그 |
