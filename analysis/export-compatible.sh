#!/bin/bash
# export-compatible.sh - 兼容export.py使用习惯的脚本
#
# 使用方法：
#   ./export-compatible.sh [输入目录] [输出文件]
#
# 示例：
#   ./export-compatible.sh ./src ./导出.docx
#   ./export-compatible.sh  # 使用默认值：./src -> ./导出.docx

set -e

# 默认参数
INPUT_DIR="${1:-./src}"
OUTPUT_FILE="${2:-导出.docx}"

# 显示使用信息
echo "=== Code Merger - export.py兼容模式 ==="
echo "输入目录: $INPUT_DIR"
echo "输出文件: $OUTPUT_FILE"
echo ""

# 检查输入目录
if [ ! -d "$INPUT_DIR" ]; then
    echo "错误: 输入目录 '$INPUT_DIR' 不存在"
    echo ""
    echo "使用方法："
    echo "  $0 [输入目录] [输出文件]"
    echo ""
    echo "示例："
    echo "  $0 ./src ./导出.docx"
    echo "  $0  # 使用默认值"
    exit 1
fi

# 使用main.py的简洁模式（最接近export.py风格）
echo "正在生成文档..."
uv run python main.py -i "$INPUT_DIR" -o "$OUTPUT_FILE" -v

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 文档生成完成: $OUTPUT_FILE"
else
    echo ""
    echo "❌ 文档生成失败"
    exit 1
fi