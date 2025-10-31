import os
from dotenv import load_dotenv

load_dotenv()

def test_av_news_correct():
    """用正确的方法测试 Alpha Vantage 新闻"""
    av_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    if not av_key:
        print("❌ 无 API Key")
        return
    
    print("=== 测试 Alpha Vantage 新闻功能 ===")
    
    # 方法1: 尝试正确的模块导入
    try:
        from alpha_vantage.news_sentiment import NewsSentiment
        print("✅ 使用 'news_sentiment' 模块")
        ns = NewsSentiment(key=av_key)
        data, metadata = ns.get_company_news(symbol='AAPL')
        print(f"✅ 新闻获取成功: {len(data)} 条新闻")
        return True
    except Exception as e:
        print(f"❌ news_sentiment 失败: {e}")
    
    # 方法2: 尝试其他可能的模块名称
    try:
        from alpha_vantage.news import News
        print("✅ 使用 'news' 模块")
        return True
    except ImportError as e:
        print(f"❌ 'news' 模块不存在: {e}")
    
    # 方法3: 直接使用 API 调用
    try:
        import requests
        url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey={av_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'feed' in data:
                print(f"✅ 直接API调用成功: {len(data['feed'])} 条新闻")
                return True
        print(f"❌ API调用失败: {response.status_code}")
    except Exception as e:
        print(f"❌ 直接API调用错误: {e}")
    
    return False

def check_av_module_structure():
    """检查 alpha_vantage 包的实际结构"""
    print("\n=== 检查模块结构 ===")
    import alpha_vantage
    import inspect
    import pkgutil
    
    print("alpha_vantage 包内容:")
    for importer, modname, ispkg in pkgutil.iter_modules(alpha_vantage.__path__):
        print(f"  - {modname} (is package: {ispkg})")
    
    # 查看 timeseries 模块有哪些方法
    try:
        from alpha_vantage.timeseries import TimeSeries
        print("\nTimeSeries 方法示例:")
        methods = [method for method in dir(TimeSeries) if not method.startswith('_')]
        for method in methods[:10]:  # 只显示前10个
            print(f"  - {method}")
    except Exception as e:
        print(f"检查方法时出错: {e}")

if __name__ == "__main__":
    test_av_news_correct()
    check_av_module_structure()