"""
舞萌DX API集成模块

提供与 diving-fish.com 舞萌DX探针API的集成。
"""

import aiohttp


# API 配置
BASE_URL = "https://www.diving-fish.com/api/maimaidxprober"
ALIVE_CHECK_ENDPOINT = "/alive_check"


async def check_game_server_status() -> str:
    """检查舞萌DX游戏服务器状态"""
    url = f"{BASE_URL}{ALIVE_CHECK_ENDPOINT}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("message") == "ok":
                        return "✅ **舞萌DX游戏服务器状态正常**"
                return f"⚠️ **舞萌DX游戏服务器状态异常**\n服务器异常或暂时不可用（HTTP {response.status}）。"

    except Exception as e:
        return f"⚠️ **舞萌DX游戏服务器状态异常**\n连接失败: {str(e)}"
