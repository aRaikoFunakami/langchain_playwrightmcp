import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
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
    セッション管理を使用してエージェントを実行する関数
    """
    # セッションを使用してMCPクライアントとの接続を管理
    async with client.session("playwright") as session:
        # セッションからツールを読み込み
        tools = await load_mcp_tools(session)
        
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