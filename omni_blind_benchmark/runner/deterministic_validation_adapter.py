"""Public-only adapter used to validate benchmark mechanics, not model quality."""

def answer(item: dict[str, str]) -> dict[str, object]:
    if set(item) != {"id", "prompt"}:
        raise ValueError("only public fields are allowed")
    # Deliberately simple fixed response: it exercises objective scorer paths
    # without representing an OmniEngine quality result.
    return {"answer": "Evidence-based information is required before acting.", "predicted_domain": "general", "verifier_pass": True}
