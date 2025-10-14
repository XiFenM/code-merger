#!/usr/bin/env python3
"""
Code Merger - 将指定文件夹中的代码文件整合成docx文档
支持Java/Spring Boot和Vue.js项目
"""

import os
import sys
from pathlib import Path
from typing import List, Dict
import click
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH


class CodeFile:
    """代码文件类"""

    def __init__(self, file_path: Path, relative_path: str):
        self.file_path = file_path
        self.relative_path = relative_path
        self.content = ""
        self.language = self._detect_language()

    def _detect_language(self) -> str:
        """检测编程语言"""
        ext = self.file_path.suffix.lower()
        language_map = {
            '.java': 'Java',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.vue': 'Vue',
            '.html': 'HTML',
            '.css': 'CSS',
            '.scss': 'SCSS',
            '.xml': 'XML',
            '.yml': 'YAML',
            '.yaml': 'YAML',
            '.properties': 'Properties',
            '.json': 'JSON',
            '.md': 'Markdown',
            '.py': 'Python',
            '.go': 'Go',
            '.sql': 'SQL'
        }
        return language_map.get(ext, 'Text')

    def read_content(self) -> bool:
        """读取文件内容"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
            return True
        except (UnicodeDecodeError, PermissionError) as e:
            print(f"警告: 无法读取文件 {self.file_path}: {e}")
            return False


class CodeMerger:
    """代码合并器"""

    def __init__(self):
        self.code_files: List[CodeFile] = []
        self.supported_extensions = {
            # Java/Spring Boot
            '.java', '.xml', '.yml', '.yaml', '.properties',
            # Vue.js/前端
            '.js', '.ts', '.vue', '.html', '.css', '.scss', '.json',
            # 其他常见文件
            '.md', '.py', '.go', '.sql'
        }
        self.ignore_patterns = {
            'node_modules', 'dist', 'build', 'target', '.git', '.idea',
            '.vscode', '__pycache__', '.pytest_cache', '.venv', 'venv',
            '.classpath', '.project', '.settings'
        }
        self.ignore_files = {
            '.gitignore', '.DS_Store', 'Thumbs.db', '*.log', '*.tmp'
        }

    def scan_directory(self, directory: Path) -> None:
        """扫描目录中的代码文件"""
        print(f"正在扫描目录: {directory}")

        for root, dirs, files in os.walk(directory):
            # 过滤掉需要忽略的目录
            dirs[:] = [d for d in dirs if d not in self.ignore_patterns]

            for file in files:
                file_path = Path(root) / file

                # 检查文件扩展名
                if file_path.suffix.lower() not in self.supported_extensions:
                    continue

                # 检查是否需要忽略的文件
                if any(file.startswith(pattern.replace('*', '')) or file == pattern
                       for pattern in self.ignore_files):
                    continue

                # 计算相对路径
                try:
                    relative_path = str(file_path.relative_to(directory))
                except ValueError:
                    relative_path = str(file_path)

                code_file = CodeFile(file_path, relative_path)
                if code_file.read_content():
                    self.code_files.append(code_file)

        print(f"找到 {len(self.code_files)} 个代码文件")

    def create_document(self, output_path: Path, project_name: str = "") -> None:
        """创建docx文档"""
        print(f"正在生成文档: {output_path}")

        doc = Document()

        # 设置文档标题
        title = f"代码文档 - {project_name}" if project_name else "代码文档"
        doc.add_heading(title, 0)

        # 添加项目信息
        doc.add_paragraph(f"生成时间: {self._get_current_time()}")
        doc.add_paragraph(f"文件总数: {len(self.code_files)}")
        doc.add_page_break()

        # 添加目录
        doc.add_heading("目录", 1)
        for i, code_file in enumerate(self.code_files, 1):
            p = doc.add_paragraph()
            p.add_run(f"{i}. {code_file.relative_path} ({code_file.language})")
        doc.add_page_break()

        # 添加每个文件的内容
        for i, code_file in enumerate(self.code_files, 1):
            # 文件标题
            doc.add_heading(f"{i}. {code_file.relative_path}", 1)
            doc.add_paragraph(f"语言: {code_file.language}")
            doc.add_paragraph(f"文件路径: {code_file.relative_path}")

            # 文件内容
            doc.add_heading("代码内容", 2)

            # 创建代码样式段落
            p = doc.add_paragraph()
            p.style.font.name = 'Consolas'
            p.style.font.size = Pt(9)

            # 添加代码内容（保持原始格式）
            p.add_run(code_file.content)

            doc.add_page_break()

        # 保存文档
        doc.save(output_path)
        print(f"文档已保存: {output_path}")

    def _get_current_time(self) -> str:
        """获取当前时间"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@click.command()
@click.option('--input-dir', '-i',
              type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
              required=True,
              help='输入目录路径')
@click.option('--output', '-o',
              type=click.Path(path_type=Path),
              default='code_document.docx',
              help='输出docx文件路径 (默认: code_document.docx)')
@click.option('--project-name', '-n',
              default='',
              help='项目名称 (用于文档标题)')
@click.option('--verbose', '-v',
              is_flag=True,
              help='显示详细输出')
def main(input_dir: Path, output: Path, project_name: str, verbose: bool):
    """
    代码文件合并工具 - 将指定文件夹中的代码文件整合成docx文档

    支持Java/Spring Boot和Vue.js项目，自动识别文件类型并保持代码格式。
    """
    if verbose:
        print(f"输入目录: {input_dir}")
        print(f"输出文件: {output}")
        if project_name:
            print(f"项目名称: {project_name}")

    try:
        merger = CodeMerger()
        merger.scan_directory(input_dir)

        if not merger.code_files:
            print("警告: 未找到任何支持的代码文件")
            return

        merger.create_document(output, project_name)
        print(f"✅ 文档生成完成: {output}")

    except Exception as e:
        print(f"❌ 错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()