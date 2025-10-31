import requests
import json
import os
from datetime import datetime

def get_news_multiple_sources():
    """从多个免费源获取新闻"""
    news_items = []
    
    # 源1: Guardian Open API
    try:
        guardian_url = "https://content.guardianapis.com/search?api-key=test&show-fields=trailText&page-size=5"
        response = requests.get(guardian_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for item in data.get('response', {}).get('results', [])[:3]:
                news_items.append({
                    'title': item.get('webTitle', ''),
                    'description': item.get('fields', {}).get('trailText', ''),
                    'url': item.get('webUrl', ''),
                    'published_at': item.get('webPublicationDate', ''),
                    'source': 'The Guardian'
                })
            print("✓ 从 Guardian 获取新闻成功")
    except Exception as e:
        print(f"✗ Guardian API 失败: {e}")
    
    # 如果没有获取到新闻，添加一些示例数据
    if not news_items:
        news_items = get_sample_news()
    
    return news_items

def get_sample_news():
    """返回示例新闻数据（备用）"""
    return [
        {
            'title': 'Global Markets Show Mixed Performance Today',
            'description': 'Major stock indices displayed varied trends in today\'s trading session.',
            'url': 'https://example.com/news1',
            'published_at': datetime.now().isoformat(),
            'source': 'Financial Times'
        },
        {
            'title': 'Central Banks Announce Monetary Policy Decisions',
            'description': 'Key central banks around the world have released their latest policy updates.',
            'url': 'https://example.com/news2', 
            'published_at': datetime.now().isoformat(),
            'source': 'Bloomberg'
        }
    ]

def save_news_to_file(news_data):
    """保存新闻到本地JSON文件"""
    # 创建news_data目录
    os.makedirs("news_data", exist_ok=True)
    
    # 生成带时间戳的文件名
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"global_news_{today}.json"
    filepath = os.path.join("news_data", filename)
    
    # 保存到文件
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(news_data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 新闻已保存到: {filepath}")
    return filepath

def load_latest_news():
    """读取最新的新闻文件"""
    news_dir = "news_data"
    if not os.path.exists(news_dir):
        return []
    
    # 获取所有新闻文件
    news_files = [f for f in os.listdir(news_dir) if f.startswith("global_news_")]
    if not news_files:
        return []
    
    # 按日期排序，取最新的
    latest_file = sorted(news_files)[-1]
    filepath = os.path.join(news_dir, latest_file)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            news_data = json.load(f)
        print(f"✓ 从 {latest_file} 读取新闻成功")
        return news_data
    except Exception as e:
        print(f"✗ 读取新闻文件失败: {e}")
        return []

def get_global_news():
    """
    主函数：获取全球新闻
    先尝试读取本地保存的今日新闻，如果没有则重新获取
    """
    # 先检查今天是否已经有新闻
    today_news = load_latest_news()
    
    if today_news:
        print("✓ 使用本地保存的新闻")
        return today_news
    else:
        print("ℹ 本地无新闻数据，从网络获取...")
        news_data = get_news_multiple_sources()
        if news_data:
            save_news_to_file(news_data)
        return news_data

# 在你的主代码中使用：
if __name__ == "__main__":
    # 获取新闻（自动处理保存和读取）
    news = get_global_news()
    
    print(f"\n获取到 {len(news)} 条新闻:")
    for i, item in enumerate(news, 1):
        print(f"{i}. {item['title']} - {item['source']}")