"""
舞萌DX API模块

提供与舞萌DX相关API的集成。
"""

from .diving_fish import check_game_server_status
from .wahlap_page_qrcode import check_qrcode_page_server_status

__all__ = ["check_game_server_status", "check_qrcode_page_server_status"]
