#!/usr/bin/env python3
"""머뉴(MoneyNews) 뉴스레터를 슬랙으로 전송하는 스크립트

슬랙 웹훅은 약 4,000자 이상이면 메시지를 자동 분할함.
따라서 PART 1(3분 캐치업)만 슬랙으로 보내고,
전체 뉴스레터는 HTML 파일 참고 안내.
"""

import json
import urllib.request
import sys
import os
import re

WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")
if not WEBHOOK_URL:
    print("❌ SLACK_WEBHOOK_URL 환경변수가 설정되어 있지 않습니다.")
    sys.exit(1)

SLACK_CHAR_LIMIT = 3800  # 슬랙 분할 방지 (4000자 미만)


def extract_slack_summary(md_path):
    """마크다운에서 PART 1(3분 캐치업) + 주요 헤드라인만 추출"""

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # A/B 테스트, 변형 섹션 제거
    content = re.sub(r'(?:#{1,4}\s*)?(?:A/B|a/b).*?(?=\n#{1,3}\s|\Z)', '', content, flags=re.DOTALL)

    lines = content.split('\n')
    result = []
    in_table = False
    table_rows = []
    current_part = 0

    for line in lines:
        stripped = line.strip()

        # PART 감지
        if re.search(r'PART\s*[23456789]|딥다이브|팟캐스트|상세\s*기사', stripped, re.IGNORECASE):
            current_part = 2  # PART 2 이상이면 중단

        # PART 1만 포함 (3분 캐치업 + 관심 종목까지)
        if current_part >= 2:
            break

        # 테이블 처리 → 리스트로 변환
        if stripped.startswith('|') and '|' in stripped[1:]:
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            if all(set(c) <= set('-: ') for c in cells):
                continue
            if not in_table:
                in_table = True
                table_rows = []
            else:
                table_rows.append(cells)
        else:
            if in_table and table_rows:
                result.append("")
                for row in table_rows:
                    if len(row) >= 2:
                        result.append("  ".join(c for c in row if c and c != '—' and c != '-'))
                result.append("")
                in_table = False
                table_rows = []

            # 마크다운 → 슬랙 mrkdwn
            converted = re.sub(r'\*\*(.+?)\*\*', r'*\1*', stripped)
            converted = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<\2|\1>', converted)
            converted = re.sub(r'^#{1,4}\s+', '', converted)
            result.append(converted)

    # 마지막 테이블
    if in_table and table_rows:
        result.append("")
        for row in table_rows:
            if len(row) >= 2:
                result.append("  ".join(c for c in row if c and c != '—'))
        result.append("")

    text = '\n'.join(result)
    text = re.sub(r'\n{4,}', '\n\n', text)

    # 길이 제한
    if len(text) > SLACK_CHAR_LIMIT:
        text = text[:SLACK_CHAR_LIMIT]
        last_newline = text.rfind('\n')
        if last_newline > SLACK_CHAR_LIMIT - 500:
            text = text[:last_newline]
        text += "\n\n📖 _전체 뉴스레터(상세 기사 · 딥다이브 · 팟캐스트)는 HTML 버전을 확인하세요._"

    return text


def send_message(text):
    """슬랙 웹훅으로 메시지 1건 전송"""
    payload = {
        "text": text,
        "unfurl_links": False,
        "unfurl_media": False
    }

    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=data,
        headers={'Content-Type': 'application/json'}
    )

    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                print("✅ 슬랙 메시지 전송 성공 (1건)")
                return True
            else:
                print(f"❌ 전송 실패: {response.status}")
                return False
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP 에러: {e.code} - {e.read().decode()}")
        return False
    except Exception as e:
        print(f"❌ 에러: {e}")
        return False


if __name__ == "__main__":
    workspace = os.path.join(os.path.dirname(__file__), "_workspace")
    md_path = os.path.join(workspace, "02_newsletter_draft.md")

    if not os.path.exists(md_path):
        print(f"❌ 뉴스레터 파일 없음: {md_path}")
        sys.exit(1)

    print("📨 머뉴(MoneyNews) 뉴스레터를 슬랙으로 전송합니다...")

    summary = extract_slack_summary(md_path)
    print(f"📏 메시지 크기: {len(summary)}자 (한도: {SLACK_CHAR_LIMIT}자)")

    if send_message(summary):
        print("🎉 완료!")
    else:
        sys.exit(1)
