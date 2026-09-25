#!/usr/bin/env python3
"""Builds app.js for the x402.eco ecosystem site (data: Indexter.cash snapshot)."""
import json

services = json.load(open("output/x402-eco-site/data_services.json"))

seen = set()
uniq = []
for s in services:
    key = (s["name"], s["provider"])
    if key in seen:
        continue
    seen.add(key)
    uniq.append(s)
print("unique services:", len(uniq))

NET_NAMES = {
  "eip155:8453": "Base", "eip155:137": "Polygon", "eip155:196": "Linea", "eip155:43114": "Avalanche",
  "eip155:56": "BNB Chain", "eip155:1952": "Nexus", "eip155:5042002": "Xion", "eip155:80002": "Polygon Amoy",
  "eip155:84532": "Base Sepolia", "eip155:42161": "Arbitrum", "eip155:143": "Unichain", "eip155:1329": "Sei",
  "eip155:10": "Optimism", "eip155:4663": "AppChain", "eip155:42220": "Celo", "stellar:pubnet": "Stellar",
  "algorand:wGHE2Pwdvd7S12BL5FaOP20EGYesN73ktiC1qzkkit8=": "Algorand",
  "solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp": "Solana", "solana:EtWTRABZaYq6iMfeYKouRu166VU2xqa1": "Solana Devnet",
  "base": "Base", "solana": "Solana",
}

CAT_MAP = {
  "data": "Data", "ai": "AI",
  "Wallet intelligence": "Wallet Intelligence",
  "Token & Market Data": "Data", "Token Prices": "Data", "Prices": "Data",
  "Market data": "Data", "Pools": "DeFi", "Token Data": "Data",
  "People data": "Data", "Web research": "Data",
  "Email": "Email", "Drafts": "Email", "Lists": "Email", "Threads": "Email", "Webhooks": "Email",
  "Domains": "Domains", "Phone Numbers": "Agent Communications", "Agents": "Agent Communications",
  "Agent communications": "Agent Communications", "Calls": "Agent Communications",
  "Infrastructure": "Infrastructure", "Blockchain infrastructure": "Infrastructure",
  "Wallet analytics": "Wallet Intelligence", "Wallet Data": "Wallet Intelligence",
  "Perpetuals": "DeFi", "DeFi": "DeFi", "Trading": "DeFi", "Smart Money": "DeFi",
  "Prediction Markets": "DeFi", "Portfolio": "DeFi",
  "AI models": "AI", "Administration": "Tools", "Document processing": "Tools",
  "Analytics": "Data", "Image generation": "AI", "Climate action": "Other",
  "Transactions": "Infrastructure", "Tokens": "Infrastructure", "NFTs": "NFTs",
  "Browser automation": "Tools",
}

sponsors = [
  {
    "id": "solana", "name": "Solana", "site": "https://solana.com", "role": "Settlement Layer",
    "wiki": [
      "Solana is a high-throughput Layer-1 blockchain engineered for speed and scale, processing thousands of transactions per second with sub-second finality and negligible fees. Its parallelized runtime (Sealevel) and Proof-of-History consensus make it the performance backbone for real-time, high-frequency applications.",
      "In the x402 economy, Solana has rapidly become a primary settlement layer for agentic payments — agents pay for APIs, data, and services in SOL and USDC with fees low enough to make micropayments of fractions of a cent economically viable. The majority of indexed x402 services advertise Solana payment options alongside Base.",
      "Solana's agent stack — wallet SDKs, Agent Kits, and deep DeFi liquidity — lets autonomous agents not just pay, but trade, stake, and manage treasuries natively."
    ],
    "facts": [["Throughput", "65k+ TPS"], ["Avg. fee", "$0.00025"], ["Finality", "~400ms"], ["x402 role", "Primary settlement"]],
  },
  {
    "id": "base", "name": "Base", "site": "https://base.org", "role": "Settlement Layer",
    "wiki": [
      "Base is Coinbase's Ethereum Layer-2, built on the OP Stack. It inherits Ethereum's security while offering a fraction of the cost, and ships with direct fiat on-ramps to Coinbase's 100M+ user base — the largest regulated distribution channel in crypto.",
      "Base is the birthplace of x402: the standard was introduced by Coinbase in 2025 and the deepest x402 tooling (facilitators, the Bazaar service catalog, CDP wallets) runs on Base. It remains the network with the most indexed x402 services advertising USDC settlement.",
      "For agents, Base offers deterministic sub-cent payments with ERC-4337 smart wallets, making it the default venue for x402-native service discovery."
    ],
    "facts": [["Builder", "Coinbase"], ["Tech", "OP Stack L2"], ["x402 role", "Origin & top network"], ["On-ramps", "Fiat native"]],
  },
  {
    "id": "aibtc", "name": "AIBTC", "site": "https://aibtc.com", "role": "Bitcoin Agent Infrastructure",
    "wiki": [
      "AIBTC is the first network for personal agents on Bitcoin — a DAO framework and toolchain that lets AI agents hold assets, execute contracts, and coordinate autonomously on Stacks (anchored to Bitcoin finality).",
      "AIBTC extends x402 to the Bitcoin economic zone: agents can monetize Bitcoin-anchored services, pay per call, and gate API access with x402 semantics while settling with Bitcoin-grade security guarantees underneath.",
      "Its platform turns smart contracts into callable tools for agents — the connective tissue between Bitcoin's capital base and the machine-to-machine payment web."
    ],
    "facts": [["Ecosystem", "Stacks / Bitcoin"], ["Focus", "Agent DAOs & tooling"], ["x402 role", "Bitcoin agent rails"]],
  },
  {
    "id": "celestia", "name": "Celestia", "site": "https://celestia.org", "role": "Modular Data Availability",
    "wiki": [
      "Celestia is the first modular data availability network: it decouples consensus and data availability from execution, letting any chain or rollup plug into a shared, order-of-magnitude-cheaper DA layer.",
      "In agentic payments, Celestia is positioning as the foundational performance layer: high-throughput settlement chains for machine commerce need cheap, verifiable data availability to scale to billions of micro-transactions without state bloat.",
      "Its GTM thesis for x402 emphasizes sovereignty — any agent economy can launch its own execution environment with Celestia DA underneath, avoiding congestion and centralized sequencers."
    ],
    "facts": [["Type", "Modular DA layer"], ["Tech", "Data availability sampling"], ["x402 role", "Scale-out settlement infra"]],
  },
  {
    "id": "1shotapi", "name": "1Shot API", "site": "https://1shotapi.com", "role": "On-chain Automation",
    "wiki": [
      "1Shot API is an onchain automation layer that turns smart contracts into easily callable tools for apps, workflows, and AI-driven systems — with managed wallets, transaction orchestration, and native x402 payment support.",
      "It lets AI agent developers consume contract functions as fully annotated tools, exposed via MCP or REST, so an agent can execute on-chain actions without hand-writing web3 code. n8n and Make workflows can even be monetized with x402 payments.",
      "1Shot effectively makes every smart contract an x402-purchasable service — a key supply-side on-ramp for the agentic economy."
    ],
    "facts": [["Focus", "Contracts → agent tools"], ["Supports", "x402, MCP, n8n"], ["x402 role", "Supply-side on-ramp"]],
  },
  {
    "id": "pinata", "name": "Pinata", "site": "https://pinata.cloud", "role": "IPFS & Content Delivery",
    "wiki": [
      "Pinata is the leading IPFS pinning and content delivery platform, serving billions of files for NFTs, gaming, and decentralized apps with fast, dedicated gateways.",
      "For x402, Pinata represents the content side of the machine economy: agent-generated media, metadata, and service assets need persistent, censorship-resistant hosting — and can be x402-gated so agents pay per fetch.",
      "Its APIs make it trivial for agent platforms to publish, pin, and monetize content natively in the agentic payment flow."
    ],
    "facts": [["Focus", "IPFS pinning & gateways"], ["Scale", "Billions of files"], ["x402 role", "Content & metadata layer"]],
  },
  {
    "id": "aeon", "name": "AEON", "site": "https://aeon.xyz", "role": "Agentic Payment Settlement",
    "wiki": [
      "AEON is the settlement layer bridging autonomous AI agent interactions (agent-to-agent and agent-to-merchant) with real-world value flows — an early Coinbase x402 partner that has shipped an x402 Facilitator and SDK on BNB Chain.",
      "The network connects AI agents to a 50-million-strong merchant base, letting agents complete real consumer tasks — search, compare, book, pay — end to end on x402 and AEON rails, as demonstrated in a public Coinbase Developers hackathon demo.",
      "Backed by $8M led by YZi Labs, AEON leverages AI-native protocols like x402, ERC-8004, Google AP2, and MCP to make autonomous agent transactions verifiable and settle them against real-world payment networks."
    ],
    "facts": [["Focus", "Agent payment settlement"], ["Backers", "$8M · YZi Labs"], ["x402 role", "Facilitator & SDK on BNB Chain"]],
  },
  {
    "id": "zauth", "name": "zauth", "site": "https://zauth.inc", "role": "Agent Security Infrastructure",
    "wiki": [
      "zauth is security infrastructure for the agentic internet — its Vector engine drives a real AI agent against your live app (recon, exploit, proof), so every finding is demonstrated on the running target, never guessed from signatures.",
      "Its Provider Hub runs continuous live checks on every x402 endpoint — schema, price, delivery — feeding a public registry agents can trust before they pay, while RepoScan fingerprints repositories to tell original projects from clones.",
      "For the x402 economy, zauth is the demand-side trust layer: agents transact only with endpoints proven to do what they claim, and builders catch vulnerabilities before attackers do."
    ],
    "facts": [["Focus", "Agent & endpoint security"], ["Products", "Vector · RepoScan · Provider Hub"], ["x402 role", "Endpoint verification"]],
  },
  {
    "id": "heyaura", "name": "heyAura", "site": "https://heyaura.com", "role": "Agentic Wallet Assistant",
    "wiki": [
      "heyAura is an AI wallet assistant that lives 24/7 in user wallets — allowing users to send, swap, bridge, and manage decentralized portfolios simply by describing what they want to do in natural language.",
      "In the x402 economy, heyAura integrates x402 payment settlement via facilitators like PayAI, allowing the AI assistant to autonomously query paid APIs, specialized compute, and external tooling on the user's behalf under clear risk rules.",
      "With built-in risk protection, automated APY discovery, and native $ADX utility, heyAura turns complex multi-chain DeFi flows into safe, autonomous agent interactions."
    ],
    "facts": [["Focus", "Autonomous wallet assistant"], ["Features", "Natural-language swaps · Smart yield"], ["x402 role", "Autonomous tool & API settlement"]],
  },
  {
    "id": "t54", "name": "t54.ai", "site": "https://t54.ai", "role": "Agent Trust & Risk Infrastructure",
    "wiki": [
      "t54.ai builds institutional-grade trust and risk infrastructure for the autonomous agent economy, screening over 20M transactions and verifying 41,000+ autonomous agents through its Trustline engine.",
      "Its open-source x402-Secure SDK and proxy layer add verified identity, reasoning-trace capture, intent validation, and dispute guardrails to every x402 payment flow — including launching the first x402 facilitator on XRPL supporting XRP and RLUSD.",
      "Through Claw Credit, t54 enables agent-native credit lines underwritten by its risk engine, letting agents pay for compute and x402 services without exposing owner credentials."
    ],
    "facts": [["Focus", "Agent trust, KYA & risk engine"], ["Products", "Trustline · x402-Secure · Claw Credit"], ["x402 role", "x402-Secure gateway & XRPL Facilitator"]],
  },
  {
    "id": "indexter", "name": "Indexter.cash", "site": "https://indexter.cash", "role": "Data Partner",
    "wiki": [
      "Indexter.cash is the discovery and analytics layer for the x402 ecosystem — indexing every payment-gated service on the network, its advertised price terms, and its supported settlement chains.",
      "This site's Live Services index is powered by Indexter's dataset: every service card, category, and network bar below is derived from their real-time crawl of the x402 service landscape.",
      "Indexter treats unresolved or zero-priced routes as 'terms at request' — giving an honest picture of the ecosystem rather than inflated counts."
    ],
    "facts": [["Focus", "x402 service indexing"], ["Powers", "This site's live data"], ["Coverage", "35+ providers"]],
  },
]


# X handles for backers (icon links in wiki cards)
SPONSOR_X = {
  "solana": "solana", "base": "base", "aibtc": "aibtcdev",
  "celestia": "celestiaorg", "1shotapi": "1ShotAPI", "pinata": "pinata",
  "aeon": "AEON_Community", "zauth": "zauthinc",
  "heyaura": "heyAura", "t54": "t54ai", "indexter": "IndexterCash",
}
for _s in sponsors:
    _s["x"] = SPONSOR_X.get(_s["id"], "")

people = [
  {"name":"x402 Intern","handle":"x402intern","org":"Intern @x402 @Solana @AIBTCdev @Base @Celestia · Biz Dev @deepstatesh · x402intern on TG",
   "img":"logos/people/x402intern.jpg","tweet":""},
  {"name":"Erik Reppel","handle":"programmer","org":"Head of Eng @coinbasedev · Creator of x402",
   "img":"logos/people/programmer.jpg","tweet":""},
  {"name":"Kevin Leffew","handle":"kleffew94","org":"GTM @coinbasedev · Coauthor of x402",
   "img":"logos/people/kleffew94.jpg","tweet":"https://x.com/kleffew94/status/2019609506737713251"},
  {"name":"Ben","handle":"rawgroundbeef","org":"Dev @x402jobs @memeputer @openfacilitator @x402storage @x402lint @x402eco @claw_fm",
   "img":"logos/people/rawgroundbeef.jpg","tweet":"https://x.com/rawgroundbeef/status/2010448220951089464"},
  {"name":"E.H. Vicky","handle":"bc1beat","org":"Dev @BlockRunAI",
   "img":"logos/people/bc1beat.jpg","tweet":"https://x.com/bc1beat/status/2018816429626200358"},
  {"name":"Branch","handle":"BranchM","org":"Dev @dexteraisol",
   "img":"","tweet":"https://x.com/BranchM/status/2003583954419614108"},
  {"name":"Notorious D.E.V.","handle":"notorious_d_e_v","org":"Dev @PayAINetwork",
   "img":"","tweet":"https://x.com/notorious_d_e_v/status/1978288895730020677"},
  {"name":"Drew","handle":"Drewmutable","org":"BD @pinatacloud",
   "img":"","tweet":""},
  {"name":"Todd Chapman","handle":"TtheBC01","org":"Dev @1shotapi @1shotpay",
   "img":"logos/people/tthebc01.jpg","tweet":"https://x.com/TtheBC01/status/2019987853883895867"},
  {"name":"Wayne","handle":"Crypto_Wayne97","org":"Dev @craagentarc",
   "img":"logos/people/crypto_wayne97.jpg","tweet":""},
  {"name":"Shafu","handle":"shafu0x","org":"Dev @Circle",
   "img":"logos/people/shafu0x.jpg","tweet":"https://x.com/shafu0x/status/2020522151619580392"},
  {"name":"Solking","handle":"Solkingchad","org":"Growth @Oobeonsol",
   "img":"logos/people/solkingchad.jpg","tweet":"https://x.com/Solkingchad/status/2018056335817117924"},
  {"name":"YQ","handle":"yq_acc","org":"Dev ClawNews.io · ClawSearch.io · 8004scan.io · AltLayer.io",
   "img":"logos/people/yq_acc.jpg","tweet":"https://x.com/yq_acc/status/2004952006658851350"},
  {"name":"VINNY","handle":"VinnyCorp","org":"Dev @alphakek",
   "img":"logos/people/vinnycorp.jpg","tweet":"https://x.com/VinnyCorp/status/1981653623860793426"},
  {"name":"Mani","handle":"maniusmaximus","org":"CMO at @t54ai",
   "img":"","tweet":"https://x.com/maniusmaximus/status/2019390869577560095"},
  {"name":"Ash","handle":"Must_be_Ash","org":"DevRel at @CoinbaseDev",
   "img":"logos/people/must_be_ash.jpg","tweet":"https://x.com/Must_be_Ash/status/2020921201640734778"},
  {"name":"Danny Organ","handle":"organ_danny","org":"AI @circle",
   "img":"","tweet":"https://x.com/organ_danny/status/2017347085146681515"},
  {"name":"Sam Ragsdale","handle":"samrags_","org":"CEO @merit_systems",
   "img":"logos/people/samrags_.jpg","tweet":"https://x.com/samrags_/status/2018802022649328091"},
  {"name":"Luis","handle":"microchipgnu","org":"Founder @mcpaytech",
   "img":"logos/people/microchipgnu.jpg","tweet":"https://x.com/microchipgnu/status/2018310397158416796"},
  {"name":"Tomek","handle":"0xwhyduck","org":"Chief Quality Officer at @heyAura",
   "img":"logos/people/0xwhyduck.jpg","tweet":""},
  {"name":"JW (jay,dub)","handle":"artoriatech","org":"Core contributor of @heurist_ai",
   "img":"logos/people/artoriatech.jpg","tweet":"https://x.com/artoriatech/status/1984767683012018220"},
  {"name":"Leo | aeon.xyz","handle":"alohaleonardox","org":"Building @AEON_Community",
   "img":"","tweet":"https://x.com/alohaleonardox/status/1972411082376638883"},
  {"name":"Kelsen Lu","handle":"spikel404","org":"Founder of aimo.network",
   "img":"logos/people/spikel404.jpg","tweet":""},
  {"name":"Connor","handle":"ConnorZero_","org":"Growth @m0",
   "img":"logos/people/connorzero_.jpg","tweet":"https://x.com/ConnorZero_/status/2019254567951827234"},
  {"name":"ClassicScuba","handle":"ClassicScuba","org":"3BAR for @PontusAndersson",
   "img":"","tweet":""},
]

PROJECTS = [
  {"id":"payai","name":"PayAI Network","chain":"Solana","url":"https://x.com/PayAINetwork",
   "desc":"Solana-native x402 facilitator and payment network for AI agents — gasless micropayments, paywalls, and autonomous agent-to-agent commerce."},
  {"id":"the402","name":"The402","chain":"Solana","url":"https://the402.ai",
   "desc":"A native x402 marketplace aggregating agent-purchasable services under one roof with per-call stablecoin settlement."},
  {"id":"agentphone","name":"AgentPhone","chain":"Solana","url":"https://agentphone.ai",
   "desc":"Phone numbers and voice infrastructure for AI agents, x402-gated so agents pay per call for autonomous communications."},
  {"id":"stabletickets","name":"StableTickets","chain":"Solana","url":"https://stabletickets.dev",
   "desc":"Ticketing on stablecoin rails with x402 settlement — agents can research and purchase event access autonomously."},
  {"id":"glim","name":"Glim","chain":"Solana","url":"https://glim.sh",
   "desc":"An early x402-native service provider on the growing long tail of machine-payable web services."},
  {"id":"jamesbpollack","name":"Pollack Music API","chain":"Solana","url":"https://music.jamesbpollack.com",
   "desc":"x402-gated music and creative APIs on Solana — creative content sold directly to agents per request."},
  {"id":"nansen","name":"Nansen","chain":"Base","url":"https://api.nansen.ai",
   "desc":"Wallet intelligence platform selling on-chain analytics to agents via its x402 endpoint on Base."},
  {"id":"exa","name":"Exa","chain":"Base","url":"https://api.exa.ai",
   "desc":"AI-powered search API with x402-gated endpoints — agents pay per search call with no API keys."},
  {"id":"allium","name":"Allium","chain":"Base","url":"https://agents.allium.so",
   "desc":"Enterprise blockchain data platform exposing curated datasets to x402 clients through its agent endpoints."},
  {"id":"apinow","name":"APINow","chain":"Base","url":"https://www.apinow.fun",
   "desc":"Marketplace of x402-ready APIs — lowering the barrier for any developer to sell services to the agent economy."},
  {"id":"agent402","name":"Agent402","chain":"Base","url":"https://agent402.tools",
   "desc":"Developer tooling that wraps any existing API with HTTP 402 payment gating in minutes."},
  {"id":"agentmail","name":"AgentMail","chain":"Base","url":"https://x402.api.agentmail.to",
   "desc":"Email infrastructure built for AI agents — x402-gated inboxes and domains for autonomous communication."},
  {"id":"greeneris","name":"Greeneris","chain":"Base","url":"https://data.greeneris.io",
   "desc":"Climate and ESG data APIs monetized per call through x402 on Base."},
  {"id":"coinmarketcap","name":"CoinMarketCap","chain":"Base","url":"https://pro-api.coinmarketcap.com",
   "desc":"Crypto market data authority with an x402-enabled pro API — agents purchase live prices per request."},
  {"id":"coingecko","name":"CoinGecko","chain":"Base","url":"https://pro-api.coingecko.com",
   "desc":"The largest independent crypto data aggregator; its pro API is x402-gated for machine consumption."},
  {"id":"alchemy","name":"Alchemy","chain":"Base","url":"https://x402.alchemy.com",
   "desc":"Leading web3 infrastructure provider running x402-gated node and API services on Base."},
  {"id":"robinhood","name":"Robinhood Chain","chain":"Robinhood","url":"https://robinhood.com",
   "desc":"Arbitrum Orbit L2 by Robinhood Markets — tokenized stocks and RWAs becoming machine-purchasable services via x402."},
  {"id":"arbitrum","name":"Arbitrum","chain":"Robinhood","url":"https://arbitrum.io",
   "desc":"The Orbit stack powering Robinhood Chain — the technology layer beneath its x402-capable settlement rails."},
  {"id":"interzoid","name":"Interzoid","chain":"Robinhood","url":"https://api.interzoid.com",
   "desc":"Data-quality and enrichment APIs with x402 per-call pricing — an early adopter of machine-payable data services."},
  {"id":"craagent","name":"CRA Agent","chain":"Arc","url":"https://cra-agent.tech",
   "desc":"Agent payment rail on Arc — one tool call quotes the x402 price, checks spend policy, verifies the seller via ERC-8004, and pays gas-free USDC through Circle Gateway with a written receipt."},
  {"id":"arc","name":"Arc.io","chain":"Arc","url":"https://arc.io",
   "desc":"Agent identity, payments, and policy guardrails — the trust and routing layer for autonomous x402 payment decisions."},
  {"id":"1shotapi","name":"1Shot API","chain":"Arc","url":"https://1shotapi.com",
   "desc":"On-chain automation turning smart contracts into agent-callable tools with native x402 payment support."},
  {"id":"indexter","name":"Indexter.cash","chain":"Arc","url":"https://indexter.cash",
   "desc":"The discovery and analytics layer indexing every x402 service — powers this site's live index."},
  {"id":"celestia","name":"Celestia","chain":"Celestia","url":"https://celestia.org",
   "desc":"Modular data availability network — the scale-out DA layer for high-throughput agentic payment chains."},
  {"id":"xion","name":"Xion","chain":"Celestia","url":"https://xion.burnt.com",
   "desc":"Meta-account chain with x402 services in the indexed ecosystem — abstracted wallets for agent commerce."},
  {"id":"appchain","name":"AppChain","chain":"Celestia","url":"https://appchain.xyz",
   "desc":"Sovereign app-chain infrastructure in the x402 settlement mix — execution environments with modular DA underneath."},
]

JS_BODY = r"""
const X_SVG = '<svg viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>';
const GLOBE_SVG = '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm7.93 9h-3.02a15.7 15.7 0 0 0-1.4-6.03A8.02 8.02 0 0 1 19.93 11zM12 4.06c.87 1.2 2.03 3.5 2.36 6.94H9.64c.33-3.44 1.49-5.74 2.36-6.94zM4.07 13h3.02c.15 2.24.64 4.3 1.4 6.03A8.02 8.02 0 0 1 4.07 13zm3.02-2H4.07a8.02 8.02 0 0 1 4.42-6.03A15.7 15.7 0 0 0 7.09 11zM12 19.94c-.87-1.2-2.03-3.5-2.36-6.94h4.72c-.33 3.44-1.49 5.74-2.36 6.94zm3.51-.91a15.7 15.7 0 0 0 1.4-6.03h3.02a8.02 8.02 0 0 1-4.42 6.03z"/></svg>';

let activeCat = "All";
let activeChain = "All";
let svcQuery = "";
let peopleQuery = "";

function normCat(c){ return CAT_MAP[c] || c; }

/* ---------- THEME ---------- */
function initTheme(){
  const saved = localStorage.getItem("x402eco-theme");
  const theme = saved || "dark";
  document.documentElement.setAttribute("data-theme", theme);
  document.getElementById("theme-btn").onclick = () => {
    const cur = document.documentElement.getAttribute("data-theme");
    const next = cur === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    localStorage.setItem("x402eco-theme", next);
  };
}

/* ---------- REVEAL ON SCROLL ---------- */
function initReveal(){
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target); }
  }), {threshold:.06});
  document.querySelectorAll(".section, .stat").forEach(el => io.observe(el));
}

function init(){
  initTheme();
  renderSponsors();
  renderStats();
  renderChainTabs();
  renderProjects();
  renderPeople();
  document.getElementById("people-search").addEventListener("input", e => {
    peopleQuery = e.target.value.toLowerCase();
    renderPeople();
  });
  renderFilters();
  renderServices();
  document.getElementById("svc-search").addEventListener("input", e => {
    svcQuery = e.target.value.toLowerCase();
    renderServices();
  });
  renderNetworks();
  initReveal();
}

/* ---------- BACKED ---------- */
function renderSponsors(){
  const g = document.getElementById("sponsor-grid");
  g.innerHTML = SPONSORS.map(s => `
    <div class="backed-card" onclick="toggleSponsor('${s.id}')" title="${s.name} — ${s.role}">
      <img src="logos/${s.id}.png" alt="${s.name}" class="${s.id==='celestia'?'logo-pad':''}" onerror="this.style.visibility='hidden'">
      <div class="nm">${s.name}</div>
      <div class="rl">${s.role}</div>
      <span class="chev">▾</span>
    </div>`).join("");
}

function toggleSponsor(id){
  const card = document.querySelector(`.backed-card[title^="${id}"]`) ||
               [...document.querySelectorAll(".backed-card")].find(c => c.onclick.toString().includes(id));
  const panel = document.getElementById("sponsor-panel");
  const already = card.classList.contains("open");
  document.querySelectorAll(".backed-card.open").forEach(c => c.classList.remove("open"));
  if (already){ panel.hidden = true; panel.innerHTML = ""; return; }
  card.classList.add("open");
  const s = SPONSORS.find(x => x.id === id);
  const xlink = s.x ? `<a class="icon-link" href="https://x.com/${s.x}" target="_blank" rel="noopener" title="@${s.x}">${X_SVG}</a>` : "";
  panel.innerHTML = `
    <div class="wiki-head">
      <img src="logos/${s.id}.png" alt="" class="${s.id==='celestia'?'logo-pad':''}" onerror="this.style.visibility='hidden'">
      <div><div class="t">${s.name}</div><div class="s">${s.role}</div></div>
      <div class="wiki-icons">${xlink}<a class="icon-link" href="${s.site}" target="_blank" rel="noopener" title="Website">${GLOBE_SVG}</a></div>
    </div>
    <div class="wiki-body">
      ${s.wiki.map(p=>`<p>${p}</p>`).join("")}
      <div class="wiki-facts">${s.facts.map(f=>`<span class="fact"><b>${f[0]}:</b> ${f[1]}</span>`).join("")}</div>
    </div>`;
  panel.hidden = false;
  panel.scrollIntoView({behavior:"smooth", block:"nearest"});
}

function renderWiki(){
  const g = document.getElementById("wiki-grid");
  g.innerHTML = SPONSORS.map(s => {
    const xlink = s.x ? `<a class="icon-link" href="https://x.com/${s.x}" target="_blank" rel="noopener" title="@${s.x} on X" aria-label="${s.name} on X">${X_SVG}</a>` : "";
    return `
    <div class="wiki-card" id="wiki-${s.id}">
      <div class="wiki-head">
        <img src="logos/${s.id}.png" alt="${s.name}" onerror="this.style.visibility='hidden'">
        <div>
          <div class="t">${s.name}</div>
          <div class="s">${s.role}</div>
        </div>
        <div class="wiki-icons">
          ${xlink}
          <a class="icon-link" href="${s.site}" target="_blank" rel="noopener" title="${s.site.replace(/^https?:\/\//,"").replace(/\/$/,"")}" aria-label="${s.name} website">${GLOBE_SVG}</a>
        </div>
      </div>
      <div class="wiki-body">
        ${s.wiki.map(p=>`<p>${p}</p>`).join("")}
        <div class="wiki-facts">
          ${s.facts.map(f=>`<span class="fact"><b>${f[0]}:</b> ${f[1]}</span>`).join("")}
        </div>
      </div>
    </div>`;
  }).join("");
}

/* ---------- PROJECTS BY CHAIN ---------- */
function renderChainTabs(){
  const chains = ["All", ...new Set(PROJECTS.map(p=>p.chain))];
  const t = document.getElementById("chain-tabs");
  t.innerHTML = chains.map(c => `<span class="chip${c===activeChain?" on":""}" data-chain="${c}">${c}</span>`).join("");
  t.querySelectorAll(".chip").forEach(ch => ch.onclick = () => {
    activeChain = ch.dataset.chain;
    renderChainTabs(); renderProjects();
  });
}

function renderProjects(){
  let list = PROJECTS.filter(p => activeChain==="All" || p.chain===activeChain);
  const g = document.getElementById("proj-grid");
  if (!list.length){ g.innerHTML = `<div class="no-results">No projects for this chain yet.</div>`; return; }
  g.innerHTML = list.map(p => `
    <div class="proj">
      <div class="top">
        <img src="logos/projects/${p.id}.png" alt="" loading="lazy" onerror="this.style.display='none'">
        <div class="nm">${p.name}</div>
        <span class="chain">${p.chain}</span>
      </div>
      <div class="desc">${p.desc}</div>
      <a class="visit" href="${p.url}" target="_blank" rel="noopener">Visit ↗</a>
    </div>`).join("");
}

/* ---------- PEOPLE (rotating) ---------- */
const PAGE_SIZE = 12;

function renderPeople(){
  const track = document.getElementById("belt-track");
  let list = PEOPLE.filter(p =>
    !peopleQuery ||
    p.name.toLowerCase().includes(peopleQuery) ||
    p.org.toLowerCase().includes(peopleQuery) ||
    p.handle.toLowerCase().includes(peopleQuery)
  );
  if (!list.length){ track.innerHTML = `<div class="no-results">No people match “${peopleQuery}”.</div>`; return; }
  const card = p => {
    const avatar = `<img src="${p.img || ('logos/people/' + p.handle.toLowerCase() + '.jpg')}" alt="${p.name}" onerror="this.outerHTML='<div class=\\'fallback\\'>${p.name[0]}</div>'">`;
    return `
    <div class="person">
      ${avatar}
      <div class="nm">${p.name}</div>
      <div class="org">${p.org}</div>
      <div class="plinks">
        <a class="xlink" href="https://x.com/${p.handle}" target="_blank" rel="noopener">${X_SVG} @${p.handle}</a>
      </div>
    </div>`;
  };
  // duplicate the set so translateX(-50%) loops seamlessly
  track.innerHTML = list.map(card).join("") + list.map(card).join("");
  // speed scales with list length so pace stays constant
  const secs = Math.max(30, list.length * 4);
  track.style.animationDuration = secs + "s";
}

/* ---------- STATS ---------- */
function renderStats(){
  const svc = SERVICES.length;
  const provs = new Set(SERVICES.map(s=>s.provider)).size;
  const nets = new Set(SERVICES.flatMap(s=>s.networks)).size;
  document.getElementById("st-services").innerText = svc;
  document.getElementById("st-providers").innerText = provs;
  document.getElementById("st-networks").innerText = nets;
}

/* ---------- SERVICES ---------- */
function renderFilters(){
  const cats = [...new Set(SERVICES.map(s=>normCat(s.category)))].sort();
  const counts = {};
  SERVICES.forEach(s=>{ const c=normCat(s.category); counts[c]=(counts[c]||0)+1; });
  const f = document.getElementById("filters");
  const mk = (label, val, n) => `<span class="chip${val===activeCat?" on":""}" data-cat="${val}">${label}${n?` (${n})`:""}</span>`;
  f.innerHTML = mk("All", "All", SERVICES.length) + cats.map(c=>mk(c,c,counts[c])).join("");
  f.querySelectorAll(".chip").forEach(ch => ch.onclick = () => {
    activeCat = ch.dataset.cat;
    renderFilters(); renderServices();
  });
}

function svcLogo(s){
  if (!s.url) return "";
  try {
    let host = new URL(s.url).hostname.toLowerCase();
    if (host.startsWith("www.")) host = host.slice(4);
    return `logos/svc/${host.replace(/\\./g,"_")}.png`;
  } catch(e){ return ""; }
}

function renderServices(){
  const q = svcQuery.trim();
  let list = SERVICES.filter(s => activeCat==="All" || normCat(s.category)===activeCat);
  if (q){
    list = list.filter(s =>
      (s.name||"").toLowerCase().includes(q) ||
      (s.provider||"").toLowerCase().includes(q) ||
      (s.summary||"").toLowerCase().includes(q) ||
      (s.category||"").toLowerCase().includes(q) ||
      (s.url||"").toLowerCase().includes(q)
    );
  }
  list = list.sort((a,b)=> a.name.localeCompare(b.name));
  document.getElementById("svc-count").innerText = `Showing ${list.length} of ${SERVICES.length} indexed services`;
  const g = document.getElementById("svc-grid");
  if (!list.length){ g.innerHTML = `<div class="no-results">No services match your search.</div>`; return; }
  g.innerHTML = list.map(s => {
    const chains = s.networks.map(n=>NET_NAMES[n]||n).slice(0,6);
    const seenCh = new Set(); const uniqCh = chains.filter(c=>!seenCh.has(c)&&seenCh.add(c));
    const nets = uniqCh.map(n=>`<img class="chainlogo" src="logos/chains/${n.replace(/ /g,"_")}.png" alt="${n}" title="${n}" onerror="this.outerHTML='<span class=\\'chaintext\\'>${n}</span>'">`).join("");
    const price = s.priceUsd ? `$${s.priceUsd}` : "terms at request";
    const logo = svcLogo(s);
    return `
    <div class="svc">
      ${logo ? `<img class="logo" src="${logo}" alt="" loading="lazy" onerror="this.style.display='none'">` : ""}
      <div class="body">
        <div class="top">
          <div class="nm">${s.name}</div>
          <span class="cat">${normCat(s.category)}</span>
        </div>
        <div class="sum">${s.summary||""}</div>
        <div class="meta">
          <span class="net">${nets}</span>
          <span class="mono">${s.method}</span>
          <span>${price}</span>
          ${s.url?`<a href="${s.url}" target="_blank" rel="noopener">endpoint ↗</a>`:""}
        </div>
      </div>
    </div>`;
  }).join("");
}

/* ---------- NETWORKS ---------- */
function renderNetworks(){
  const counts = {};
  SERVICES.forEach(s=>s.networks.forEach(n=>{
    const nm = NET_NAMES[n]||n;
    counts[nm]=(counts[nm]||0)+1;
  }));
  const rows = Object.entries(counts).sort((a,b)=>b[1]-a[1]).slice(0,10);
  const max = rows[0][1];
  document.getElementById("net-bars").innerHTML = rows.map(([nm,ct])=>`
    <div class="net-row">
      <span class="nm">${nm}</span>
      <div class="bar"><i style="width:${(ct/max*100).toFixed(1)}%"></i></div>
      <span class="ct mono">${ct}</span>
    </div>`).join("");
}


/* ---------- CLICKABLE STATS ---------- */
let openPanel = null;
function statRows(pairs){
  return `<div class="rows">` + pairs.map(([n,c]) =>
    `<div class="prow"><span class="n">${n}</span><span class="c">${c}</span></div>`).join("") + `</div>`;
}
function panelData(kind){
  if (kind === "services"){
    const cats = {};
    SERVICES.forEach(s=>{ const c = normCat(s.category); cats[c]=(cats[c]||0)+1; });
    const rows = Object.entries(cats).sort((a,b)=>b[1]-a[1]);
    return `<h4>Services by category</h4>` + statRows(rows);
  }
  if (kind === "providers"){
    const provs = {};
    SERVICES.forEach(s=>{ const p = (s.provider||"unknown"); provs[p]=(provs[p]||0)+1; });
    const rows = Object.entries(provs).sort((a,b)=>b[1]-a[1]).map(([p,c])=>[p.charAt(0).toUpperCase()+p.slice(1), c]);
    return `<h4>Service providers</h4>` + statRows(rows);
  }
  if (kind === "networks"){
    const nets = {};
    SERVICES.forEach(s=>s.networks.forEach(n=>{ const nm = NET_NAMES[n]||n; nets[nm]=(nets[nm]||0)+1; }));
    const rows = Object.entries(nets).sort((a,b)=>b[1]-a[1]);
    return `<h4>Settlement networks</h4>` + statRows(rows);
  }
  return "";
}
function togglePanel(kind){
  const panel = document.getElementById("stat-panel");
  document.querySelectorAll(".stat.clickable").forEach(b => b.classList.toggle("open", b.dataset.panel === kind && openPanel !== kind));
  if (openPanel === kind){ panel.hidden = true; panel.innerHTML = ""; openPanel = null; return; }
  openPanel = kind;
  panel.innerHTML = panelData(kind) + `<div class="close" onclick="togglePanel(null)">✕ close</div>`;
  panel.hidden = false;
  panel.scrollIntoView({behavior:"smooth", block:"nearest"});
}
document.querySelectorAll(".stat.clickable").forEach(b => b.onclick = () => togglePanel(b.dataset.panel));

window.onload = init;
"""


js = "\n".join([
  "// x402.eco — data embedded from Indexter.cash index (build-time snapshot)",
  f"const SERVICES = {json.dumps(uniq, ensure_ascii=False)};",
  f"const NET_NAMES = {json.dumps(NET_NAMES)};",
  f"const CAT_MAP = {json.dumps(CAT_MAP)};",
  f"const SPONSORS = {json.dumps(sponsors, ensure_ascii=False)};",
  f"const PEOPLE = {json.dumps(people, ensure_ascii=False)};",
  f"const PROJECTS = {json.dumps(sorted(PROJECTS, key=lambda p: p['name'].lower()), ensure_ascii=False)};",
  JS_BODY,
])
open("output/x402-eco-site/app.js", "w").write(js)
print("app.js written, bytes:", len(js))