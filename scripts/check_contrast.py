#!/usr/bin/env python3
"""Auditoria de contraste WCAG 2.2 para os tokens dos temas do Kanban."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ColorPair:
    theme: str
    name: str
    foreground: str
    background: str
    requirement: float
    criterion: str


PAIRS = (
    ColorPair("Claro", "Texto principal sobre fundo", "#172554", "#EEF2FF", 4.5, "1.4.3"),
    ColorPair("Claro", "Texto secundário sobre fundo", "#475569", "#EEF2FF", 4.5, "1.4.3"),
    ColorPair("Claro", "Texto sobre sidebar", "#FFFFFF", "#172B4D", 4.5, "1.4.3"),
    ColorPair("Claro", "Texto sobre botão primário", "#FFFFFF", "#2563EB", 4.5, "1.4.3"),
    ColorPair("Claro", "Texto do banner", "#FFFFFF", "#1E40AF", 4.5, "1.4.3"),
    ColorPair("Claro", "Título da coluna A Fazer", "#1D4ED8", "#FFFFFF", 4.5, "1.4.3"),
    ColorPair("Claro", "Indicador da coluna A Fazer", "#3B82F6", "#FFFFFF", 3.0, "1.4.11"),
    ColorPair("Claro", "Título da coluna Em Andamento", "#92400E", "#FFFFFF", 4.5, "1.4.3"),
    ColorPair("Claro", "Indicador da coluna Em Andamento", "#B45309", "#FFFFFF", 3.0, "1.4.11"),
    ColorPair("Claro", "Título da coluna Concluídas", "#166534", "#FFFFFF", 4.5, "1.4.3"),
    ColorPair("Claro", "Indicador da coluna Concluídas", "#15803D", "#FFFFFF", 3.0, "1.4.11"),
    ColorPair("Escuro", "Texto principal sobre superfície", "#E5EDF8", "#1E293B", 4.5, "1.4.3"),
    ColorPair("Escuro", "Texto secundário sobre superfície", "#CBD5E1", "#1E293B", 4.5, "1.4.3"),
    ColorPair("Escuro", "Texto principal sobre fundo", "#E5EDF8", "#0F172A", 4.5, "1.4.3"),
    ColorPair("Escuro", "Texto sobre sidebar", "#FFFFFF", "#0B1220", 4.5, "1.4.3"),
    ColorPair("Escuro", "Texto sobre botão primário", "#FFFFFF", "#2563EB", 4.5, "1.4.3"),
    ColorPair("Escuro", "Título e indicador da coluna A Fazer", "#60A5FA", "#1E293B", 4.5, "1.4.3"),
    ColorPair("Escuro", "Título e indicador da coluna Em Andamento", "#FBBF24", "#1E293B", 4.5, "1.4.3"),
    ColorPair("Escuro", "Título e indicador da coluna Concluídas", "#4ADE80", "#1E293B", 4.5, "1.4.3"),
)


def linearize(channel: int) -> float:
    value = channel / 255
    return value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4


def luminance(color: str) -> float:
    if len(color) != 7 or not color.startswith("#"):
        raise ValueError(f"Cor hexadecimal inválida: {color}")
    red, green, blue = (int(color[index:index + 2], 16) for index in (1, 3, 5))
    return (
        0.2126 * linearize(red)
        + 0.7152 * linearize(green)
        + 0.0722 * linearize(blue)
    )


def contrast_ratio(foreground: str, background: str) -> float:
    lighter, darker = sorted(
        (luminance(foreground), luminance(background)), reverse=True
    )
    return (lighter + 0.05) / (darker + 0.05)


def main() -> int:
    failures = 0
    print("Auditoria de contraste WCAG 2.2 AA")
    print("=" * 76)

    for pair in PAIRS:
        ratio = contrast_ratio(pair.foreground, pair.background)
        approved = ratio >= pair.requirement
        status = "APROVADO" if approved else "REPROVADO"
        failures += not approved
        print(
            f"[{status}] Tema {pair.theme} | {pair.name}: "
            f"{ratio:.2f}:1 (mínimo {pair.requirement:.1f}:1; WCAG {pair.criterion})"
        )

    print("-" * 76)
    print(f"Combinações verificadas: {len(PAIRS)}")
    print(f"Combinações reprovadas: {failures}")
    print("Resultado: " + ("FALHA" if failures else "TODAS AS COMBINAÇÕES APROVADAS"))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
