# 리서치 노트 — 2026-06-18 딥다이브

## 1차 자료 인용 건수: 6건 (기준 3건 충족 ✅)
1. Google Cloud 공식 블로그 — AP2 발표 (WebFetch로 직접 확인)
2. Mastercard 공식 보도자료 — Agent Pay for Machines (mastercard.com / investor.mastercard.com)
3. Visa 공식 뉴스룸 — Intelligent Commerce / Payments Forum 2026 (usa.visa.com)
4. 카카오페이 공식 보도자료 — x402 재단 창립멤버 합류 (플래텀/뉴스1 relay)
5. McKinsey QuantumBlack 공식 리포트 — 에이전틱 커머스 시장 전망
6. Morgan Stanley Research 공식 insights / Juniper Research 공식 보도 — 시장 규모

## 테마
AI 에이전트가 사람 대신 결제하는 시대 — "에이전트 경제(Agentic Economy)"의 결제 레일 전쟁

## 유형
🎤 보이스 컴필 (5인 발언 교차 분석)

## 선정 이유
6월 둘째 주, 카드 네트워크·빅테크·크립토가 거의 동시에 "AI 에이전트 결제" 인프라를 발표했다(6/2 x402 재단, 6/10 Mastercard, 6/11 Visa). 한국에선 카카오페이가 국내 유일 x402 재단 창립멤버로 참여했지만 규제로 출발이 늦다. 결제 산업의 수십 년 질서(카드 중심)가 흔들리는 구조적 변곡점을 5인의 발언으로 해부.

---

## 팩트 (출처 필수)

### 타임라인 (시계열용)
1. x402는 HTTP의 오래 잠들어 있던 "402 Payment Required" 에러 코드에서 이름을 따왔다. Coinbase가 머신-투-머신 결제 프로토콜로 부활시킴 — 출처: https://crypto.news/brian-armstrong-hands-ai-agents-the-keys-to-coinbase/
2. 2025-09-16: Google이 Agent Payments Protocol(AP2)을 60개+ 파트너와 함께 발표. 파트너: Mastercard, PayPal, Coinbase, American Express, Salesforce, Adyen, JCB, Revolut, Worldpay 등 — 출처: https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol (직접 확인)
3. AP2는 A2A(Agent2Agent) 및 MCP(Model Context Protocol)의 확장으로 작동. 3대 질문(Authorization 권한·Authenticity 진정성·Accountability 책임)을 해결하는 결제수단 중립 프레임워크 — 출처: 위 Google Cloud 블로그 (직접 확인, 원문 인용)
4. Google은 Coinbase·Ethereum Foundation·MetaMask와 협력해 "A2A x402 extension"(크립토 결제용 프로덕션 솔루션) 출시 — 출처: 위 Google Cloud 블로그 (직접 확인)
5. 2026-02-11: Coinbase가 x402 프로토콜 위에 Agentic Wallets 출시 — 출처: https://cryptobriefing.com/coinbase-ai-agent-accounts-trading/
6. 2026-03(말, ~3/24): OpenAI가 ChatGPT의 Instant Checkout을 5~6개월 만에 사실상 접고 상품 '발견(discovery)' 중심으로 개편. Shopify 수백만 가맹점 중 약 12곳만 라이브였음 — 출처: https://www.cnbc.com/2026/03/24/openai-revamps-shopping-experience-in-chatgpt-after-instant-checkout.html
7. 2026-04: Coinbase Agentic.Market 출시; AP2 v0.2.0 배포 — 출처: https://www.coindesk.com/markets/2026/03/11/coinbase-backed-ai-payments-protocol-wants-to-fix-micropayment-but-demand-is-just-not-there-yet
8. 2026-06-02(미 동부시간): Linux Foundation이 'x402 재단' 출범. 카카오페이가 국내 결제사 중 처음·한국 기업 중 유일하게 창립멤버 합류(6/6 발표). 재단 참여: Coinbase, Circle, Solana, Google, AWS, Microsoft, Visa, Mastercard, Stripe, Shopify 등 — 출처: https://platum.kr/archives/284819 , https://www.news1.kr/it-science/general-it/6126308 , https://www.sedaily.com/article/20028862
9. 2026-06-10: Mastercard가 "Agent Pay for Machines" 출시. AI 에이전트·머신이 머신 속도로 1센트 미만(a fraction of a cent) 마이크로트랜잭션까지 결제 가능한 멀티레일 서비스. 30개+ 파트너 — 출처: https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html , https://genfinity.io/2026/06/10/mastercard-agent-pay-for-machines-launch/
10. Mastercard Agent Pay는 카드부터 6종 규제 달러 스테이블코인(Circle USDC, Paxos PYUSD, USDG, USDP, Ripple RLUSD, SoFiUSD)까지 settlement 지원 — 출처: https://finance.yahoo.com/markets/crypto/articles/mastercard-taps-coinbase-ripple-crypto-222300868.html
11. Mastercard Agent Pay 초기 파트너: Aave Labs, Adyen, Ant International, BVNK, Checkout.com, Cloudflare, Coinbase, Crossmint, Global Payments, MoonPay, OKX, Polygon, Rain, Ripple, Skyfire, Solana Foundation, Stripe, Turnkey 등 — 출처: 위 Mastercard 보도 / Genfinity
12. 2026-06-11: Visa가 "Intelligent Commerce Connect"(에이전틱 커머스 단일 통합) 출시. 4대 에이전트 프로토콜 지원: Trusted Agent Protocol, Machine Payments Protocol, Agentic Commerce Protocol, Universal Commerce Protocol. 파일럿 파트너: Aldar, AWS, Diddo, Highnote, Mesh, Payabli, Sumvin — 출처: https://thepaypers.com/payments/news/visa-launches-intelligent-commerce-connect-for-agentic-payments
13. 2026-06-11: Visa-OpenAI 협력으로 ChatGPT 안에 Visa 결제 임베드 — 에이전트가 추천을 넘어 직접 구매 완료 가능 — 출처: https://fortune.com/2026/06/11/visa-chatgpt-ai-agent-payments-shopping/ , https://www.pymnts.com/news/artificial-intelligence/2026/visa-openai-unlock-agentic-commerce/
14. Visa는 2026 홀리데이 시즌까지 수백만 소비자가 AI 에이전트로 구매를 완료할 것으로 전망. 이미 수백 건의 통제된 실거래 에이전트 결제 실행 — 출처: 위 thepaypers / Visa 뉴스룸
15. 2026-06-17: PayPal이 기업 벤처 부문(PayPal Ventures)을 정리. 2월 CEO가 Alex Chriss → Enrique Lores로 교체된 구조조정의 일환 — 출처: https://techcrunch.com/2026/06/17/paypal-ventures-shutters-as-company-restructuring-continues/
16. 2026-06-11: OCC가 Bulletin 2026-24로 결제 스테이블코인 발행사 주간·분기 보고 양식 제안 — 출처: https://www.lowenstein.com/news-insights/newsletters/fintech-five-june-16-2026
17. 2026-06-18: 한국 정부, 금융 AI '7대 원칙' 6/22 시행 — 망분리 완화·AX 규율체계 구축 — 출처: https://www.etnews.com/20260618000036

### 시장 규모 (숫자 데이터)
18. Juniper Research: 에이전틱 커머스 거래액 2026년 80억 달러 → 2030년 1.5조 달러 전망 — 출처: https://www.juniperresearch.com/press/agentic-commerce-set-to-generate-15-trillion-globally-by-2030-as-payments-infrastructure-leaders-revealed/
19. McKinsey: 2030년까지 최대 5조 달러 에이전틱 커머스 매출 전망 — 출처: https://www.digitalcommerce360.com/2025/10/20/mckinsey-forecast-5-trillion-agentic-commerce-sales-2030/ , https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-agentic-commerce-opportunity-how-ai-agents-are-ushering-in-a-new-era-for-consumers-and-merchants
20. Morgan Stanley Research: 2030년 미국 이커머스에서 에이전틱 쇼핑 1,900억~3,850억 달러 — 출처: https://www.morganstanley.com/insights/articles/agentic-commerce-market-impact-outlook
21. Bain & Company: 2030년 미국 에이전틱 커머스 3,000억~5,000억 달러, 전체 이커머스의 15~25% — 출처: https://www.bain.com/insights/2030-forecast-how-agentic-ai-will-reshape-us-retail-snap-chart/
22. 에이전틱 '결제 인프라' 시장만 2032년 70억→930억 달러 전망 — 출처: https://nevermined.ai/blog/agentic-commerce-growth-statistics
23. Coinbase는 연간 약 1조 달러 스테이블코인 결제를 처리 — 출처: https://thedefiant.io/news/cefi/brian-armstrong-says-coinbase-processes-usd1t-in-stablecoin-payments-annually
24. Coinbase Agentic.Market: 2026년 4월 출시 후 1억 6,500만 건 거래·48만 에이전트가 프로토콜에서 거래(2026년 6월 기준) — 출처: https://crypto.news/ai-agents-could-outspend-humans-coinbase-ceo-says/
25. (한국) 네이버페이·카카오페이·토스 연간 순수 간편결제 거래액 첫 100조원 돌파 — 출처: https://www.fnnews.com/news/202601011803461679

---

## 직접 인용 (정확한 원문만)

1. "The agentic economy could be larger than the human economy." — Brian Armstrong (Coinbase CEO), crypto.news, 2026 — https://crypto.news/ai-agents-could-outspend-humans-coinbase-ceo-says/
   - 부연: Armstrong은 곧 인간보다 더 많은 AI 에이전트가 거래를 하게 될 것이며, AI 에이전트는 은행 계좌를 열 수 없으므로 그 거래는 크립토(스테이블코인)에서 돌 것이라고 주장 — https://www.fintechweekly.com/news/brian-armstrong-ai-agents-crypto-wallets-coinbase-agentic-wallets-march-2026

2. "AI will transform commerce more profoundly than the internet or mobile technology ever did." — Jack Forestell (Visa Chief Product and Strategy Officer), Visa Payments Forum 2026 — https://www.pymnts.com/visa/2026/visa-launches-ai-and-stablecoin-tools-to-power-agentic-commerce/

3. "AI is transforming the front end of commerce. Stablecoins are reshaping the back end." — Jack Forestell (Visa), Visa Payments Forum 2026 — https://www.pymnts.com/visa/2026/visa-launches-ai-and-stablecoin-tools-to-power-agentic-commerce/
   - 부연: Forestell은 추천을 넘어 실제 구매까지 가는 것은 "완전히 다른 수준의 신뢰(a whole different level of trust)"가 필요하다며, 초기엔 다수 거래가 여전히 인간 승인을 거칠 것이라고 — https://fortune.com/2026/06/11/visa-chatgpt-ai-agent-payments-shopping/

4. "We are already seeing a number of services and agents popping up to provide a range of products and services." — Raj Dhamodharan (Mastercard EVP, blockchain and digital asset products and partnerships), CoinDesk, 2026-06-10 — https://www.coindesk.com/business/2026/06/10/mastercard-prepares-for-a-future-where-ai-agents-make-payments-with-latest-introduction
   - 부연: 여행 예약, 웹사이트 제작, 아트워크 생성 등 디지털 작업을 수행하는 에이전트가 등장 중이라고 언급

5. "We're seeing a fundamental shift in commerce as businesses increasingly use AI agents to transact on their behalf." / "At BVNK, we believe stablecoins will play a powerful role in enabling this change, bringing greater speed, programmability and efficiency to how value moves." — Chris Harmse (BVNK 공동창업자·최고사업책임자), Mastercard 보도자료, 2026-06-10 — https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html

(반대편 목소리 — 교차 분석용)
6. OpenAI는 Instant Checkout 후퇴를 발표하며 초기 버전이 "지향하는 수준의 유연성을 제공하지 못했다(did not offer the level of flexibility that we aspire to provide)"고 인정 — 출처: https://www.cnbc.com/2026/03/24/openai-revamps-shopping-experience-in-chatgpt-after-instant-checkout.html

---

## 반론/리스크 (반대 시각 섹션용)
1. OpenAI Instant Checkout 실패(2026-03): Shopify 수백만 가맹점 중 약 12곳만 라이브, 사용자는 ChatGPT에서 리서치는 하지만 구매는 안 함, 수백만 SKU 실시간 재고 동기화는 "10년짜리 난제", 세금·사기 방지 메커니즘 부재 — CNBC, Forrester
2. 신뢰 격차: 소비자는 수십 년간 아마존 원클릭·애플페이에 길들여져 챗봇 결제를 아직 신뢰 못 함 — CNBC
3. 프롬프트 인젝션 등 새로운 사기 벡터, 에이전트가 거래를 개시하면 전통적 사기 모델이 무력화 — IMF Note 2026/004 "How Agentic AI Will Reshape Payments" https://www.imf.org/-/media/files/publications/imf-notes/2026/english/insea2026004.pdf
4. 마이크로페이먼트 수요 미성숙: "demand is just not there yet" — CoinDesk 2026-03 https://www.coindesk.com/markets/2026/03/11/coinbase-backed-ai-payments-protocol-wants-to-fix-micropayment-but-demand-is-just-not-there-yet
5. (한국) 망분리 규제, 책임소재 불명확(현행은 금융사가 전책임), 법제 부재로 출발 지연 — 헤럴드경제 https://biz.heraldcorp.com/article/10759999 , 바이라인네트워크 https://byline.network/2026/05/0528-6/

---

## 관련 종목
- $V (Visa): Intelligent Commerce Connect + OpenAI ChatGPT 결제. "프론트엔드=AI, 백엔드=스테이블코인" 전략. 카드망 디스럽션 우려 → 오히려 레일 제공자로 전환
- $MA (Mastercard): Agent Pay for Machines, 6종 스테이블코인 멀티레일. 1센트 미만 마이크로트랜잭션
- $COIN (Coinbase): x402 표준 주도, Agentic.Market 1.65억 거래, 연 1조 달러 스테이블코인 처리. ※와치리스트 종목(딥다이브에서는 분석 대상 허용)
- $CRCL (Circle): USDC 발행사, x402 재단 멤버. 스테이블코인 레일 직접 수혜
- $PYPL (PayPal): AP2 파트너지만 구조조정·벤처부문 정리(6/17)로 상대 열위
- 카카오페이(377300.KS): 국내 유일 x402 재단 창립멤버, 원화 스테이블코인 TF
- 네이버(035420.KS): 네이버페이 간편결제 강자, 규제 해소 시 잠재 수혜
