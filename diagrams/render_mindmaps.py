#!/usr/bin/env python3
"""Render the two light-theme README mind maps as self-contained SVGs."""

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"

COLORS = {
    "blue": "#2563eb",
    "green": "#078466",
    "orange": "#b45309",
    "purple": "#7c3aed",
}


def line_text(x, y, lines, *, size=20, weight=600, fill="#263447", anchor="start", gap=25):
    spans = "".join(
        f'<tspan x="{x}" dy="{0 if i == 0 else gap}">{escape(item)}</tspan>'
        for i, item in enumerate(lines)
    )
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
        f'font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Arial,sans-serif" '
        f'font-size="{size}" font-weight="{weight}" fill="{fill}">{spans}</text>'
    )


def render_group(group):
    left = group["side"] == "left"
    color = COLORS[group["color"]]
    cy = group["y"]
    cat_x = 270 if left else 735
    cat_end = 455 if left else 945
    leaf_dot = 224 if left else 976
    leaf_text = 205 if left else 995
    root_edge = 500 if left else 700
    cat_attach = cat_end if left else cat_x
    root_y = 363 if group["position"] == "top" else 397

    result = [
        f'<path d="M {root_edge} {root_y} C '
        f'{root_edge + (-60 if left else 60)} {root_y}, '
        f'{cat_attach + (58 if left else -58)} {cy}, {cat_attach} {cy}" '
        f'fill="none" stroke="{color}" stroke-width="5" stroke-linecap="round"/>',
        f'<circle cx="{cat_attach}" cy="{cy}" r="5" fill="{color}"/>',
    ]

    # The leaves fan away from each topic, as they do in a conventional mind map.
    for leaf, y in zip(group["leaves"], group["leaf_y"]):
        end_x = leaf_dot
        begin_x = cat_x if left else cat_end
        result.append(
            f'<path d="M {begin_x} {cy} C '
            f'{begin_x + (-22 if left else 22)} {cy}, '
            f'{end_x + (22 if left else -22)} {y}, {end_x} {y}" '
            f'fill="none" stroke="{color}" stroke-opacity=".72" '
            f'stroke-width="2.6" stroke-linecap="round"/>'
        )
        result.append(f'<circle cx="{end_x}" cy="{y}" r="4.5" fill="{color}"/>')
        lines = [leaf] if isinstance(leaf, str) else leaf
        result.append(
            line_text(
                leaf_text,
                y + (7 if len(lines) == 1 else -2),
                lines,
                size=18,
                weight=500,
                anchor="end" if left else "start",
                gap=21,
            )
        )

    label = group["label"]
    label_y = cy - 15 if len(label) == 1 else cy - 26
    result.append(line_text(cat_x, label_y, label, size=21, weight=700, fill=color))
    result.append(
        f'<path d="M {cat_x} {cy + 17} H {cat_end}" '
        f'stroke="{color}" stroke-width="4" stroke-linecap="round"/>'
    )
    return "\n".join(result)


def render(name, title, description, center, groups):
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="760" '
        'viewBox="0 0 1200 760" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title>',
        f'<desc id="desc">{escape(description)}</desc>',
        '<rect width="1200" height="760" fill="#ffffff"/>',
        '<g>',
    ]
    parts.extend(render_group(group) for group in groups)
    parts.extend(
        [
            '</g>',
            '<rect x="500" y="325" width="200" height="110" rx="25" '
            'fill="#17324f"/>',
            line_text(600, 365, center, size=24, weight=700, fill="#ffffff", anchor="middle", gap=29),
            '</svg>',
        ]
    )
    (OUT / name).write_text("\n".join(parts) + "\n", encoding="utf-8")


render(
    "dataset-map.svg",
    "Speech recognition dataset mind map",
    "Singapore and Southeast Asian speech datasets grouped by recording setting.",
    ["SPEECH", "DATASETS"],
    [
        {"side": "left", "position": "top", "color": "blue", "y": 180,
         "label": ["READ SPEECH"],
         "leaves": ["MNSC Parts 1–2", "Common Voice SG", "SG Streets", "IMDA2RareWord"],
         "leaf_y": [65, 120, 175, 230]},
        {"side": "left", "position": "bottom", "color": "green", "y": 570,
         "label": ["CONVERSATION"],
         "leaves": ["MNSC Part 3", "SASRBench", "AppTek en-SG", "GigaSpeechBench", "YCSEP"],
         "leaf_y": [445, 500, 555, 610, 665]},
        {"side": "right", "position": "top", "color": "orange", "y": 180,
         "label": ["CODE SWITCHING"],
         "leaves": ["MNSC Part 4", "SEAME", "ASCEND", "CS-Dialogue"],
         "leaf_y": [65, 120, 175, 230]},
        {"side": "right", "position": "bottom", "color": "purple", "y": 570,
         "label": ["LANGUAGES", "AND STYLES"],
         "leaves": ["MNSC Parts 5–6", "SEA-SpeechBench", "FLEURS", "ESD"],
         "leaf_y": [470, 525, 580, 635]},
    ],
)

render(
    "source-reuse.svg",
    "Dataset source reuse mind map",
    "Original recording sources branch to releases that use some of their material; branches do not assert exact clip overlap.",
    ["SHARED", "SOURCES"],
    [
        {"side": "left", "position": "top", "color": "blue", "y": 180,
         "label": ["NATIONAL SPEECH", "CORPUS"],
         "leaves": ["MNSC Parts 1–6", "SASRBench-v1", "Reprocessed NSC", "IMDA2RareWord"],
         "leaf_y": [65, 120, 175, 230]},
        {"side": "left", "position": "bottom", "color": "green", "y": 570,
         "label": ["COMMON VOICE"],
         "leaves": ["MCV_ACCENT SG", "SEA-SpeechBench", "Revolab public split"],
         "leaf_y": [490, 555, 620]},
        {"side": "right", "position": "top", "color": "orange", "y": 180,
         "label": ["FLEURS"],
         "leaves": ["SEA-SpeechBench", "Revolab public split"],
         "leaf_y": [130, 200]},
        {"side": "right", "position": "bottom", "color": "purple", "y": 570,
         "label": ["OTHER INPUTS"],
         "leaves": [["SG Streets →", "SEA-SpeechBench"], ["ESD →", "SEA-SpeechBench"], "TUFS Malay → Revolab"],
         "leaf_y": [490, 555, 620]},
    ],
)
