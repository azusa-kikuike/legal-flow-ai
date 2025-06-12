# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import os
from zoneinfo import ZoneInfo

import google.auth
from google.adk.agents import Agent

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")


def get_weather(query: str) -> str:
    """Simulates a web search. Use it get information on weather.

    Args:
        query: A string containing the location to get weather information for.

    Returns:
        A string with the simulated weather information for the queried location.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."


def get_current_time(query: str) -> str:
    """Simulates getting the current time for a city.

    Args:
        city: The name of the city to get the current time for.

    Returns:
        A string with the current time information.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        tz_identifier = "America/Los_Angeles"
    else:
        return f"Sorry, I don't have timezone information for query: {query}."

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    return f"The current time for query {query} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"

def parse_legal_article(article_text: str) -> str:
    """法令条文を解析して関係者とアクションを抽出する
    
    Args:
        article_text: 解析したい法令条文のテキスト
        
    Returns:
        解析結果（関係者とアクション）をJSON形式の文字列で返す
    """
    import json
    
    # 関係者を抽出
    actors = []
    if "認証業務を行う者" in article_text:
        actors.append("認証業務事業者")
    if "申請者" in article_text:
        actors.append("申請者")
    if "総務大臣" in article_text:
        actors.append("総務大臣")
        
    # アクションを抽出
    actions = []
    if "認定する" in article_text:
        actions.append("認定")
    if "申請" in article_text:
        actions.append("申請")
    if "通知" in article_text:
        actions.append("通知")
        
    result = {
        "actors": actors,
        "actions": actions,
        "summary": f"関係者{len(actors)}名、アクション{len(actions)}個を検出"
    }
    
    return json.dumps(result, ensure_ascii=False)


# root_agentのtoolsに追加
root_agent = Agent(
    name="legal_flow_agent",  # 名前も変更
    model="gemini-2.0-flash",
    instruction="You are a legal document analysis assistant that helps extract actors and actions from Japanese legal texts.",
    tools=[get_weather, get_current_time, parse_legal_article],  # 追加
)



#root_agent = Agent(
#    name="root_agent",
#    model="gemini-2.0-flash",
#    instruction="You are a helpful AI assistant designed to provide accurate and useful information.",
#    tools=[get_weather, get_current_time],
#)
