import os
from dotenv import load_dotenv

load_dotenv()

def test_all_av_modules():
    """测试 alpha_vantage 所有模块"""
    av_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    if not av_key:
        print("❌ 无 Alpha Vantage API Key")
        return
    
    print("=== 测试 Alpha Vantage 所有功能 ===")
    
    # 测试不同的模块 - 修正模块名称
    modules = {
        'timeseries': '股价时间序列',
        'techindicators': '技术指标', 
        'fundamentaldata': '基本面数据',  
        'alphaintelligence': '新闻情感',  
        'cryptocurrencies': '加密货币'
    }
    
    for module_name, description in modules.items():
        try:
            if module_name == 'timeseries':
                from alpha_vantage.timeseries import TimeSeries
                ts = TimeSeries(key=av_key, output_format='pandas')
                data, meta = ts.get_daily(symbol='AAPL', outputsize='compact')
                print(f"✅ {description}: 成功获取 {len(data)} 条数据")
                
            elif module_name == 'techindicators':
                from alpha_vantage.techindicators import TechIndicators
                ti = TechIndicators(key=av_key, output_format='pandas')
                data, meta = ti.get_sma(symbol='AAPL', interval='daily', time_period=20)
                print(f"✅ {description}: 成功获取技术指标")
                
            elif module_name == 'fundamentaldata':  # 修正模块名称
                from alpha_vantage.fundamentaldata import FundamentalData  # 修正类名
                fd = FundamentalData(key=av_key, output_format='pandas')
                data, meta = fd.get_company_overview(symbol='AAPL')
                print(f"✅ {description}: 模块导入成功，获取公司数据")
                
            elif module_name == 'alphaintelligence':  # 修正模块名称
                from alpha_vantage.alphaintelligence import AlphaIntelligence
                ai = AlphaIntelligence(key=av_key)
                print(f"✅ {description}: 模块导入成功")
                # 注意：可能需要查看具体的方法名来测试新闻功能
                
            elif module_name == 'cryptocurrencies':
                from alpha_vantage.cryptocurrencies import CryptoCurrencies
                cc = CryptoCurrencies(key=av_key, output_format='pandas')
                print(f"✅ {description}: 模块导入成功")
                
        except Exception as e:
            print(f"❌ {description}: {e}")

def test_simple_av():
    """简单的 Alpha Vantage 测试"""
    print("\n=== 简单功能测试 ===")
    av_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    
    try:
        from alpha_vantage.timeseries import TimeSeries
        ts = TimeSeries(key=av_key)
        
        # 修正方法名：get_quote_end → get_quote_endpoint
        data, meta = ts.get_quote_endpoint(symbol='AAPL')  # 修正方法名
        print("✅ 实时报价测试:")
        for key, value in data.items():
            print(f"   {key}: {value}")
            
    except Exception as e:
        print(f"❌ 简单测试失败: {e}")

def test_news_sentiment_api():
    """测试新闻情感API（直接调用）"""
    print("\n=== 测试新闻情感API ===")
    av_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    
    try:
        import requests
        url = "https://www.alphavantage.co/query"
        params = {
            'function': 'NEWS_SENTIMENT',
            'tickers': 'AAPL',
            'apikey': av_key,
            'limit': 3
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'feed' in data:
                print(f"✅ 新闻情感API: 成功获取 {len(data['feed'])} 条新闻")
                return True
        print(f"❌ 新闻情感API失败")
        return False
    except Exception as e:
        print(f"❌ 新闻情感API错误: {e}")
        return False

if __name__ == "__main__":
    test_all_av_modules()
    test_simple_av()
    test_news_sentiment_api()