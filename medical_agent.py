class MedicalAgent:
    """Simple medical agent implementing basic helper methods."""

    def __init__(self, api_key: str | None = None, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model
        self.openai = None
        if api_key:
            try:
                import openai  # type: ignore
                openai.api_key = api_key
                self.openai = openai
            except ImportError:
                raise ImportError("openai package not installed. Install openai to use API features.")

    def _chat(self, prompt: str) -> str:
        """Internal helper for optional OpenAI interaction."""
        if self.openai:
            response = self.openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message["content"].strip()
        return "Model not configured."

    def get_differential_diagnosis(self, symptoms: str) -> str:
        """Return a differential diagnosis given a set of symptoms."""
        prompt = (
            f"Given the following symptoms: {symptoms}. "
            "Provide a concise differential diagnosis list."
        )
        return self._chat(prompt)

    def suggest_treatment(self, diagnosis: str) -> str:
        """Suggest a treatment plan for the provided diagnosis."""
        prompt = (
            f"Based on the diagnosis '{diagnosis}', suggest an appropriate treatment plan.""
        )
        return self._chat(prompt)

    def triage_patient(self, urgency_level: str) -> str:
        """Provide triage instructions based on the urgency level."""
        prompt = (
            f"A patient is presenting with an urgency level of '{urgency_level}'. "
            "Advise on immediate steps for triage."
        )
        return self._chat(prompt)
