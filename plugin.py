"""
MaiBot 舞萌插件

提供舞萌DX相关功能。
"""

import aiohttp
from typing import Any, Dict, Tuple, Type, List

from src.plugin_system import (
    BasePlugin,
    register_plugin,
    BaseTool,
    ComponentInfo,
    ConfigField,
)


# API 配置
BASE_URL = "https://www.diving-fish.com/api/maimaidxprober"
ALIVE_CHECK_ENDPOINT = "/alive_check"


class MaimaiServerStatusTool(BaseTool):
    """舞萌服务器状态检查工具"""

    name = "maimai_server_status_check"
    description = (
        "检查舞萌DX官方服务器的状态。询问舞萌、华立服务器是否正常、修好了没、能否登录、还活着吗、能玩了吗等情况时使用。"
    )
    available_for_llm = True
    parameters = []

    async def execute(self, function_args: Dict[str, Any]) -> Dict[str, Any]:
        """
        执行服务器状态检查

        Returns:
            dict: 包含服务器状态信息的字典
        """
        try:
            # 构建完整URL
            url = f"{BASE_URL}{ALIVE_CHECK_ENDPOINT}"

            # 发送GET请求检查服务器状态
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                    if response.status == 200:
                        data = await response.json()
                        if data.get("message") == "ok":
                            return {
                                "name": self.name,
                                "content": "✅ **舞萌服务器状态正常**\n\n服务器已上线，可以正常访问。",
                            }
                        else:
                            return {
                                "name": self.name,
                                "content": f"⚠️ **舞萌服务器状态异常**\n\n服务器返回了意外响应：{data}",
                            }
                    else:
                        return {
                            "name": self.name,
                            "content": f"❌ **舞萌服务器连接失败**\n\nHTTP状态码: {response.status}\n服务器可能正在维护或暂时不可用。",
                        }

        except aiohttp.ClientError as e:
            return {
                "name": self.name,
                "content": f"❌ **舞萌服务器连接失败**\n\n连接错误: {str(e)}\n请检查网络连接或稍后再试。",
            }
        except Exception as e:
            return {"name": self.name, "content": f"❌ **舞萌服务器状态检查失败**\n\n发生未知错误: {str(e)}"}


@register_plugin
class MaimaiServerStatusPlugin(BasePlugin):
    """MaiBot 舞萌插件"""

    plugin_name: str = "maimaidx_plugin"
    enable_plugin: bool = True
    dependencies: List[str] = []
    python_dependencies: List[str] = ["aiohttp"]
    config_file_name: str = "config.toml"

    # 配置节描述
    config_section_descriptions = {
        "plugin": "插件启用配置",
    }

    # 配置Schema定义
    config_schema: dict = {
        "plugin": {
            "config_version": ConfigField(type=str, default="1.0.0", description="配置文件版本"),
            "enabled": ConfigField(type=bool, default=True, description="是否启用插件"),
        },
    }

    def get_plugin_components(self) -> List[Tuple[ComponentInfo, Type]]:
        """返回插件包含的组件列表"""
        return [
            (MaimaiServerStatusTool.get_tool_info(), MaimaiServerStatusTool),
        ]
