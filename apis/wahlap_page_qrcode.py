"""
舞萌DX API集成模块

提供与舞萌DX玩家二维码网页服务器的集成。
"""

import aiohttp


# API 配置
BASE_URL = "http://wq.wahlap.net"


async def check_qrcode_page_server_status() -> str:
    """检查舞萌DX玩家二维码网页服务器状态"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(BASE_URL) as response:
                if response.status == 200:
                    return "✅ **舞萌DX玩家二维码网页服务器状态正常**"
                return f"⚠️ **舞萌DX玩家二维码网页服务器状态异常**\n服务器异常或暂时不可用（HTTP {response.status}）。"

    except Exception as e:
        return f"⚠️ **舞萌DX玩家二维码网页服务器状态异常**\n连接失败: {str(e)}"


if __name__ == "__main__":
    import asyncio

    status = asyncio.run(check_qrcode_page_server_status())
    print(status)
