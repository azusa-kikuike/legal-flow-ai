#!/usr/bin/env python3
"""
Streamlit Web UI for Legal Flow AI
法令文書解析のためのWebインターフェース
"""

import streamlit as st
import json
from typing import Dict, Any
import base64

# ADK関連のimport
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from app.agent import root_agent


class LegalFlowUI:
    def __init__(self):
        self.session_service = InMemorySessionService()
        self.runner = Runner(
            agent=root_agent, 
            session_service=self.session_service, 
            app_name="legal_flow_ui"
        )
    
    def process_legal_text(self, legal_text: str, user_id: str = "default_user") -> str:
        """法令条文を処理して結果を返す"""
        session = self.session_service.create_session(
            user_id=user_id, 
            app_name="legal_flow_ui"
        )
        
        message = types.Content(
            role="user", 
            parts=[types.Part.from_text(text=legal_text)]
        )
        
        # エージェントの実行
        events = list(self.runner.run(
            new_message=message,
            user_id=user_id,
            session_id=session.id
        ))
        
        # 結果の収集
        result_text = ""
        for event in events:
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        result_text += part.text + "\n"
        
        return result_text


def main():
    st.set_page_config(
        page_title="Legal Flow AI",
        page_icon="⚖️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # メインタイトル
    st.title("⚖️ Legal Flow AI")
    st.markdown("法令条文を平易な文章と業務フロー図に変換します")
    
    # サイドバー
    with st.sidebar:
        st.header("📋 使い方")
        st.markdown("""
        1. 左のテキストエリアに法令条文を入力
        2. 「解析実行」ボタンをクリック
        3. 平易な文章と業務フロー図が生成されます
        """)
        
        st.header("🔧 設定")
        user_id = st.text_input("ユーザーID", value="default_user")
        
        st.header("ℹ️ システム情報")
        st.info("Agent Development Kit (ADK) を使用")
    
    # メインコンテンツ
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📝 法令条文入力")
        legal_text = st.text_area(
            "法令条文を入力してください",
            height=300,
            placeholder="例: 申請者は総務大臣に申請し、認証業務を行う者が認定する。",
            help="解析したい法令条文を貼り付けてください"
        )
        
        # サンプルテキスト
        if st.button("📄 サンプルテキストを使用"):
            sample_text = """第三条　認証業務を行おうとする者は、総務大臣の認定を受けなければならない。
２　前項の認定を受けようとする者は、総務省令で定めるところにより、次に掲げる事項を記載した申請書を総務大臣に提出しなければならない。
３　総務大臣は、第一項の認定の申請が次の各号のいずれにも適合していると認めるときは、その認定をするものとする。"""
            st.session_state['legal_text'] = sample_text
            st.rerun()
        
        if 'legal_text' in st.session_state:
            legal_text = st.session_state['legal_text']
        
        # 解析ボタン
        if st.button("🚀 解析実行", type="primary", disabled=not legal_text.strip()):
            with st.spinner("解析中..."):
                try:
                    # Legal Flow UIインスタンスを作成
                    if 'legal_flow_ui' not in st.session_state:
                        st.session_state['legal_flow_ui'] = LegalFlowUI()
                    
                    # 解析実行
                    result = st.session_state['legal_flow_ui'].process_legal_text(
                        legal_text, user_id
                    )
                    
                    st.session_state['analysis_result'] = result
                    st.success("解析が完了しました！")
                
                except Exception as e:
                    st.error(f"エラーが発生しました: {str(e)}")
    
    with col2:
        st.header("📊 解析結果")
        
        if 'analysis_result' in st.session_state:
            result = st.session_state['analysis_result']
            
            # タブで結果を分割表示
            tab1, tab2, tab3 = st.tabs(["📋 全体結果", "📝 平易な文章", "🔄 フロー図"])
            
            with tab1:
                st.markdown("### 完全な解析結果")
                st.text_area("", value=result, height=400, disabled=True)
                
                # ダウンロードボタン
                st.download_button(
                    label="📥 結果をダウンロード",
                    data=result,
                    file_name="legal_analysis_result.txt",
                    mime="text/plain"
                )
            
            with tab2:
                st.markdown("### 平易な文章")
                # 平易な文章部分を抽出して表示（実装により調整）
                simplified_text = result  # TODO: 結果から平易な文章部分を抽出
                st.markdown(simplified_text)
            
            with tab3:
                st.markdown("### 業務フロー図")
                # Mermaid図の表示
                if "```mermaid" in result:
                    # Mermaid記法の抽出
                    mermaid_start = result.find("```mermaid") + 10
                    mermaid_end = result.find("```", mermaid_start)
                    if mermaid_end > mermaid_start:
                        mermaid_code = result[mermaid_start:mermaid_end].strip()
                        st.code(mermaid_code, language="mermaid")
                        
                        # Mermaid Live Editorへのリンク
                        encoded = base64.b64encode(mermaid_code.encode('utf-8')).decode('utf-8')
                        mermaid_url = f"https://mermaid.live/edit#{encoded}"
                        st.markdown(f"[🔗 Mermaidエディターで開く]({mermaid_url})")
                else:
                    st.info("フロー図が見つかりませんでした")
        else:
            st.info("法令条文を入力して「解析実行」ボタンをクリックしてください")
    
    # フッター
    st.markdown("---")
    st.markdown("**Legal Flow AI** - Agent Development Kit (ADK) による法令文書解析システム")


if __name__ == "__main__":
    main()