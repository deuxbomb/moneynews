#!/usr/bin/env python3
"""머뉴(MoneyNews) 뉴스레터를 슬랙으로 전송하는 스크립트

전송 방식:
1. 슬랙 메시지: 3분 캐치업 요약 (표 없이 텍스트, 가독성 우선)
2. HTML 파일 업로드: 풀 뉴스레터 (표, 딥다이브, 팟캐스트 포함)
"""

import json
import urllib.request
import sys
import os
import re
from datetime import datetime

WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")
if not WEBHOOK_URL:
    print("❌ SLACK_WEBHOOK_URL 환경변수가 설정되어 있지 않습니다.")
    sys.exit(1)


def extract_slack_summary(md_path):
    """마크다운에서 슬랙용 요약을 생성 (표를 리스트 형태로 변환)"""

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 마크다운 테이블을 슬랙 친화적 리스트로 변환
    lines = content.split('\n')
    result = []
    in_table = False
    table_rows = []
    headers = []

    for line in lines:
        stripped = line.strip()

        # 테이블 감지
        if stripped.startswith('|') and '|' in stripped[1:]:
            cells = [c.strip() for c in stripped.split('|')[1:-1]]

            # 구분선(---|---) 스킵
            if all(set(c) <= set('-: ') for c in cells):
                continue

            if not in_table:
                # 첫 번째 행 = 헤더
                in_table = True
                headers = cells
                table_rows = []
            else:
                table_rows.append(cells)
        else:
            # 테이블 끝 → 리스트로 변환
            if in_table and table_rows:
                result.append("")
                for row in table_rows:
                    if len(row) >= 2:
                        # 종목 테이블인 경우 (첫 열이 $로 시작)
                        if row[0].startswith('$') or row[0].startswith('*$'):
                            ticker = row[0].replace('*', '')
                            parts = [ticker]
                            for i, cell in enumerate(row[1:], 1):
                                if cell and cell != '—' and cell != '-':
                                    parts.append(cell)
                            result.append("  ".join(parts))
                        else:
                            result.append(" · ".join(c for c in row if c and c != '—'))
                result.append("")
                in_table = False
                table_rows = []
                headers = []

            # 마크다운 → 슬랙 mrkdwn 변환
            # **bold** → *bold*
            converted = re.sub(r'\*\*(.+?)\*\*', r'*\1*', stripped)
            # [text](url) → <url|text>
            converted = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<\2|\1>', converted)
            # ### → 볼드
            converted = re.sub(r'^#{1,4}\s+', '', converted)

            result.append(converted)

    # 마지막 테이블 처리
    if in_table and table_rows:
        result.append("")
        for row in table_rows:
            if len(row) >= 2:
                if row[0].startswith('$'):
                    result.append("  ".join(c for c in row if c))
                else:
                    result.append(" · ".join(c for c in row if c and c != '—'))
        result.append("")

    text = '\n'.join(result)

    # 연속 빈 줄 정리
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    return text


def send_message(text):
    """슬랙 웹훅으로 메시지 전송"""
    MAX_LEN = 39000
    chunks = []

    if len(text) <= MAX_LEN:
        chunks = [text]
    else:
        # PART 단위로 분할
        parts = re.split(r'\n(={3,})\n', text)
        if len(parts) <= 1:
            # ---로 분할
            parts = text.split('\n---\n')

        current = ""
        for part in parts:
            if len(current) + len(part) > MAX_LEN:
                if current:
                    chunks.append(current)
                current = part
            else:
                current += ('\n\n' if current else '') + part
        if current:
            chunks.append(current)

    for i, chunk in enumerate(chunks):
        payload = {
            "text": chunk,
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
                    part_info = f" (파트 {i+1}/{len(chunks)})" if len(chunks) > 1 else ""
                    print(f"✅ 슬랙 메시지 전송 성공{part_info}")
                else:
                    print(f"❌ 전송 실패: {response.status}")
                    return False
        except urllib.error.HTTPError as e:
            print(f"❌ HTTP 에러: {e.code} - {e.read().decode()}")
            return False
        except Exception as e:
            print(f"❌ 에러: {e}")
            return False

    return True


if __name__ == "__main__":
    workspace = os.path.join(os.path.dirname(__file__), "_workspace")
    md_path = os.path.join(workspace, "02_newsletter_draft.md")
    html_path = os.path.join(workspace, "02_newsletter_draft.html")

    if not os.path.exists(md_path):
        print(f"❌ 뉴스레터 파일 없음: {md_path}")
        sys.exit(1)

    print("📨 머뉴(MoneyNews) 뉴스레터를 슬랙으로 전송합니다...")
    print()

    # 마크다운을 슬랙 친화적 포맷으로 변환
    summary = extract_slack_summary(md_path)

    # 슬랙 전송
    if send_message(summary):
        print()
        if os.path.exists(html_path):
            print(f"💡 상세 뉴스레터 HTML: {html_path}")
            print("   브라우저에서 열면 표와 레이아웃이 완벽하게 보입니다.")
        print("🎉 완료!")
    else:
        sys.exit(1)
