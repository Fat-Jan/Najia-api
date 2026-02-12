from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict, Any


@dataclass
class TransformedHexagram:
    """变卦数据类"""
    name: str
    mark: str
    qin6: List[str]
    qinx: List[str]
    gong: str
    hexagram_type: str

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            'name': self.name,
            'mark': self.mark,
            'qin6': self.qin6,
            'qinx': self.qinx,
            'gong': self.gong,
            'hexagram_type': self.hexagram_type
        }


@dataclass
class HiddenHexagram:
    """伏神数据类"""
    name: str
    mark: str
    qin6: List[str]
    qinx: List[str]
    seat: List[int]

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return {
            'name': self.name,
            'mark': self.mark,
            'qin6': self.qin6,
            'qinx': self.qinx,
            'seat': self.seat
        }


@dataclass
class HexagramResult:
    """六爻排盘结果数据类"""
    params: List[int]          # 爻位参数 [1,2,1,2,4,2]
    mark: str                 # 卦符 '111000'
    name: str                 # 卦名 '乾为天'
    gong: str                 # 卦宫 '乾'
    shiy: Tuple[int, int, int]  # (世爻, 应爻, 索引)
    qin6: List[str]          # 六亲
    qinx: List[str]          # 纳甲五行
    god6: List[str]          # 六神
    dong: List[int]           # 动爻位置
    solar: str               # 公历时间 (ISO格式)
    lunar: Dict[str, Any]    # 农历时间
    hexagram_type: str        # 卦象类型
    guaci: Optional[Dict[str, Any]] = None  # 卦辞
    bian: Optional[TransformedHexagram] = None  # 变卦
    hide: Optional[HiddenHexagram] = None     # 伏神

    def to_dict(self) -> Dict[str, Any]:
        """转换为字典（向后兼容）"""
        result = {
            'params': self.params,
            'mark': self.mark,
            'name': self.name,
            'gong': self.gong,
            'shiy': self.shiy,
            'qin6': self.qin6,
            'qinx': self.qinx,
            'god6': self.god6,
            'dong': self.dong,
            'solar': self.solar,
            'lunar': self.lunar,
            'hexagram_type': self.hexagram_type,
        }

        if self.bian is not None:
            result['bian'] = self.bian.to_dict()

        if self.hide is not None:
            result['hide'] = self.hide.to_dict()

        if self.guaci is not None:
            result['guaci'] = self.guaci

        return result

    def to_json(self) -> str:
        """转换为JSON字符串"""
        import json
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)