"""
main.py - 基本的なMCPクライアント実装
直接client.get_tools()を使用してツールを取得する方式
"""
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

# Playwright MCPサーバーの設定
# npxコマンドを使用して@playwright/mcpパッケージを実行
client = MultiServerMCPClient(
    {
        "playwright": {
            "command": "npx",
            "args": [
                "@playwright/mcp@latest",
            ],
            "transport": "stdio",
        }
    }
)

async def run_agent():
    """
    エージェントを実行する関数
    直接client.get_tools()でツールを取得し、Google Gemini 2.5 Flashモデルを使用
    """
    # クライアントから直接ツールを取得
    tools = await client.get_tools()
    
    # ReAct エージェントを作成（Google Geminiモデルを使用）
    agent = create_react_agent("google_genai:gemini-2.5-flash", tools)

    # YouTubeでサンドイッチマンの漫才動画を検索・再生するタスクを実行
    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "youtubeでサンドイッチマンの漫才の動画を検索して動画を再生して"}]}
    )
    
    # レスポンスメッセージの内容を出力
    print("Agent response:", response["messages"][-1].content)

if __name__ == "__main__":
    # メイン実行部：非同期関数を実行
    asyncio.run(run_agent())