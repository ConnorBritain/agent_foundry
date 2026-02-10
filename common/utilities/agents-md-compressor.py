#!/usr/bin/env python3
"""
Documentation compressor for Agent Foundry.

Scans a directory of documentation files and generates a compressed,
pipe-delimited index format suitable for inclusion in ``agents.md`` files.
The compressed format dramatically reduces token consumption while preserving
the information an agent needs to locate and retrieve relevant documents.

Three output styles are supported:
  - **api**   -- Pipe-delimited section index (best for API references)
  - **prose** -- Section summaries with file references (best for guides)
  - **code**  -- Function/class signatures only (best for code examples)

Usage:
    python agents-md-compressor.py <docs-directory>
    python agents-md-compressor.py <docs-directory> --output agents.md
    python agents-md-compressor.py <docs-directory> --style api
    python agents-md-compressor.py <docs-directory> --style prose
    python agents-md-compressor.py <docs-directory> --style code

Examples:
    python agents-md-compressor.py docs/
    python agents-md-compressor.py docs/ --output compressed-agents.md --style api
    python agents-md-compressor.py docs/ --style code --validate
"""

import argparse
import os
import re
import sys
from collections import OrderedDict
from pathlib import Path

# ---------------------------------------------------------------------------
# Token estimation (same heuristic as token-calculator.py)
# ---------------------------------------------------------------------------

_TOKEN_MULTIPLIER = 1.3


def _estimate_tokens(text):
    """Estimate token count using a word-based heuristic."""
    return max(1, int(len(text.split()) * _TOKEN_MULTIPLIER))


# ---------------------------------------------------------------------------
# Directory scanning
# ---------------------------------------------------------------------------

_DOC_EXTENSIONS = {".md", ".txt", ".rst", ".adoc", ".org"}
_CODE_EXTENSIONS = {".py", ".js", ".ts", ".jsx", ".tsx", ".sh", ".bash"}
_ALL_EXTENSIONS = _DOC_EXTENSIONS | _CODE_EXTENSIONS


def _scan_directory(docs_dir):
    """Scan *docs_dir* and group files by their immediate subdirectory.

    Files in the root of *docs_dir* are placed in a ``_root`` group.

    Returns:
        OrderedDict: section_name -> sorted list of Path objects.
    """
    root = Path(docs_dir)
    sections = OrderedDict()

    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in _ALL_EXTENSIONS:
            continue
        # Skip hidden files / directories
        rel = path.relative_to(root)
        if any(p.startswith(".") for p in rel.parts):
            continue

        # Determine the section name
        if len(rel.parts) == 1:
            section = "_root"
        else:
            section = rel.parts[0]

        sections.setdefault(section, []).append(path)

    return sections


def _extract_heading(text):
    """Extract the first markdown heading from *text*, if any."""
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return None


def _extract_first_paragraph(text):
    """Extract the first non-empty paragraph from markdown *text*."""
    lines = text.split("\n")
    paragraph = []
    started = False
    for line in lines:
        stripped = line.strip()
        # Skip frontmatter
        if stripped == "---" and not started:
            continue
        # Skip headings
        if stripped.startswith("#"):
            if started:
                break
            continue
        if stripped:
            started = True
            paragraph.append(stripped)
        elif started:
            break
    return " ".join(paragraph)[:200] if paragraph else ""


def _extract_code_signatures(text, file_path):
    """Extract function/class signatures from a code file.

    Returns a list of signature strings.
    """
    signatures = []
    suffix = Path(file_path).suffix.lower()

    if suffix == ".py":
        for match in re.finditer(r"^((?:async\s+)?(?:def|class)\s+\w+[^:]*)", text, re.MULTILINE):
            signatures.append(match.group(1).strip())
    elif suffix in {".js", ".ts", ".jsx", ".tsx"}:
        # function declarations
        for match in re.finditer(
            r"^(?:export\s+)?(?:async\s+)?function\s+\w+\s*\([^)]*\)", text, re.MULTILINE
        ):
            signatures.append(match.group(0).strip())
        # arrow functions assigned to const/let
        for match in re.finditer(
            r"^(?:export\s+)?(?:const|let)\s+(\w+)\s*=\s*(?:async\s+)?\(", text, re.MULTILINE
        ):
            signatures.append(f"const {match.group(1)} = (...)")
        # class declarations
        for match in re.finditer(
            r"^(?:export\s+)?class\s+\w+(?:\s+extends\s+\w+)?", text, re.MULTILINE
        ):
            signatures.append(match.group(0).strip())
    elif suffix in {".sh", ".bash"}:
        for match in re.finditer(r"^(\w+)\s*\(\)", text, re.MULTILINE):
            signatures.append(f"{match.group(1)}()")

    return signatures


# ---------------------------------------------------------------------------
# Compression styles
# ---------------------------------------------------------------------------

def compress_api_style(docs_dir, sections):
    """Generate pipe-delimited API reference index.

    Format:
        [Docs Index]|root: ./docs
        |IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning
        |01-section:{file1.md,file2.md,file3.md}
        |02-section:{file4.md,file5.md}
    """
    root = Path(docs_dir)
    lines = [
        f"[Docs Index]|root: {root}",
        "|IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning",
    ]

    idx = 0
    for section_name, files in sections.items():
        filenames = [f.name for f in files]
        file_list = ",".join(filenames)
        if section_name == "_root":
            lines.append(f"|root:{{{file_list}}}")
        else:
            idx += 1
            lines.append(f"|{idx:02d}-{section_name}:{{{file_list}}}")

    return "\n".join(lines) + "\n"


def compress_prose_style(docs_dir, sections):
    """Generate summary + references style for prose guides.

    Each section gets a one-line summary extracted from the first file's
    content, followed by the file list.
    """
    root = Path(docs_dir)
    lines = [
        f"# Documentation Index",
        f"Root: {root}",
        "",
        "> Prefer retrieval-led reasoning over pre-training-led reasoning.",
        "",
    ]

    for section_name, files in sections.items():
        display = section_name if section_name != "_root" else "(root)"
        lines.append(f"## {display}")

        # Try to extract a summary from the first file
        first_file = files[0]
        try:
            text = first_file.read_text(encoding="utf-8", errors="replace")
            summary = _extract_first_paragraph(text)
            if summary:
                lines.append(f"  {summary}")
        except IOError:
            pass

        for f in files:
            rel = f.relative_to(root)
            lines.append(f"  - {rel}")
        lines.append("")

    return "\n".join(lines)


def compress_code_style(docs_dir, sections):
    """Generate signatures-only index for code example directories.

    Extracts function and class signatures from each code file.
    """
    root = Path(docs_dir)
    lines = [
        f"# Code Index",
        f"Root: {root}",
        "",
        "> Prefer retrieval-led reasoning over pre-training-led reasoning.",
        "",
    ]

    for section_name, files in sections.items():
        display = section_name if section_name != "_root" else "(root)"
        lines.append(f"## {display}")

        for f in files:
            rel = f.relative_to(root)
            if f.suffix.lower() in _CODE_EXTENSIONS:
                try:
                    text = f.read_text(encoding="utf-8", errors="replace")
                    sigs = _extract_code_signatures(text, f)
                    if sigs:
                        lines.append(f"  {rel}:")
                        for sig in sigs:
                            lines.append(f"    {sig}")
                    else:
                        lines.append(f"  {rel} (no extractable signatures)")
                except IOError:
                    lines.append(f"  {rel} (read error)")
            else:
                # For non-code files, just list them with heading if available
                try:
                    text = f.read_text(encoding="utf-8", errors="replace")
                    heading = _extract_heading(text)
                    label = f" -- {heading}" if heading else ""
                    lines.append(f"  {rel}{label}")
                except IOError:
                    lines.append(f"  {rel}")

        lines.append("")

    return "\n".join(lines)


STYLE_MAP = {
    "api": compress_api_style,
    "prose": compress_prose_style,
    "code": compress_code_style,
}


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_references(compressed_text, docs_dir):
    """Validate that file references in the compressed output actually exist.

    Args:
        compressed_text (str): The generated compressed index.
        docs_dir (str | Path): The documentation root directory.

    Returns:
        list[str]: List of missing file paths.
    """
    root = Path(docs_dir)
    missing = []

    # Extract filenames from pipe-delimited format: |section:{f1,f2,f3}
    for match in re.finditer(r"\{([^}]+)\}", compressed_text):
        filenames = [f.strip() for f in match.group(1).split(",")]
        for fname in filenames:
            # We don't know the exact subdirectory, so search for the file
            found = list(root.rglob(fname))
            if not found:
                missing.append(fname)

    # Extract paths from list format: - path/to/file.md
    for match in re.finditer(r"^\s+-\s+(.+\.(?:md|txt|rst|py|js|ts|sh))", compressed_text, re.MULTILINE):
        ref = match.group(1).strip()
        full_path = root / ref
        if not full_path.exists():
            missing.append(ref)

    return missing


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

def compute_stats(docs_dir, compressed_text, sections):
    """Compute token savings and other statistics.

    Returns:
        dict: Statistics including original/compressed token counts and
        percentage savings.
    """
    root = Path(docs_dir)
    original_tokens = 0
    original_chars = 0
    file_count = 0

    for file_list in sections.values():
        for f in file_list:
            try:
                text = f.read_text(encoding="utf-8", errors="replace")
                original_tokens += _estimate_tokens(text)
                original_chars += len(text)
                file_count += 1
            except IOError:
                pass

    compressed_tokens = _estimate_tokens(compressed_text)
    compressed_chars = len(compressed_text)

    saved_tokens = original_tokens - compressed_tokens
    pct = (saved_tokens / original_tokens * 100) if original_tokens > 0 else 0.0

    return {
        "files_scanned": file_count,
        "sections": len(sections),
        "original_tokens": original_tokens,
        "original_characters": original_chars,
        "compressed_tokens": compressed_tokens,
        "compressed_characters": compressed_chars,
        "tokens_saved": saved_tokens,
        "reduction_percent": round(pct, 1),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser():
    parser = argparse.ArgumentParser(
        description="Compress documentation directories into token-efficient agent indexes.",
        epilog=(
            "Styles:\n"
            "  api    Pipe-delimited section index (best for API references)\n"
            "  prose  Section summaries with file references (best for guides)\n"
            "  code   Function/class signatures only (best for code examples)\n"
            "\n"
            "Examples:\n"
            "  %(prog)s docs/\n"
            "  %(prog)s docs/ --output agents.md --style api\n"
            "  %(prog)s docs/ --style code --validate\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "docs_directory",
        help="Root directory containing documentation files to compress",
    )
    parser.add_argument(
        "--output", "-o",
        metavar="FILE",
        default=None,
        help="Write compressed output to FILE (default: stdout)",
    )
    parser.add_argument(
        "--style", "-s",
        choices=list(STYLE_MAP.keys()),
        default="api",
        help="Compression style (default: api)",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate that referenced files actually exist",
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Print token savings statistics",
    )
    return parser


def main():
    parser = _build_parser()
    args = parser.parse_args()

    docs_dir = Path(args.docs_directory)
    if not docs_dir.is_dir():
        print(f"Error: Not a directory: {docs_dir}", file=sys.stderr)
        sys.exit(1)

    # Scan
    sections = _scan_directory(docs_dir)
    if not sections:
        print(f"Warning: No documentation files found in {docs_dir}", file=sys.stderr)
        sys.exit(0)

    # Compress
    compress_fn = STYLE_MAP[args.style]
    compressed = compress_fn(docs_dir, sections)

    # Output
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(compressed, encoding="utf-8")
        print(f"Compressed index written to {output_path}")
    else:
        print(compressed)

    # Validation
    if args.validate:
        missing = validate_references(compressed, docs_dir)
        if missing:
            print(f"\nValidation: {len(missing)} missing reference(s):", file=sys.stderr)
            for m in missing:
                print(f"  - {m}", file=sys.stderr)
            sys.exit(1)
        else:
            print("\nValidation: All references resolved successfully.", file=sys.stderr)

    # Statistics
    if args.stats:
        stats = compute_stats(docs_dir, compressed, sections)
        print(f"\n--- Token Savings ---", file=sys.stderr)
        print(f"Files scanned:       {stats['files_scanned']}", file=sys.stderr)
        print(f"Sections:            {stats['sections']}", file=sys.stderr)
        print(f"Original tokens:     {stats['original_tokens']:,}", file=sys.stderr)
        print(f"Compressed tokens:   {stats['compressed_tokens']:,}", file=sys.stderr)
        print(f"Tokens saved:        {stats['tokens_saved']:,}", file=sys.stderr)
        print(f"Reduction:           {stats['reduction_percent']:.1f}%", file=sys.stderr)


if __name__ == "__main__":
    main()
