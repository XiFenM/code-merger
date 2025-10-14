# Code Merger

将指定文件夹中的所有代码文件内容整合成为一个docx文档的工具。

## 功能特点

- 🚀 支持Java/Spring Boot项目文件
- 🎨 支持Vue.js/前端项目文件
- 📄 自动生成格式化的Word文档
- 🔍 自动识别文件类型和编程语言
- 🚫 智能过滤构建文件和依赖目录
- 📚 包含文件目录索引

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
- 输出文件如果已存在会被覆盖
- 大型项目可能需要一些时间来处理
- 文档格式针对代码阅读进行了优化

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

## 贡献

欢迎提交Issue和Pull Request！