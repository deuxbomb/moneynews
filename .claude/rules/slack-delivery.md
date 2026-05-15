# Slack 자동 발송 규칙 (필수)

## 배경
Claude Code 원격 실행 환경의 git push (`noreply@anthropic.com`)는 GitHub Actions `push` 이벤트를 트리거하지 않는다.
따라서 git push만으로는 `send-to-slack.yml` 워크플로가 실행되지 않아 Slack 발송이 누락된다.

## Step 9 필수 절차 (딥다이브 · 뉴스레터 모든 파이프라인)

`_workspace/02_newsletter_draft.md`를 업데이트한 후 **반드시 두 단계를 모두 수행**한다:

### 1단계: git commit + push (로컬→원격 동기화)
```bash
git add -f _workspace/02_newsletter_draft.md [기타 파일들]
git commit -m "..."
git push -u origin main
```

### 2단계: mcp__github__push_files (GitHub Actions 트리거) — 필수!
git push 직후, `mcp__github__push_files` 도구로 `_workspace/02_newsletter_draft.md`를 다시 한번 API로 푸시한다.
이 API 커밋은 사용자 OAuth 토큰으로 귀속되어 GitHub Actions를 정상 트리거한다.

```
mcp__github__push_files(
  owner="deuxbomb",
  repo="moneynews",
  branch="main",
  message="trigger: Slack 발송 — {날짜} {제목}",
  files=[{"path": "_workspace/02_newsletter_draft.md", "content": <파일 전체 내용>}]
)
```

**주의**: `content`에는 파일 전체 내용을 그대로 넣는다. 변경이 없으면 GitHub API가 커밋을 생성하지 않을 수 있으므로, 파일 끝에 `<!-- slack_trigger: {날짜} -->` 한 줄을 추가한다.
`send_to_slack.py`는 `<!-- ... -->` 형태의 HTML 주석을 자동으로 제거하므로 Slack 메시지에는 나타나지 않는다.

### 2단계 수행 후 git pull (로컬 동기화)
```bash
git pull origin main
```
API 커밋이 원격에 생성되므로, 로컬과 동기화가 필요하다.

## 검증
2단계 수행 후 GitHub Actions 탭에서 `Send MoneyNews to Slack` 워크플로가 실행됨을 확인.
