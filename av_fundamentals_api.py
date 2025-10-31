import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

def test_fundamentals_apis():
    """测试 Alpha Vantage 基本面数据API"""
    av_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    if not av_key:
        print("❌ 无 API Key")
        return
    
    print("=== 测试 Alpha Vantage 基本面数据API ===")
    
    # Alpha Vantage 基本面数据端点
    fundamental_functions = {
        'OVERVIEW': '公司概览',
        'INCOME_STATEMENT': '利润表', 
        'BALANCE_SHEET': '资产负债表',
        'CASH_FLOW': '现金流量表',
        'EARNINGS': '盈利数据'
    }
    
    for function, description in fundamental_functions.items():
        try:
            url = "https://www.alphavantage.co/query"
            params = {
                'function': function,
                'symbol': 'AAPL',
                'apikey': av_key
            }
            
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                
                if function == 'OVERVIEW':
                    print(f"✅ {description}:")
                    print(f"   公司: {data.get('Name', 'N/A')}")
                    print(f"   行业: {data.get('Industry', 'N/A')}")
                    print(f"   市盈率: {data.get('PERatio', 'N/A')}")
                    print(f"   市值: {data.get('MarketCapitalization', 'N/A')}")
                else:
                    print(f"✅ {description}: 数据获取成功")
                    
            else:
                print(f"❌ {description}: API调用失败")
                
        except Exception as e:
            print(f"❌ {description} 错误: {e}")

def test_fundamentaldata_module():
    """测试 fundamentaldata 模块（从之前的列表看到这个模块存在）"""
    print("\n=== 测试 fundamentaldata 模块 ===")
    
    try:
        from alpha_vantage.fundamentaldata import FundamentalData
        print("✅ FundamentalData 模块导入成功！")
        
        av_key = os.getenv("ALPHA_VANTAGE_API_KEY")
        fd = FundamentalData(key=av_key, output_format='pandas')
        
        # 测试获取公司概览
        data, meta = fd.get_company_overview(symbol='AAPL')
        print("✅ 公司概览数据获取成功")
        return True
        
    except ImportError as e:
        print(f"❌ FundamentalData 导入失败: {e}")
        return False
    except Exception as e:
        print(f"❌ FundamentalData 功能失败: {e}")
        return False

if __name__ == "__main__":
    test_fundamentals_apis()
    test_fundamentaldata_module()