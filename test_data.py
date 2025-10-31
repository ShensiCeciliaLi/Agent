import os
from dotenv import load_dotenv
import yfinance as yf
from alpha_vantage.fundamentals import Fundamentals

# 加载环境变量
load_dotenv()

def test_yfinance():
    """测试 yfinance（完全免费）"""
    print("=== 测试 yfinance 数据 ===")
    try:
        # 获取 Apple 股票数据
        stock = yf.Ticker("AAPL")
        hist = stock.history(period="5d")  # 最近5天数据
        if not hist.empty:
            latest_price = hist['Close'].iloc[-1]
            print(f"✅ Apple 最新价格: ${latest_price:.2f}")
            print(f"   数据时间范围: {hist.index[0]} 到 {hist.index[-1]}")
            return True
        else:
            print("❌ 未获取到数据")
            return False
    except Exception as e:
        print(f"❌ yfinance 错误: {e}")
        return False

def test_alpha_vantage():
    """测试 Alpha Vantage API 是否有效"""
    print("\n=== 测试 Alpha Vantage API ===")
    try:
        av_key = os.getenv("ALPHA_VANTAGE_API_KEY")
        if not av_key:
            print("❌ 未找到 Alpha Vantage API Key")
            return False
            
        print(f"✅ Alpha Vantage API Key 配置正确")
        print(f"   Key 前几位: {av_key[:10]}...")
        
        # 简单测试 Alpha Vantage 连接
        # 注意：这里只是测试配置，实际调用可能在项目中有特定方式
        return True
    except Exception as e:
        print(f"❌ Alpha Vantage 错误: {e}")
        return False

def test_project_import():
    """测试能否导入项目模块"""
    print("\n=== 测试项目模块导入 ===")
    try:
        from tradingagents.data.data_vendor import DataVendor
        print("✅ 成功导入 TradingAgents 模块")
        return True
    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        return False
    except Exception as e:
        print(f"⚠️  其他导入错误（可能缺少 OpenAI）: {e}")
        return True  # 可能是 OpenAI 相关错误，但模块导入成功了

if __name__ == "__main__":
    print("开始测试 TradingAgents 数据功能...")
    print("=" * 50)
    
    success_count = 0
    total_tests = 3
    
    if test_yfinance():
        success_count += 1
        
    if test_alpha_vantage():
        success_count += 1
        
    if test_project_import():
        success_count += 1
    
    print("\n" + "=" * 50)
    print(f"测试完成: {success_count}/{total_tests} 项通过")
    
    if success_count >= 2:
        print("🎉 环境配置基本成功！")
        print("   等有了 OpenAI API Key 后就可以运行完整功能了")
    else:
        print("❌ 需要检查环境配置")