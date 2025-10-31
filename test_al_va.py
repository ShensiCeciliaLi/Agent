# 测试 Alpha Vantage 数据
from alpha_vantage.fundamentals import Fundamentals
import os
from dotenv import load_dotenv

load_dotenv()

def test_alpha_vantage_fundamentals():
    av_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    if av_key:
        try:
            # 测试获取公司基本面数据
            fundamentals = Fundamentals(key=av_key)
            data, metadata = fundamentals.get_company_overview(symbol='AAPL')
            print("✅ Alpha Vantage 基本面数据:")
            print(f"   公司: {data.get('Name', 'N/A')}")
            print(f"   行业: {data.get('Industry', 'N/A')}")
            print(f"   市盈率: {data.get('PERatio', 'N/A')}")
            return True
        except Exception as e:
            print(f"⚠️  Alpha Vantage 基本面数据获取失败: {e}")
            return False
    return False

test_alpha_vantage_fundamentals()