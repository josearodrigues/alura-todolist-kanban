#!/usr/bin/env python3
"""Script de validação de cobertura de testes conforme metas do RNF03 e Decisão Técnica 3.5.

Metas obrigatórias:
- Cobertura de linhas: percent_covered >= 90.0%
- Cobertura de ramos: percent_branches_covered >= 85.0%
"""

import json
import sys
from pathlib import Path

MIN_LINE_COVERAGE = 90.0
MIN_BRANCH_COVERAGE = 85.0
COVERAGE_FILE = Path("coverage.json")


def verify_coverage() -> int:
    if not COVERAGE_FILE.exists():
        print(f"ERRO: Arquivo de cobertura '{COVERAGE_FILE}' não encontrado.", file=sys.stderr)
        return 1

    try:
        with open(COVERAGE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"ERRO: Falha ao ler '{COVERAGE_FILE}': {e}", file=sys.stderr)
        return 1

    totals = data.get("totals", {})
    percent_covered = totals.get("percent_covered")
    percent_branches_covered = totals.get("percent_branches_covered")

    if percent_covered is None or percent_branches_covered is None:
        print("ERRO: Campos de cobertura ausentes em 'coverage.json'.", file=sys.stderr)
        return 1

    print("=== Relatório de Verificação de Cobertura ===")
    print(f"Cobertura de linhas (percent_covered): {percent_covered:.2f}% (Meta: >= {MIN_LINE_COVERAGE:.1f}%)")
    print(f"Cobertura de ramos (percent_branches_covered): {percent_branches_covered:.2f}% (Meta: >= {MIN_BRANCH_COVERAGE:.1f}%)")

    has_error = False

    if percent_covered < MIN_LINE_COVERAGE:
        print(f"FALHA: Cobertura de linhas ({percent_covered:.2f}%) abaixo da meta de {MIN_LINE_COVERAGE:.1f}%!", file=sys.stderr)
        has_error = True

    if percent_branches_covered < MIN_BRANCH_COVERAGE:
        print(f"FALHA: Cobertura de ramos ({percent_branches_covered:.2f}%) abaixo da meta de {MIN_BRANCH_COVERAGE:.1f}%!", file=sys.stderr)
        has_error = True

    if has_error:
        return 1

    print("SUCESSO: Todas as metas de cobertura de testes foram atendidas.")
    return 0


if __name__ == "__main__":
    sys.exit(verify_coverage())
