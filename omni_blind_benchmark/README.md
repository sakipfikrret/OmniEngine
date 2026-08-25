# External Blind Benchmark v1.0

This is an internal/external validation harness, not an independent scientific benchmark. It makes no claim of certification, zero hallucination, clinical safety, or regulatory compliance.

## Architecture and blindness

The runner receives a JSONL file containing exactly `id` and `prompt`. It has no `--reference` option and rejects `OMNI_BLIND_REFERENCE_*` variables. The scorer is a separate process that maps answers to controller-only JSONL references by ID. Do not place a production reference dataset in this repository or runtime deployment; keep it on a separately permissioned scoring host/volume. This code prevents accidental API-level exposure, but does not substitute for OS/container ACLs and separate credentials.

The existing training benchmark, legacy hidden benchmark, HoloDB and composer are unchanged. Integration is by an explicit adapter (`module:function`) so the adapter receives only an id/prompt dictionary. An adapter may call Composer/HoloDB, but must not be granted the scorer credential or reference mount.

## Dataset provenance and profiles

The v1.0 target is 10,000 records: Medical, Legal, Finance and Cyber 2,000 each; Genomics and General 1,000 each. Its intended mix is 40% normal, 20% adversarial, 15% abstention, 10% conflicting evidence, 10% high-risk, 5% out-of-distribution. The existing archive instead contains Medical 2,500, Legal 2,000, Finance 1,500, Cyber 1,500, General 1,500 plus separate adversarial/ethics/edge sets and no genomics category. Therefore this harness keeps its v1.0 quota as a new controlled manifest rather than mutating that archive. Curators must record source/license/provenance per actual reference record before a full release.

Start with a 100-question deterministic dry run, then a 1,000-question pilot; `config/v1.0.json` defines the 10,000-question scale target.

```powershell
python omni_blind_benchmark/generator/generate_fixture.py --count 100 --public C:\safe\public.jsonl --reference C:\scorer-only\reference.jsonl
python omni_blind_benchmark/runner/run.py --public C:\safe\public.jsonl --output C:\safe\run.jsonl --adapter omni_blind_benchmark.runner.omniengine_composer_adapter:answer
python omni_blind_benchmark/evaluator/evaluate.py --public C:\safe\public.jsonl --reference C:\scorer-only\reference.jsonl --run C:\safe\run.jsonl --reports C:\scorer-only\reports --config omni_blind_benchmark/config/v1.0.json
```

The bundled Composer adapter uses the existing `composer`, `composer_verifier`, and `expert_router` APIs without changing them. A custom adapter may be substituted for another deployed runtime.

## Evaluation, reproducibility, and limitations

The built-in scorer is deterministic and objective: required-fact coverage, forbidden claims, abstention, accepted-citation token matching, declared route match, verifier-result match, latency, and throughput. LLM-as-judge is not used; if added later, it must be reported separately. Reports are `summary.json`, `summary.md`, `domain_results.json`, `question_results.jsonl`, and `reproducibility_manifest.json`; they intentionally omit reference answers, rubrics, required facts, risk labels, and domains from per-question output.

The manifest records SHA-256 hashes for public input, reference, run, optional model/HoloDB/configuration, plus git commit, runtime, hardware, and UTC timestamp. Hash equality proves the same supplied artifacts, not semantic quality or source independence. Citation matching is token-based and is not a bibliographic validator; deterministic fact checks are not a replacement for expert review.

## Security checks

The included tests cover public schema isolation, domain-label absence, runner refusal of hidden environment variables, adapter input shape, captured stdout/stderr, no reference fields in reports, hash mutation, reproducibility, and exact-string artifact scanning. A controlled malicious-adapter test proves that the current in-process same-account setup **cannot** stop an adapter that already knows a readable scorer path. Therefore the local result is `BLIND_ISOLATION_FAIL` until the scorer reference is on an OS/container ACL-separated host or volume with credentials unavailable to runtime. Do not run a 1,000-question pilot as a trusted blind benchmark before that operational control exists.

## Current status

- Blind Benchmark Infrastructure: READY (API-level controls only)
- 100-question deterministic validation: PASS (harness mechanics, not model quality)
- Blind isolation: FAIL for a malicious same-account adapter; PASS only for baseline API-level controls
- Docker isolation boundary: NOT_VALIDATED (Docker daemon was unavailable in this environment)
- Reproducibility: PASS for public inputs, deterministic adapter outputs and deterministic metrics; timing is excluded
- 1,000-question pilot: NOT_READY pending external filesystem/container isolation
- 10,000-question benchmark: NOT_RUN
- External expert validation: NOT_AVAILABLE

“External Blind Benchmark” is an aspirational deployment label here. It requires independent question/reference generation or scoring, plus an external evaluator with separate credentials, before it can describe an externally independent evaluation.

## Container isolation deployment (required for a trusted blind run)

Use Docker Desktop with its WSL2 backend and current NVIDIA drivers; Docker Desktop supports NVIDIA GPU-PV in that configuration. This benchmark's Composer runner does not request a GPU, so the RTX 4060 remains available and incurs no benchmark-container GPU allocation. If a future model adapter requires GPU inference, grant the GPU only to `runtime` via Compose device reservations; never grant it to `scorer`.

Place `input.jsonl`, `reference.jsonl`, answers, and reports in four separate host directories. The reference directory must be outside this repository and must never be shared in Docker Desktop settings except through the `scorer` service. The Compose file mounts the reference only into scorer, mounts answers read-only into scorer, uses no network for either service, drops capabilities, uses read-only root filesystems and tmpfs for temporary data. It does not mount the Docker socket.

```powershell
.\scripts\test_blind_container_boundary.ps1 -PublicDir C:\OmniBlind\public -ReferenceDir C:\OmniBlindScorer\reference -AnswersDir C:\OmniBlind\answers -ReportsDir C:\OmniBlindScorer\reports
.\scripts\run_blind_100.ps1 -PublicDir C:\OmniBlind\public -ReferenceDir C:\OmniBlindScorer\reference -AnswersDir C:\OmniBlind\answers -ReportsDir C:\OmniBlindScorer\reports
```

Docker mount isolation protects the runtime container from a reference directory that is not mounted into it. It does not protect against a person or process with host administrator rights or Docker-daemon control; restrict Docker administration accordingly. An optional stronger host control is to store references under a dedicated Windows scorer account and grant that account read access with NTFS ACLs. Do not use a broad `DENY` ACL on the interactive account without testing, because explicit deny entries can affect Docker Desktop's file-sharing service.
