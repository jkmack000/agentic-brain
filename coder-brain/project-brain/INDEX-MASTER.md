# INDEX-MASTER — Coder Brain
<!-- type: INDEX -->
<!-- updated: 2026-02-17 -->
<!-- project: Coder Brain -->
<!-- total-files: 2 -->
<!-- capabilities: code-generation, strategy-implementation, testing, validation, refactoring -->
<!-- input-types: implement, test, fix, refactor -->
<!-- output-types: RESULT, LEARN-candidate -->
<!-- token-budget: 1500 -->
<!-- domain: freqtrade, ccxt, ta-lib, vectorbt, pytest, python -->
<!-- Load this file at the start of every Claude Code session. -->

## How to Use This Index
1. Read this file first in every session.
2. Scan entries below to find what you need.
3. Use `brain.py search "query"` for keyword search OUTSIDE context when possible.

---

## Sub-Indexes
_None yet._

---

## SPEC Files
_None yet._

---

## CODE Files
_None yet._

---

## RULE Files
_None yet._

---

## LEARN Files

### LEARN-001
- **Type:** LEARN
- **File:** learnings/LEARN-001_freqtrade-istrategy-technical-reference.md
- **Tags:** freqtrade, IStrategy, trading, python, callbacks, hyperopt, signals, indicators
- **Links:** SPEC-001
- **Backlinks:** LEARN-002
- **Summary:** Complete technical reference for Freqtrade's IStrategy interface. Covers: 3 required methods (populate_indicators/entry_trend/exit_trend) with exact signatures, DataFrame OHLCV columns, 15+ optional callback methods with full signatures (custom_stoploss, custom_exit, adjust_trade_position, leverage, etc.), parameter optimization interface (IntParameter/DecimalParameter/BooleanParameter/CategoricalParameter), signal column conventions, trailing stop mechanics, ROI table format, indicator libraries (TA-Lib, technical, pandas-ta), complete signal pattern example, and 10 code generation constraints.
- **Key decisions:** Template-fill for IStrategy (fill only populate method bodies); hyperopt parameters cannot be used in populate_indicators; always include volume > 0 guard.
- **Interface:** N/A (reference). Consumed by code generation pipeline.
- **Known issues:** TA-Lib problematic on Windows. Freqtrade crypto-focused. startup_candle_count must be ≥200.

### LEARN-002
- **Type:** LEARN
- **File:** learnings/LEARN-002_llm-code-generation-patterns.md
- **Tags:** code-generation, LLM, validation, security, sandbox, prompting, few-shot, SCoT, iteration
- **Links:** SPEC-001, LEARN-001
- **Backlinks:** _(none)_
- **Summary:** Quantitative research synthesis on LLM code generation for trading strategies. Prompting: SCoT +13.79% Pass@1, few-shot ~80% over zero-shot, prompt format varies 40%. Iteration: 3-5 rounds optimal, GPT-4o-mini 53%→75%, Gemini-flash 57%→89%. Validation: AST hallucination detection, Bandit security linting, smolagents LocalPythonExecutor (best fit for strategy validation), 4-tier sandbox hierarchy. Cross-project finding: LLM API hallucination is the consistent failure mode — every successful project required a validation layer. NexusTrade JSON-out pattern (24K users). Template-based generation recommended (eliminates structural errors).
- **Key decisions:** Knowledge-first beats guess-and-check; template-fill eliminates largest error classes; whitelist imports never blacklist; smolagents as validation model; max 3-5 iterations.
- **Interface:** N/A (research). Informs write + validation pipeline.
- **Known issues:** Academic benchmarks may differ from real-world. smolagents HuggingFace-specific. All APIs point-in-time Feb 2026.

---

## LOG Files
_None yet._
