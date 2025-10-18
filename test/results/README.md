# 测试结果文档说明

本文件夹包含了所有测试生成的Word文档，用于验证Code Merger工具的各项功能。

## 文档列表及说明

### 📋 基础测试文档

| 文件名 | 大小 | 生成命令 | 功能验证 |
|--------|------|----------|----------|
| `test-output.docx` | ~39KB | `python main.py -i test-project -o test-output.docx -n "测试项目"` | 基础功能测试 |
| `script-test.docx` | ~39KB | `./merge.sh test-project script-test.docx "脚本测试项目"` | 便捷脚本测试 |

### 🔧 改进功能测试文档

| 文件名 | 大小 | 生成命令 | 功能验证 |
|--------|------|----------|----------|
| `final-improved.docx` | ~39KB | `python main.py -i test-project -o final-improved.docx -n "最终改进版本" -v` | 完整改进功能 |
| `encoding-test.docx` | ~37KB | `python main.py -i encoding-test -o encoding-test.docx -s -v` | 多编码支持测试 |

### 🔄 追加模式测试文档

| 文件名 | 大小 | 生成命令 | 功能验证 |
|--------|------|----------|----------|
| `append-final.docx` | ~39KB | `python main.py -i test-project -o append-final.docx -a -v` | 追加模式测试 |
| `append-test.docx` | ~40KB | `python main.py -i test-project -o append-test.docx -a -s -v` | 简单模式追加测试 |

### 🎯 其他测试文档

| 文件名 | 大小 | 生成命令 | 功能验证 |
|--------|------|----------|----------|
| `improved-test.docx` | ~39KB | 中间版本测试 | 改进版本中间测试 |
| `simple-test.docx` | ~39KB | `python main.py -i test-project -o simple-test.docx -s -v` | 简单模式测试 |

## 📊 文档内容结构验证

### 完整模式文档结构
1. **封面页**
   - 项目标题
   - 生成时间
   - 文件总数统计
   - 语言类型统计

2. **目录页**
   - 所有文件索引
   - 文件路径和语言类型
   - 编码信息（如果检测到）

3. **代码内容页**
   - 文件标题和路径
   - 语言类型和编码信息
   - 格式化的代码内容（Consolas字体，10pt）
   - 分隔线

### 简单模式文档结构
1. **时间戳**
   - 导出时间或追加时间

2. **代码内容**
   - 文件名（粗体，12pt）
   - 代码内容（Consolas字体，10pt）
   - 分隔线（80字符宽度）

### 追加模式特性
- 保留原有内容
- 添加分页符
- 显示追加时间和文件数
- 使用分隔符区分不同批次的内容

## ✅ 质量检查清单

每个文档都应该通过以下检查：

- [ ] 文档可以正常打开，无损坏
- [ ] 所有预期的代码文件都包含在内
- [ ] 代码格式正确，使用等宽字体
- [ ] 文件路径显示正确
- [ ] 语言类型识别准确
- [ ] 中文内容正确显示（特别是encoding-test.docx）
- [ ] 追加模式文档包含多次追加的内容
- [ ] 文档属性信息完整

## 🔍 问题排查

如果发现文档有问题，可以：

1. **检查文件完整性**
   ```bash
   file test/results/*.docx
   ```

2. **重新生成特定文档**
   ```bash
   cd /root/workspace/code-merger
   uv run python main.py -i test/projects/test-project -o test/results/new-test.docx -v
   ```

3. **验证项目文件**
   ```bash
   ls -la test/projects/
   ```

## 📈 性能参考

- 处理4个文件的测试项目约需1-2秒
- 生成的文档大小通常在35-45KB范围内
- 追加模式会略微增加文档大小
- 编码检测会增加少量处理时间

## 🎯 测试建议

1. **新增测试项目**：可以在 `test/projects/` 下添加新的测试项目
2. **功能测试**：针对新功能创建对应的测试用例
3. **边界测试**：测试空项目、大文件、特殊字符等情况
4. **性能测试**：测试包含大量文件的项目处理性能

所有测试文档都是功能验证的重要参考，建议保留用于对比和回归测试。如需清理，请参考主README.md中的清理说明。,