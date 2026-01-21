"""
MaiBot 舞萌插件

提供舞萌DX相关功能。
"""

from typing import List, Tuple, Type

from src.plugin_system import (
    BasePlugin,
    register_plugin,
    ComponentInfo,
    ConfigField,
)

from .tools import MaimaiServerStatusTool


@register_plugin
class MaimaiDXPlugin(BasePlugin):
    """MaiBot 舞萌DX插件 - 提供舞萌DX相关功能"""

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
            "enabled": ConfigField(type=bool, default=True, description="是否启用插件"),
        },
    }

    def get_plugin_components(self) -> List[Tuple[ComponentInfo, Type]]:
        """返回插件包含的组件列表"""
        return [
            (MaimaiServerStatusTool.get_tool_info(), MaimaiServerStatusTool),
        ]
