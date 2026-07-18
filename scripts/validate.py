#!/usr/bin/env python3
"""
Lec.Course schema 校验脚本。

用法:
    python scripts/validate.py <schema_path> <artifact_path>

示例:
    python scripts/validate.py schemas/requirements.schema.json output/requirements.md.json
    python scripts/validate.py schemas/learning-plan.schema.json output/learning-plan.json
    python scripts/validate.py schemas/qa-report.schema.json output/qa-report.json

规则: 校验失败时 exit 1,通过时 exit 0。
每个 skill 的 SKILL.md 入口应调用此脚本校验产出。
"""

import sys
import json
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("缺少依赖: pip install jsonschema", file=sys.stderr)
    sys.exit(2)


def load_json(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        print(f"文件不存在: {path}", file=sys.stderr)
        sys.exit(2)
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    if len(sys.argv) != 3:
        print(f"用法: {sys.argv[0]} <schema_path> <artifact_path>", file=sys.stderr)
        sys.exit(2)

    schema_path, artifact_path = sys.argv[1], sys.argv[2]
    schema = load_json(schema_path)
    artifact = load_json(artifact_path)

    try:
        jsonschema.validate(instance=artifact, schema=schema)
    except jsonschema.ValidationError as e:
        print("❌ schema 校验失败:", file=sys.stderr)
        print(f"   路径: {e.json_path}", file=sys.stderr)
        print(f"   错误: {e.message}", file=sys.stderr)
        print(f"   违反schema: {list(e.schema_path)}", file=sys.stderr)
        sys.exit(1)

    print("✅ schema 校验通过")


if __name__ == "__main__":
    main()
