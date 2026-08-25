"""Optional OmniEngine adapter for the blind runner.

It intentionally accepts one public record and does not import, open, or receive
any scoring reference. Keep this module in the runtime image, while evaluator
and reference material remain in the scorer environment.
"""
from pathlib import Path
import sys

PROJECT = Path(__file__).resolve().parents[2]
PYTHON_SRC = PROJECT / "src" / "python"
if str(PYTHON_SRC) not in sys.path:
    sys.path.insert(0, str(PYTHON_SRC))

from composer import synthesize_response, verify_response
from expert_router import MoERouter

_ROUTE_TO_DOMAIN = {3: "finance", 5: "cyber", 6: "legal", 7: "medical", 8: "medical", 10: "medical", 12: "medical"}
_router = MoERouter()


def answer(item: dict[str, str]) -> dict[str, object]:
    if set(item) != {"id", "prompt"}:
        raise ValueError("adapter accepts only public id and prompt")
    prompt = item["prompt"]
    expert, _confidence, _scores = _router.route_query(prompt)
    response = synthesize_response(intent="blind_benchmark_query", entities=[], rag_chunks=[], graph_context="", memory_context="", user_prompt=prompt)
    verifier_pass, _reason = verify_response(response)
    return {"answer": response, "predicted_domain": _ROUTE_TO_DOMAIN.get(expert, "general"), "verifier_pass": verifier_pass}
