import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

def get_alpha_vantage_news(symbol='AAPL', limit=10):
    """直接调用 Alpha Vantage 新闻API"""
    av_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    if not av_key:
        print("❌ 无 API Key")
        return None
    
    url = f"https://www.alphavantage.co/query"
    params = {
        'function': 'NEWS_SENTIMENT',
        'tickers': symbol,
        'apikey': av_key,
        'limit': limit
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            
            if 'feed' in data:
                print(f"✅ 获取到 {len(data['feed'])} 条 {symbol} 新闻")
                
                # 显示前几条新闻
                for i, news in enumerate(data['feed'][:3]):
                    print(f"\n--- 新闻 {i+1} ---")
                    print(f"标题: {news.get('title', 'N/A')}")
                    print(f"来源: {news.get('source', 'N/A')}")
                    print(f"时间: {news.get('time_published', 'N/A')}")
                    print(f"摘要: {news.get('summary', 'N/A')[:100]}...")
                    
                    # 情感分析
                    sentiment = news.get('overall_sentiment_score', 0)
                    label = news.get('overall_sentiment_label', 'N/A')
                    print(f"情感: {label} (分数: {sentiment})")
                
                return data['feed']
            else:
                print(f"❌ API响应格式异常: {data}")
                return None
        else:
            print(f"❌ API调用失败: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ 请求错误: {e}")
        return None

def test_multiple_stocks_news():
    """测试多只股票的新闻"""
    stocks = ['AAPL', 'MSFT', 'GOOGL', 'TSLA']
    
    for symbol in stocks:
        print(f"\n{'='*50}")
        print(f"获取 {symbol} 新闻...")
        get_alpha_vantage_news(symbol, limit=5)

if __name__ == "__main__":
    # 测试单只股票
    get_alpha_vantage_news('AAPL')
    
    # 测试多只股票
    # test_multiple_stocks_news()