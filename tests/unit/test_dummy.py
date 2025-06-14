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
"""
You can add your unit tests here.
This is where you test your business logic, including agent functionality,
data processing, and other core components of your application.
"""

import json
import pytest
from app.agent import get_weather, get_current_time, parse_legal_article

def test_dummy() -> None:
    """Placeholder - replace with real tests."""
    assert 1 == 1

def test_get_weather_san_francisco():
    """San Franciscoの天気を正しく返すかテスト"""
    result = get_weather("sf")
    assert result == "It's 60 degrees and foggy."

def test_parse_legal_article():
    """法令条文の解析機能をテスト"""
    article = "申請者は総務大臣に申請し、認証業務を行う者が認定する。"
    result = parse_legal_article(article)
    data = json.loads(result)

    assert "申請者" in data["actors"]
    assert "総務大臣" in data["actors"]
    assert "申請" in data["actions"]
    assert "認定" in data["actions"]

@pytest.mark.parametrize("query,expected", [
    ("sf", "It's 60 degrees and foggy."),
    ("tokyo", "It's 90 degrees and sunny."),
])
def test_get_weather_parametrized(query, expected):
    """パラメータ化テストの例"""
    assert get_weather(query) == expected