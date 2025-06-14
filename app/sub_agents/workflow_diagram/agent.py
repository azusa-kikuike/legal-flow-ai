from google.adk.agents.llm_agent import Agent
from . import prompt


def generate_mermaid_image_url(mermaid_code: str) -> str:
    """MermaidコードをMermaid Live Editorの画像URLに変換"""
    import base64
    import json
    
    # JSON形式で設定を含めたconfig（より確実）
    config = {
        "code": mermaid_code,
        "mermaid": {
            "theme": "default"
        }
    }
    
    # UTF-8エンコードしてBase64変換
    json_str = json.dumps(config)
    base64_data = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
    return f"https://mermaid.live/edit#{base64_data}"


def generate_diagram_with_image(mermaid_code: str) -> dict:
    """Mermaidコードと画像URLを返す"""
    image_url = generate_mermaid_image_url(mermaid_code)
    return image_url 


workflow_diagram_agent = Agent(
    name="workflow_diagram_agent",
    model='gemini-2.0-flash',
    description="Analyzes legal articles and creates business workflow diagrams",
    instruction=prompt.WORKFLOW_DIAGRAM_AGENT_PROMPT,
    tools=[generate_diagram_with_image],
)