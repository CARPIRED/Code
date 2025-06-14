class MedicalAgent:
    """Simple medical agent implementing basic helper methods."""

    def __init__(self, api_key: str | None = None, model: str = "gpt-3.5-turbo"):
        """Initialize the agent and configure optional OpenAI access.

        The method checks the ``MEDICAL_AGENT_API_KEY`` or ``OPENAI_API_KEY``
        environment variables when ``api_key`` is not explicitly provided. This
        allows configuring the key without hardcoding it in the application.
        """

        import os

        if api_key is None:
            api_key = os.getenv("MEDICAL_AGENT_API_KEY") or os.getenv("OPENAI_API_KEY")

        self.api_key = api_key
        self.model = model
        self.openai = None

        if api_key:
            try:
                import openai  # type: ignore
                openai.api_key = api_key
                self.openai = openai
            except ImportError as exc:
                raise ImportError(
                    "openai package not installed. Install openai to use API features."
                ) from exc

    def _chat(self, prompt: str) -> str:
        """Internal helper for optional OpenAI interaction."""
        if not self.openai:
            return "Model not configured."

        try:
            response = self.openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
            )
            return response["choices"][0]["message"]["content"].strip()
        except Exception as exc:
            return f"Error communicating with the model: {exc}"

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
            f"Based on the diagnosis '{diagnosis}', suggest an appropriate treatment plan."
        )
        return self._chat(prompt)

    def triage_patient(self, urgency_level: str) -> str:
        """Provide triage instructions based on the urgency level."""
        prompt = (
            f"A patient is presenting with an urgency level of '{urgency_level}'. "
            "Advise on immediate steps for triage."
        )
        return self._chat(prompt)
