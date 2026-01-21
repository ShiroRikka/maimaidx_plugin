"""
舞萌DX API集成模块

提供与 diving-fish.com 舞萌DX探针API的集成。
"""

import aiohttp
from typing import Any, Dict


# API 配置
BASE_URL = "https://www.diving-fish.com/api/maimaidxprober"
ALIVE_CHECK_ENDPOINT = "/alive_check"


async def check_server_status() -> Dict[str, Any]:
    """
    检查舞萌DX官方服务器状态

    Returns:
        dict: 包含服务器状态信息的字典
            - status: str, 状态类型 ("ok", "error", "connection_failed", "unknown")
            - message: str, 状态描述
            - raw_response: Optional[Any], 原始响应数据
    """
    url = f"{BASE_URL}{ALIVE_CHECK_ENDPOINT}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status == 200:
                    data = await response.json()
                    if data.get("message") == "ok":
                        return {
                            "status": "ok",
                            "message": "服务器已上线，可以正常访问。",
                            "raw_response": data,
                        }
                    else:
                        return {
                            "status": "error",
                            "message": f"服务器返回了意外响应：{data}",
                            "raw_response": data,
                        }
                else:
                    return {
                        "status": "connection_failed",
                        "message": f"HTTP状态码: {response.status}，服务器可能正在维护或暂时不可用。",
                        "raw_response": None,
                    }

    except aiohttp.ClientError as e:
        return {
            "status": "connection_failed",
            "message": f"连接错误: {str(e)}",
            "raw_response": None,
        }
    except Exception as e:
        return {
            "status": "unknown",
            "message": f"发生未知错误: {str(e)}",
            "raw_response": None,
        }


def format_status_response(result: Dict[str, Any]) -> str:
    """
    格式化服务器状态响应消息

    Args:
        result: check_server_status 返回的结果

    Returns:
        str: 格式化后的状态消息
    """
    status = result.get("status", "unknown")
    message = result.get("message", "未知错误")

    if status == "ok":
        return f"✅ **舞萌服务器状态正常**\n\n{message}"
    elif status == "error":
        return f"⚠️ **舞萌服务器状态异常**\n\n{message}"
    elif status == "connection_failed":
        return f"❌ **舞萌服务器连接失败**\n\n{message}"
    else:
        return f"❌ **舞萌服务器状态检查失败**\n\n{message}"
