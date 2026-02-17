# Coder Agent Project — First Draft

## Overview

The Coder agent is a **Python coding agent** in the Prover multi-brain system. It receives architectural designs and implementation plans from Planner and Architect agents, then writes, tests, and proves the code. Its domain is the trading infrastructure stack: Freqtrade strategies, CCXT exchange integrations, data pipelines, and supporting tooling.

This is not a template filler — it's a knowledgeable coding agent with deep, ingested understanding of the libraries it works with.

---

## Position in the Agent Chain

```
User
 └─▸ Orchestrator
      ├─▸ Architect Agent  → Designs system architecture, component interfaces
      ├─▸ Planner Agent    → Breaks designs into implementation tasks with acceptance criteria
      ├─▸ Coder Agent      → Writes, tests, proves code from plans   ← THIS DOC
      ├─▸ Donchian Brain   → Trading thesis, strategy parameters
      └─▸ Frontend Brain   → Visualization, HMI
```

**Coder receives:** Implementation plans with clear acceptance criteria, file paths, function signatures, and test expectations.

**Coder produces:** Working, tested Python code + test files + validation evidence.

**Coder does NOT:** Make architectural decisions, devise trading logic, or choose between competing approaches. Those are upstream decisions.

---

## Knowledge Architecture

The Coder agent's power comes from **pre-ingested knowledge** about the libraries and tools it works with. Without this knowledge, it's just an LLM guessing at APIs. With it, it writes correct code on the first try.

### Knowledge Sources to Ingest

| Source | What to Extract | Brain File Type | Priority |
|--------|----------------|-----------------|----------|
| **Freqtrade docs** (freqtrade.io) | IStrategy interface, callbacks, hyperopt params, bot lifecycle, configuration | LEARN + CODE | P0 |
| **Freqtrade GitHub** (github.com/freqtrade/freqtrade) | Source code patterns, IStrategy base class, sample strategies, test patterns | CODE | P0 |
| **freqtrade-strategies repo** (github.com/freqtrade/freqtrade-strategies) | Battle-tested strategy examples, common indicator patterns | CODE | P0 |
| **CCXT docs** (docs.ccxt.com) | Exchange abstraction, unified API, market structure, order types, error handling | LEARN + CODE | P1 |
| **CCXT GitHub** (github.com/ccxt/ccxt) | Python API patterns, exchange-specific quirks, async patterns | CODE | P1 |
| **ta-lib docs** | Indicator function signatures, parameter defaults, output formats | LEARN | P0 |
| **pandas-ta** (github.com/twopirllc/pandas-ta) | Alternative indicator library, DataFrame-native API | LEARN | P2 |
| **VectorBT docs** (vectorbt.dev) | Vectorized backtesting API, signal generation, portfolio simulation | LEARN + CODE | P1 |
| **Context7 GitHub** (github.com/upstash/context7) | MCP integration patterns, two-tool resolution, token-budgeted retrieval | LEARN | P1 |
| **Optuna docs** (optuna.org) | Hyperparameter optimization, trial API, pruning, Freqtrade integration | LEARN | P2 |
| **pytest docs** | Testing patterns, fixtures, parametrize, mocking | LEARN | P1 |

### Live Knowledge via Context7 MCP

Static brain files cover **project conventions and validated patterns**. Context7 MCP covers **current API reference** (auto-updated every 10-15 days across 33K+ libraries).

```
Coder Agent Session
├── Brain files → "How does OUR project use CCXT? What patterns have we validated?"
├── Context7 MCP → "What are the current parameters for ccxt.fetch_ohlcv()?"
└── GitHub MCP/CLI → "What does Freqtrade's IStrategy base class look like right now?"
```

**Rule:** Brain files are the first source of truth. Context7 supplements with current API details. GitHub is the fallback for source-level questions brain files don't cover.

### Brain File Structure

```
coder-brain/
├── project-brain/
│   ├── INIT.md
│   ├── INDEX-MASTER.md
│   ├── SESSION-HANDOFF.md
│   ├── specs/
│   │   └── SPEC-001 (this document — agent architecture)
│   ├── learnings/
│   │   ├── LEARN-001 — Freqtrade IStrategy reference (methods, params, signals, callbacks)
│   │   ├── LEARN-002 — CCXT unified API patterns (fetch_ohlcv, create_order, error taxonomy)
│   │   ├── LEARN-003 — ta-lib indicator reference (function signatures, gotchas)
│   │   ├── LEARN-004 — VectorBT API patterns (signals, portfolio, parameter sweeps)
│   │   ├── LEARN-005 — Freqtrade testing patterns (conftest, backtesting mocks, data fixtures)
│   │   ├── LEARN-006 — LLM code generation patterns (template-fill, validation, iteration)
│   │   ├── LEARN-007 — Common generation errors + fixes (accumulated over time)
│   │   └── LEARN-00x — [grows with use: new libraries, edge cases, validated patterns]
│   ├── code/
│   │   ├── CODE-001 — IStrategy template v1.0 (skeleton with fill slots)
│   │   ├── CODE-002 — VectorBT runner template
│   │   ├── CODE-003 — CCXT data fetcher patterns (sync + async)
│   │   ├── CODE-004 — Test scaffolding templates (pytest fixtures, strategy test patterns)
│   │   ├── CODE-005 — Validation pipeline implementation
│   │   └── CODE-00x — [grows: reusable snippets, indicator recipes, integration patterns]
│   ├── rules/
│   │   ├── RULE-001 — Import whitelist (allowed modules for generated strategies)
│   │   ├── RULE-002 — Code style conventions (naming, structure, provenance comments)
│   │   ├── RULE-003 — Testing requirements (what must be tested, coverage expectations)
│   │   └── RULE-004 — Security guardrails (forbidden operations, resource limits)
│   └── logs/
│       ├── LOG-001 — Generation success/failure log (patterns, error rates)
│       └── LOG-002 — Project timeline
```

---

## Input: What the Coder Receives

### From Architect Agent
- Component interfaces and contracts
- Data flow diagrams
- File/module structure decisions
- Technology choices (already made — Coder implements, doesn't choose)

### From Planner Agent
- Implementation tasks with acceptance criteria
- Ordered task list (dependencies resolved)
- File paths and function signatures to implement
- Test expectations (what to test, expected behavior)
- References to relevant brain files

### From Donchian Brain (via Orchestrator)
- Trading thesis + strategy specification
- Indicator parameters and optimization ranges
- Entry/exit logic in plain language

---

## How the Coder Writes Code

### Strategy: Knowledge-First, Not Guess-and-Check

The Coder doesn't generate code blind. Before writing anything, it:

1. **Searches its brain** for relevant patterns (indicator recipes, similar strategies, known gotchas)
2. **Queries Context7** for current API signatures if the brain doesn't cover it
3. **Uses few-shot examples** from CODE files (2-3 validated, working implementations)
4. **Reasons about control flow** before generating (SCoT pattern — think in code structures, not prose)

### Template-Fill for Strategies

For IStrategy generation, the Coder uses a template with fixed sections (imports, class skeleton, lifecycle methods) and variable sections (indicator logic, signal conditions, parameters). This eliminates structural errors entirely.

**What's fixed:** imports, class inheritance, method signatures, volume guards, return statements
**What's filled:** indicator calculations, entry/exit conditions, parameter declarations, ROI/stoploss values

### Full Generation for Non-Strategy Code

For data pipelines, CCXT integrations, utility modules, and tests — the Coder generates complete files guided by:
- Brain CODE files with validated patterns for that domain
- Architect/Planner specifications for interfaces and structure
- Context7 for current API reference

---

## How the Coder Tests Code

### Test Generation

Every implementation task produces both **code and tests**. The Coder writes:

1. **Unit tests** — individual functions and methods
2. **Integration tests** — strategy loads in Freqtrade, CCXT calls work with mock exchanges
3. **Property tests** — DataFrame operations preserve shape, signals are binary, indicators compute without NaN after startup

### Test Patterns

```python
# Strategy loading test
def test_strategy_loads():
    strategy = StrategyClassName({})
    assert strategy.timeframe == '1d'
    assert strategy.stoploss < 0

# Indicator computation test
def test_populate_indicators(sample_dataframe):
    strategy = StrategyClassName({})
    result = strategy.populate_indicators(sample_dataframe, {'pair': 'BTC/USDT'})
    assert 'donchian_upper' in result.columns
    assert not result['donchian_upper'].iloc[50:].isna().any()

# Signal generation test
def test_entry_signals(sample_dataframe_with_indicators):
    strategy = StrategyClassName({})
    result = strategy.populate_entry_trend(sample_dataframe_with_indicators, {'pair': 'BTC/USDT'})
    assert 'enter_long' in result.columns
    assert result['enter_long'].isin([0, 1, None]).all() or result['enter_long'].isna().all()

# CCXT integration test (mocked)
def test_fetch_ohlcv(mocker):
    mock_exchange = mocker.Mock()
    mock_exchange.fetch_ohlcv.return_value = [...]
    # test data pipeline with mock
```

### Pre-Built Fixtures

- `sample_dataframe` — 200 candles of realistic OHLCV data
- `sample_dataframe_with_indicators` — pre-computed indicators for signal testing
- `mock_exchange` — CCXT exchange mock with standard responses
- `minimal_config` — Freqtrade config for dry-run validation

---

## How the Coder Proves Code

### Validation Pipeline (3 stages)

```
Generated Code
     │
     ▼
┌─────────────────┐
│ Stage 1: AST    │  Syntax valid? Structural correctness?
│ Parse           │  → Fail: feed SyntaxError back to LLM
└────────┬────────┘
         ▼
┌─────────────────┐
│ Stage 2: Import │  Only allowed modules? No dangerous ops?
│ Whitelist       │  → Fail: feed forbidden import back to LLM
└────────┬────────┘
         ▼
┌─────────────────┐
│ Stage 3: Test   │  pytest passes? Dry-run completes?
│ Execution       │  → Fail: feed traceback back to LLM
└────────┬────────┘
         ▼
    RESULT: passed
```

### Import Whitelist

```python
ALLOWED_IMPORTS = {
    # Core Python
    "datetime", "typing", "dataclasses", "enum", "math", "functools",
    "collections", "itertools", "decimal", "logging",
    # Data
    "numpy", "pandas",
    # Indicators
    "talib", "talib.abstract", "technical", "technical.indicators",
    # Freqtrade
    "freqtrade.strategy", "freqtrade.vendor.qtpylib.indicators",
    "freqtrade.persistence",
    # Exchange
    "ccxt",
    # Testing
    "pytest", "unittest.mock",
}
```

- **Strategy files:** strict whitelist (no network, no filesystem, no system access)
- **Non-strategy files** (data pipelines, scripts): relaxed whitelist (allow pathlib, json, csv for file I/O)

### Iterative Refinement
- On failure: extract specific error → feed back to LLM with original plan + failed code + error
- LLM regenerates only the failing component
- **Max 3 rounds** per task (research shows diminishing returns beyond this)
- If still failing after 3 rounds: return `status: blocked` with all error messages

---

## Security Guardrails

### For Strategy Files (strict)
- Import whitelist — **whitelist, never blacklist**
- No network calls (socket, urllib, requests, http all blocked at import level)
- No filesystem writes (os, pathlib.write, shutil blocked)
- No code execution (exec, eval, compile, __import__ blocked)
- No serialization (pickle, shelve, marshal blocked)
- No system access (subprocess, ctypes, multiprocessing blocked)
- 30-second timeout on dry-run execution
- 512MB memory limit (container-level if available)

### For Non-Strategy Files (relaxed)
- Allow filesystem reads (pathlib, json, csv — needed for data pipelines)
- Allow logging
- Still block: network calls, subprocess, exec/eval, pickle
- Code review by Orchestrator before execution in production

---

## Knowledge Ingestion Plan

### Phase 1: Seed Knowledge (at brain creation)

1. **Freqtrade docs** → LEARN-001 (IStrategy reference), CODE-001 (strategy template)
2. **Freqtrade GitHub** → CODE-004 (test patterns), CODE-005 (sample strategies)
3. **freqtrade-strategies repo** → CODE files (2-3 validated examples as few-shot)
4. **CCXT docs** → LEARN-002 (unified API reference)
5. **ta-lib** → LEARN-003 (indicator reference with gotchas)

### Phase 2: Expand Knowledge (after first strategies work)

6. **VectorBT** → LEARN-004, CODE-002
7. **Optuna + Freqtrade hyperopt** → LEARN file
8. **pytest patterns** → LEARN-005, CODE-004
9. **Context7 integration** → configure MCP, test two-tool resolution

### Phase 3: Accumulate (ongoing)

- Every generation session produces discoveries → Orchestrator deposits as LEARN files
- Common errors accumulate in LEARN-007 (error patterns + fixes)
- Validated code snippets accumulate as CODE files
- Periodic consolidation every ~20-30 files

---

## Open Questions

1. Architect/Planner agent design — how do they communicate plans to Coder? (needs own spec)
2. CCXT async vs sync — which pattern for data fetchers?
3. Short/futures support — day-one or deferred?
4. Multi-timeframe template — include `informative_pairs()` scaffold?
5. VectorBT template details — deferred to CODE-002
6. How to ingest GitHub repos — clone + extract, or use GitHub MCP?
7. CCXT scope — focus on top 5 exchanges (Binance, Bybit, OKX, Kraken, Coinbase)?

---

## Known Issues

- Freqtrade dry-run requires Freqtrade installed in agent environment
- Context7 requires network — not available in air-gapped environments
- ta-lib C library installation is problematic on Windows
- CCXT is 600+ exchanges — brain can't cover all; need to scope
- Generated code quality depends on clarity of upstream Architect/Planner specs
- VectorBT validation not yet designed (Stage 3 covers IStrategy only)
