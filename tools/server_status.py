"""
舞萌DX服务器状态检查工具

提供检查舞萌DX官方服务器状态的功能。
"""

from typing import Any, Dict

from src.plugin_system import BaseTool

from ..apis.diving_fish import check_server_status


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
        content = await check_server_status()

        return {"name": self.name, "content": content}
