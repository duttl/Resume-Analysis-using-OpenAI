from ats.llm_chatgpt import analyze_resume
from unittest.mock import patch

@patch("ats.llm_chatgpt.openai.ChatCompletion.create")
def test_analyze_resume_returns_expected_output(mock_create):
    mock_create.return_value = {
        "choices": [{
            "message": {
                "content": "Match Score: 8/10"
            }
        }]
    }


    result = analyze_resume("resume text", "job description")
    assert "8/10" in result

