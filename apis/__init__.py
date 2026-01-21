"""
舞萌DX API模块

提供与舞萌DX相关API的集成。
"""

from .diving_fish import BASE_URL, ALIVE_CHECK_ENDPOINT, check_server_status

__all__ = ["BASE_URL", "ALIVE_CHECK_ENDPOINT", "check_server_status"]
