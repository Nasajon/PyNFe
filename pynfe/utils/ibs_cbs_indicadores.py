import csv
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Optional, Sequence


DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "IBS_CBS"


def _sanitize_key(raw_key: Optional[str]) -> str:
    if not raw_key:
        return ""
    return raw_key.strip().replace(" ", "")


def _normalize_indicator_value(key: str, raw_value: Optional[str]):
    if raw_value is None:
        return None
    value = raw_value.strip()
    if not value or value.upper() in {"N/A", "NA"}:
        return None
    if key.startswith("ind_"):
        if value == "1":
            return 1
        if value == "0":
            return 0
        return None
    return value


def _normalize_code(raw_code: Optional[str], size: Optional[int] = None) -> str:
    if raw_code is None:
        return ""
    code = str(raw_code).strip()
    if not code:
        return ""
    if size and code.isdigit():
        return code.zfill(size)
    return code


def _load_csv(filename: str, key_field: str) -> Dict[str, Dict[str, Any]]:
    path = DATA_DIR / filename
    if not path.exists():
        return {}

    with path.open(encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        data: Dict[str, Dict[str, Any]] = {}
        for row in reader:
            code = _normalize_code(row.get(key_field))
            if not code:
                continue

            normalized: Dict[str, Any] = {}
            for raw_key, raw_value in row.items():
                key = _sanitize_key(raw_key)
                if not key:
                    continue
                normalized[key] = _normalize_indicator_value(key, raw_value or "")
            data[code] = normalized

        return data


class IBSCBSIndicadores:
    _CST_FILE = "CST 2025-11-19.csv"
    _CLASS_FILE = "cClassTrib 2025-11-19.csv"

    @classmethod
    @lru_cache(maxsize=1)
    def _dados_cst(cls) -> Dict[str, Dict[str, Any]]:
        return _load_csv(cls._CST_FILE, "CST-IBS/CBS")

    @classmethod
    @lru_cache(maxsize=1)
    def _dados_classificacao(cls) -> Dict[str, Dict[str, Any]]:
        return _load_csv(cls._CLASS_FILE, "cClassTrib")

    @classmethod
    def obter_por_cst(cls, codigo: str) -> Optional[Dict[str, Any]]:
        codigo_normalizado = _normalize_code(codigo, size=3)
        return cls._dados_cst().get(codigo_normalizado)

    @classmethod
    def obter_por_classificacao(cls, codigo: str) -> Optional[Dict[str, Any]]:
        codigo_normalizado = _normalize_code(codigo, size=6)
        return cls._dados_classificacao().get(codigo_normalizado)

    @staticmethod
    def _valor_indicador(
        indicadores: Optional[Dict[str, Any]], chave: str
    ) -> Optional[int]:
        if not indicadores:
            return None
        valor = indicadores.get(chave)
        if isinstance(valor, int):
            return valor
        if isinstance(valor, str) and valor.isdigit():
            inteiro = int(valor)
            if inteiro in (0, 1):
                return inteiro
        return None

    @classmethod
    def grupo_permitido(
        cls,
        chaves: Sequence[str],
        *conjuntos: Optional[Dict[str, Any]],
    ) -> bool:
        valores: list[int] = []
        for chave in chaves:
            for indicadores in conjuntos:
                valor = cls._valor_indicador(indicadores, chave)
                if valor is not None:
                    valores.append(valor)

        if not valores:
            return True

        return all(valor == 1 for valor in valores)
