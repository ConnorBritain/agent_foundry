#!/usr/bin/env python3
"""
SKILL.md validator for Sforza.

Validates SKILL.md files against the agentskills.io specification, checking:
  - YAML frontmatter structure (between ``---`` markers)
  - Required fields: ``name``, ``description``
  - Name format: lowercase, hyphens and digits only, max 64 characters
  - Description length: max 1024 characters
  - Referenced files exist (``references/`` and ``scripts/`` directories)
  - No deeply nested references (max 2 levels)
  - Token budget warning if estimated tokens exceed 5 000

Usage:
    python skill-validator.py <path-to-SKILL.md>
    python skill-validator.py --all <skills-directory>

Examples:
    python skill-validator.py common/skills/code-review/SKILL.md
    python skill-validator.py --all common/skills/
"""

import argparse
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

NAME_REGEX = re.compile(r"^[a-z0-9][a-z0-9-]*$")
NAME_MAX_LENGTH = 64
DESCRIPTION_MAX_LENGTH = 1024
TOKEN_BUDGET_WARN = 5000
MAX_REFERENCE_DEPTH = 2

# Simple token heuristic (same as token-calculator fallback)
_TOKEN_MULTIPLIER = 1.3


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _estimate_tokens(text):
    """Estimate token count using word-based heuristic."""
    return max(1, int(len(text.split()) * _TOKEN_MULTIPLIER))


def _parse_frontmatter(text):
    """Extract YAML frontmatter from a SKILL.md file.

    The frontmatter is the block between the first pair of ``---`` lines.

    Returns:
        tuple: (dict of parsed key-value pairs, list of error strings).
               The parser handles simple ``key: value`` lines and does NOT
               require PyYAML.
    """
    errors = []
    lines = text.split("\n")

    # Find the opening ---
    if not lines or lines[0].strip() != "---":
        errors.append("Missing opening '---' for YAML frontmatter")
        return {}, errors

    # Find the closing ---
    closing_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            closing_idx = i
            break

    if closing_idx is None:
        errors.append("Missing closing '---' for YAML frontmatter")
        return {}, errors

    # Parse simple key: value pairs (no nested YAML support needed)
    frontmatter = {}
    current_key = None
    current_value_lines = []

    for line in lines[1:closing_idx]:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # Check for a new key
        match = re.match(r"^([a-z_][a-z0-9_-]*):\s*(.*)", line, re.IGNORECASE)
        if match:
            # Save previous key if any
            if current_key is not None:
                frontmatter[current_key] = "\n".join(current_value_lines).strip()
            current_key = match.group(1).lower()
            current_value_lines = [match.group(2).strip()]
        elif current_key is not None:
            # Continuation line for a multiline value
            current_value_lines.append(stripped)

    # Save final key
    if current_key is not None:
        frontmatter[current_key] = "\n".join(current_value_lines).strip()

    return frontmatter, errors


def _find_file_references(text):
    """Find all file references in the SKILL.md body.

    Looks for references to files in ``references/`` and ``scripts/``
    directories, expressed as markdown links, inline code, or plain paths.

    Returns:
        list[str]: Extracted relative file paths.
    """
    refs = set()

    # Patterns like: references/foo.md, scripts/bar.py, ./references/...
    pattern = re.compile(r"(?:\./)?((?:references|scripts)/[^\s\)\]\"'`,]+)")
    for match in pattern.finditer(text):
        ref = match.group(1).rstrip(".")
        refs.add(ref)

    return sorted(refs)


def _check_reference_depth(ref_path):
    """Check that a reference path does not exceed MAX_REFERENCE_DEPTH.

    Depth is counted as the number of directory levels below the top-level
    reference directory (``references/`` or ``scripts/``).

    Returns:
        bool: True if within allowed depth.
    """
    parts = Path(ref_path).parts
    # First part is "references" or "scripts", remaining are depth
    depth = len(parts) - 1  # subtract the top-level dir itself
    return depth <= MAX_REFERENCE_DEPTH


# ---------------------------------------------------------------------------
# Core validator
# ---------------------------------------------------------------------------

class ValidationResult:
    """Accumulator for validation findings."""

    def __init__(self, file_path):
        self.file_path = str(file_path)
        self.errors = []
        self.warnings = []

    def error(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    @property
    def is_valid(self):
        return len(self.errors) == 0

    def summary(self):
        status = "PASS" if self.is_valid else "FAIL"
        parts = [f"[{status}] {self.file_path}"]
        for e in self.errors:
            parts.append(f"  ERROR:   {e}")
        for w in self.warnings:
            parts.append(f"  WARNING: {w}")
        if self.is_valid and not self.warnings:
            parts.append("  All checks passed.")
        return "\n".join(parts)


def validate_skill(skill_path):
    """Validate a single SKILL.md file.

    Args:
        skill_path (str | Path): Path to the SKILL.md file.

    Returns:
        ValidationResult: The accumulated errors and warnings.
    """
    skill_path = Path(skill_path)
    result = ValidationResult(skill_path)

    # --- File existence ---
    if not skill_path.exists():
        result.error(f"File does not exist: {skill_path}")
        return result

    if not skill_path.is_file():
        result.error(f"Not a file: {skill_path}")
        return result

    text = skill_path.read_text(encoding="utf-8", errors="replace")

    # --- Frontmatter parsing ---
    frontmatter, parse_errors = _parse_frontmatter(text)
    for err in parse_errors:
        result.error(err)

    if not frontmatter and not parse_errors:
        result.error("Frontmatter is empty (no key-value pairs found)")

    # --- Required field: name ---
    name = frontmatter.get("name")
    if not name:
        result.error("Required field 'name' is missing from frontmatter")
    else:
        # Strip quotes if present
        name = name.strip("\"'")
        if len(name) > NAME_MAX_LENGTH:
            result.error(
                f"Name exceeds {NAME_MAX_LENGTH} characters (got {len(name)}): '{name}'"
            )
        if not NAME_REGEX.match(name):
            result.error(
                f"Name must be lowercase alphanumeric with hyphens, "
                f"matching {NAME_REGEX.pattern}. Got: '{name}'"
            )

    # --- Required field: description ---
    description = frontmatter.get("description")
    if not description:
        result.error("Required field 'description' is missing from frontmatter")
    else:
        description = description.strip("\"'")
        if len(description) > DESCRIPTION_MAX_LENGTH:
            result.error(
                f"Description exceeds {DESCRIPTION_MAX_LENGTH} characters "
                f"(got {len(description)})"
            )

    # --- File references ---
    skill_dir = skill_path.parent
    refs = _find_file_references(text)

    for ref in refs:
        ref_full = skill_dir / ref
        if not ref_full.exists():
            result.error(f"Referenced file does not exist: {ref} (resolved: {ref_full})")

        if not _check_reference_depth(ref):
            result.error(
                f"Reference too deeply nested (max {MAX_REFERENCE_DEPTH} levels): {ref}"
            )

    # --- Token budget ---
    estimated_tokens = _estimate_tokens(text)
    if estimated_tokens > TOKEN_BUDGET_WARN:
        result.warn(
            f"Estimated token count ({estimated_tokens:,}) exceeds recommended "
            f"budget of {TOKEN_BUDGET_WARN:,}. Consider compressing or splitting."
        )

    # --- Optional field checks (non-fatal) ---
    if "version" not in frontmatter:
        result.warn("Optional field 'version' is not set in frontmatter")
    if "author" not in frontmatter:
        result.warn("Optional field 'author' is not set in frontmatter")

    return result


def validate_directory(skills_dir):
    """Validate all SKILL.md files found under *skills_dir*.

    Recursively searches for files named ``SKILL.md`` (case-sensitive).

    Args:
        skills_dir (str | Path): Root directory to search.

    Returns:
        list[ValidationResult]: One result per SKILL.md file found.
    """
    skills_dir = Path(skills_dir)
    if not skills_dir.is_dir():
        r = ValidationResult(skills_dir)
        r.error(f"Not a directory: {skills_dir}")
        return [r]

    results = []
    for skill_file in sorted(skills_dir.rglob("SKILL.md")):
        results.append(validate_skill(skill_file))

    if not results:
        r = ValidationResult(skills_dir)
        r.warn("No SKILL.md files found in directory")
        results.append(r)

    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser():
    parser = argparse.ArgumentParser(
        description="Validate SKILL.md files against the agentskills.io specification.",
        epilog=(
            "Validation checks:\n"
            "  - YAML frontmatter presence and structure\n"
            "  - Required fields: name, description\n"
            "  - Name format: ^[a-z0-9][a-z0-9-]*$ (max 64 chars)\n"
            "  - Description length (max 1024 chars)\n"
            "  - Referenced files in references/ and scripts/ exist\n"
            "  - Reference nesting depth (max 2 levels)\n"
            "  - Token budget (warn if > 5000 estimated tokens)\n"
            "\n"
            "Examples:\n"
            "  %(prog)s common/skills/code-review/SKILL.md\n"
            "  %(prog)s --all common/skills/\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "skill_file",
        nargs="?",
        default=None,
        help="Path to a single SKILL.md file to validate",
    )
    group.add_argument(
        "--all",
        metavar="SKILLS_DIR",
        dest="skills_dir",
        help="Validate all SKILL.md files under the given directory",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON instead of human-readable text",
    )

    return parser


def main():
    parser = _build_parser()
    args = parser.parse_args()

    if args.skills_dir:
        results = validate_directory(args.skills_dir)
    elif args.skill_file:
        results = [validate_skill(args.skill_file)]
    else:
        parser.print_help()
        sys.exit(1)

    if args.json:
        output = []
        for r in results:
            output.append({
                "file": r.file_path,
                "valid": r.is_valid,
                "errors": r.errors,
                "warnings": r.warnings,
            })
        print(json.dumps(output, indent=2))
    else:
        total_errors = 0
        total_warnings = 0
        for r in results:
            print(r.summary())
            print()
            total_errors += len(r.errors)
            total_warnings += len(r.warnings)

        # Summary line
        file_count = len(results)
        passed = sum(1 for r in results if r.is_valid)
        failed = file_count - passed
        print(
            f"Validated {file_count} file(s): "
            f"{passed} passed, {failed} failed, "
            f"{total_errors} error(s), {total_warnings} warning(s)"
        )

    # Exit with non-zero if any file failed
    if any(not r.is_valid for r in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
