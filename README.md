# LangChain Playwright MCP

このプロジェクトは、LangChainとPlaywright MCPサーバーを統合したAIエージェントの実装です。Google Gemini 2.5 Flashモデルを使用してウェブブラウザの自動化を行います。

## 概要

- **LangChain**: AIエージェントフレームワーク
- **Playwright MCP**: ウェブブラウザ自動化のためのModel Context Protocol (MCP)サーバー
- **Google Gemini 2.5 Flash**: 高速な大規模言語モデル
- **uv**: Pythonパッケージマネージャー

## 機能

- YouTube動画の検索・再生
- ウェブページの自動操作
- AIエージェントによる自然言語でのブラウザ制御

## システム要件

- Python 3.13以上
- Node.js（npxコマンド用）
- uv（パッケージマネージャー）

## 依存関係

```toml
dependencies = [
    "langchain>=0.3.26",
    "langchain-anthropic>=0.3.17",
    "langchain-google-genai>=2.1.6",
    "langchain-mcp-adapters>=0.1.8",
    "langchain-openai>=0.3.27",
    "langgraph>=0.5.1",
    "openai>=1.93.0",
]
```

## セットアップ

1. リポジトリをクローン

```bash
git clone https://github.com/aRaikoFunakami/langchain_playwrightmcp.git
cd langchain_playwrightmcp
```

1. uvを使用して依存関係をインストール

```bash
uv sync
```

1. 仮想環境をアクティベート

```bash
source .venv/bin/activate
```

1. Google Gemini APIキーを環境変数に設定

```bash
export GOOGLE_API_KEY="your-api-key"
```

## 使用方法

### 基本的な使用例

```bash
uv run main.py
```

プログラムは自動的にYouTubeでサンドイッチマンの漫才動画を検索し、再生を試みます。

### コードの構造

```python
# MCPクライアントの設定
client = MultiServerMCPClient({
    "playwright": {
        "command": "npx",
        "args": ["@playwright/mcp@latest"],
        "transport": "stdio",
    }
})

# エージェントの実行
async def run_agent():
    tools = await client.get_tools()
    agent = create_react_agent("google_genai:gemini-2.5-flash", tools)
    response = await agent.ainvoke({
        "messages": [{"role": "user", "content": "youtubeでサンドイッチマンの漫才の動画を検索して動画を再生して"}]
    })
```

## アーキテクチャ

1. **MultiServerMCPClient**: 複数のMCPサーバーを管理
2. **Playwright MCP**: ウェブブラウザの自動化機能を提供
3. **ReActエージェント**: 推論と行動を組み合わせたAIエージェント
4. **Google Gemini**: 自然言語理解と生成


## トラブルシューティング

### よくある問題

1. **npxコマンドが見つからない**
   - Node.jsをインストールしてください

2. **Google Gemini APIキーエラー**
   - 環境変数`GOOGLE_API_KEY`が設定されていることを確認してください

3. **Playwright MCPサーバーが起動しない**
   - `@playwright/mcp`パッケージが最新版であることを確認してください

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。

## 貢献

プルリクエストや問題報告を歓迎します。

## 更新履歴

- v0.1.0: 初回リリース
  - LangChain + Playwright MCP統合
  - Google Gemini 2.5 Flash対応
  - YouTube動画検索・再生機能