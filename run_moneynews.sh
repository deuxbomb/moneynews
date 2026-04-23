#!/bin/bash
# 머뉴(MoneyNews) 일간 뉴스레터 자동 실행 스크립트

export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/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"

cd /Users/jongcheollim/moneynews

LOG_FILE="/Users/jongcheollim/moneynews/_workspace/run_$(date +%Y%m%d_%H%M%S).log"
mkdir -p _workspace

echo "$(date): 머뉴 뉴스레터 생성 시작" | tee "$LOG_FILE"

# Step 1: Claude가 뉴스레터만 생성 (슬랙 전송은 하지 않음)
claude --print --dangerously-skip-permissions -p "당신은 머뉴(MoneyNews) 뉴스레터 생성 에이전트입니다. .claude/CLAUDE.md를 먼저 읽고 규칙을 숙지하세요. 오늘 날짜 기준으로 다음을 수행하세요:

1. 자율주행 뉴스: 오늘 날짜 포함 한국어/영어 검색. 24시간 이내 기사만.
2. 미국 증시 뉴스: 오늘+전일 검색. 3대 지수, 핵심 이슈, 관심종목(\$TSLA,\$GOOGL,\$OKLO,\$NVDA,\$COIN,\$NFLX,\$OHI,\$SPY,\$QQQ) 뉴스, 가십.
3. 관심 종목 분석: 실적, 컨센서스, 목표가, 옵션/수급.
4. 테크 팟캐스트 요약(최근 1주일): TBPN, Lenny's, 20VC, No Priors, All-In, Acquired, Lex Fridman.
5. _workspace/02_newsletter_draft.md 파일로 뉴스레터 생성. 머니네버슬립 스타일, 한글, 이모지, 티커심볼.

⚠️ 중요: send_to_slack.py를 실행하지 마세요. 슬랙 전송은 이 스크립트가 직접 합니다.
⚠️ 중요: python이나 send_to_slack 관련 명령을 절대 실행하지 마세요.

모든 내용 한글. 영어 기사는 원문 제목+URL 병기. 블로그가 아닌 뉴스 기사 우선." >> "$LOG_FILE" 2>&1

# Step 2: 뉴스레터 파일이 생성되었으면 슬랙으로 1회만 전송
if [ -f "_workspace/02_newsletter_draft.md" ]; then
    echo "$(date): 뉴스레터 생성 완료. 슬랙 전송 중..." | tee -a "$LOG_FILE"
    python3 send_to_slack.py >> "$LOG_FILE" 2>&1
    echo "$(date): 슬랙 전송 완료" | tee -a "$LOG_FILE"
else
    echo "$(date): ❌ 뉴스레터 파일이 생성되지 않았습니다" | tee -a "$LOG_FILE"
fi

echo "$(date): 전체 완료" | tee -a "$LOG_FILE"
