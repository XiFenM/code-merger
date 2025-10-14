#!/bin/bash
# Code Merger 脚本 - 简化使用

if [ $# -eq 0 ]; then
    echo "用法: $0 <输入目录> [输出文件名] [项目名称]"
    echo ""
    echo "参数:"
    echo "  输入目录    必需，要扫描的项目目录路径"
    echo "  输出文件名  可选，默认为 code_document.docx"
    echo "  项目名称    可选，用于文档标题"
    echo ""
    echo "示例:"
    echo "  $0 /path/to/spring-boot-app"
    echo "  $0 /path/to/vue-app my_project.docx"
    echo "  $0 /path/to/project output.docx \"My Project\""
    exit 1
fi

INPUT_DIR="$1"
OUTPUT_FILE="${2:-code_document.docx}"
PROJECT_NAME="$3"

# 检查输入目录是否存在
if [ ! -d "$INPUT_DIR" ]; then
    echo "错误: 目录 '$INPUT_DIR' 不存在"
    exit 1
fi

# 构建命令
CMD="uv run python main.py -i \"$INPUT_DIR\" -o \"$OUTPUT_FILE\""

if [ -n "$PROJECT_NAME" ]; then
    CMD="$CMD -n \"$PROJECT_NAME\""
fi

echo "正在执行: $CMD"
echo ""

# 执行命令
eval $CMD

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 文档生成成功: $OUTPUT_FILE"
else
    echo ""
    echo "❌ 文档生成失败"
    exit 1
fi