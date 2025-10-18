# Code Merger

将指定文件夹中的所有代码文件内容整合成为一个docx文档的工具。

## 功能特点

- 🚀 支持Java/Spring Boot项目文件
- 🎨 支持Vue.js/前端项目文件
- 📄 自动生成格式化的Word文档
- 🔍 自动识别文件类型和编程语言
- 🚫 智能过滤构建文件和依赖目录
- 📚 包含文件目录索引
- 🔄 **新增**: 文档追加功能，支持向现有文档添加内容
- 🔤 **新增**: 多编码支持（UTF-8、GB18030、CP936、Latin-1）
- 🧹 **新增**: 智能清理连续空行，优化文档长度
- 💪 **新增**: 更健壮的错误处理和文档损坏恢复

## 支持的文件类型

### Java/Spring Boot
- `.java` - Java源文件
- `.xml` - XML配置文件
- `.yml/.yaml` - YAML配置文件
- `.properties` - 属性配置文件

### Vue.js/前端
- `.js` - JavaScript文件
- `.ts` - TypeScript文件
- `.vue` - Vue单文件组件
- `.html` - HTML文件
- `.css/.scss` - 样式文件
- `.json` - JSON配置文件

### 其他
- `.md` - Markdown文档
- `.py` - Python文件
- `.go` - Go文件
- `.sql` - SQL脚本

## 安装

```bash
# 克隆项目
git clone <repository-url>
cd code-merger

# 使用uv安装依赖
uv sync

# 或者使用pip
pip install -r requirements.txt
```

## 使用方法

### 基本用法

```bash
# 扫描当前目录并生成文档
python main.py -i ./my-project

# 指定输出文件名
python main.py -i ./my-project -o my_code.docx

# 添加项目名称
python main.py -i ./my-project -o my_code.docx -n "My Spring Boot Project"
```

### 高级选项

```bash
# 显示详细输出
python main.py -i ./my-project -v

# 查看帮助
python main.py --help
```

## 命令行参数

- `-i, --input-dir`: 输入目录路径（必需）
- `-o, --output`: 输出docx文件路径（默认: code_document.docx）
- `-n, --project-name`: 项目名称（用于文档标题）
- `-a, --append`: 追加模式：向现有文档追加内容
- `-v, --verbose`: 显示详细输出

## 使用示例

### 示例1: Java Spring Boot项目
```bash
python main.py -i /path/to/spring-boot-app -n "用户管理系统" -o user_management.docx
```

### 示例2: Vue.js前端项目
```bash
python main.py -i /path/to/vue-app -n "管理后台前端" -o admin_frontend.docx
```

### 示例3: 全栈项目
```bash
python main.py -i /path/to/fullstack-app -n "电商平台" -o ecommerce_platform.docx
```

### 示例4: 追加内容到现有文档
```bash
# 第一次生成文档
python main.py -i /path/to/project-part1 -o combined.docx -n "项目第一部分"

# 向现有文档追加内容
python main.py -i /path/to/project-part2 -o combined.docx -a
```

## 智能过滤

工具会自动过滤以下文件和目录：

- **构建目录**: `node_modules`, `dist`, `build`, `target`
- **IDE目录**: `.git`, `.idea`, `.vscode`, `.settings`
- **缓存目录**: `__pycache__`, `.pytest_cache`
- **虚拟环境**: `.venv`, `venv`
- **系统文件**: `.DS_Store`, `Thumbs.db`
- **日志文件**: `*.log`, `*.tmp`

## 输出文档结构

生成的Word文档包含：

1. **封面页**: 项目标题、生成时间、文件统计
2. **目录**: 所有代码文件的索引
3. **代码内容**: 每个文件的完整内容，包含：
   - 文件路径和名称
   - 编程语言类型
   - 格式化的代码内容

## 注意事项

- 确保输入目录存在且有读取权限
- 输出文件如果已存在会被覆盖（追加模式除外）
- 大型项目可能需要一些时间来处理
- 文档格式针对代码阅读进行了优化
- **编码支持**: 自动处理多种编码格式，包括中文编码
- **追加模式**: 可以向现有文档追加内容，支持文档合并

## 开发

```bash
# 运行测试
python -m pytest tests/

# 代码格式化
black main.py

# 类型检查
mypy main.py
```

## 许可证

MIT License

## 从export.py中吸收的优点

本工具在与export.py对比后，吸收了以下优秀特性：

### 🔤 多编码支持
- 支持UTF-8、GB18030、CP936、Latin-1等多种编码
- 智能编码检测和降级处理
- 避免因编码问题导致的文件读取失败

### 🔄 文档追加功能
- 支持向现有Word文档追加内容
- 处理文档损坏情况的优雅降级
- 追加时间戳和分隔符，保持文档结构清晰

### 🧹 代码清理优化
- 智能合并连续空行，减少文档长度
- 使用正则表达式优化文本格式
- 保持代码可读性的同时优化显示效果

### 💪 增强的健壮性
- 完善的错误处理机制
- 文件读取失败时的优雅处理
- 文档保存错误的异常处理

## 测试

项目包含完整的测试用例和测试文档，位于 `test/` 文件夹：

```
test/
├── projects/          # 测试项目
│   ├── test-project/  # Java+Vue.js全栈项目
│   └── encoding-test/ # 编码测试项目
├── results/           # 生成的测试文档
└── scripts/           # 测试脚本
```

### 运行测试

```bash
# 基础功能测试
uv run python main.py -i test/projects/test-project -o test/results/test-output.docx -n "测试项目"

# 编码处理测试
uv run python main.py -i test/projects/encoding-test -o test/results/encoding-test.docx

# 使用测试脚本
bash test/scripts/merge.sh test/projects/test-project test/results/script-test.docx
```

详细测试说明请参考 `test/README.md`。

## 从export.py迁移

如果您之前使用export.py，可以通过以下方式使用main.py：

### 兼容性脚本
```bash
# 使用兼容性脚本（最接近export.py行为）
./export-compatible.sh ./src ./导出.docx

# 或者直接使用main.py的简洁模式
uv run python main.py -i ./src -o ./导出.docx -v
```

### 主要改进
- ✅ 支持更多文件类型（14种 vs 2种）
- ✅ 命令行参数化（更灵活）
- ✅ 智能目录过滤（自动排除node_modules等）
- ✅ 中文界面（更友好）
- ✅ 完善的错误处理
- ✅ 文档追加功能
- ✅ 多编码支持

## 贡献

欢迎提交Issue和Pull Request！

## 更新日志

### v2.0 (当前版本)
- 🔥 完全吸收export.py的所有功能
- 🎯 新增文档追加功能
- 🔤 增强多编码支持
- 🧹 优化代码清理功能
- 💪 完善错误处理机制
- 🚀 删除export.py，专注于main.py