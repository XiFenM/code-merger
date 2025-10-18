# 测试文件夹说明

本文件夹包含了Code Merger工具的所有测试用例和测试结果。

## 文件夹结构

```
test/
├── projects/          # 测试项目
│   ├── test-project/  # 主要的Java+Vue.js测试项目
│   └── encoding-test/ # 编码测试项目
├── results/           # 生成的文档结果
│   ├── *.docx        # 各种测试生成的Word文档
│   └── README.md     # 结果说明文档
└── scripts/           # 测试脚本
    └── merge.sh      # 便捷使用脚本
```

## 测试项目说明

### 1. test-project
模拟了一个完整的Spring Boot + Vue.js全栈项目，包含：

**Java后端部分：**
- `src/main/java/com/example/UserController.java` - RESTful用户控制器
- `src/main/resources/application.yml` - Spring Boot配置文件

**Vue.js前端部分：**
- `frontend/src/components/UserList.vue` - 用户列表组件
- `frontend/src/views/Home.vue` - 主页视图组件

### 2. encoding-test
专门用于测试编码处理的项目：
- `Test.java` - 包含中文字符的Java文件

## 测试结果说明

### 基础测试文档

1. **test-output.docx** - 基础功能测试
   - 命令：`python main.py -i test-project -o test-output.docx -n "测试项目" -v`
   - 说明：验证基本功能是否正常

2. **script-test.docx** - 脚本测试
   - 命令：`./merge.sh test-project script-test.docx "脚本测试项目"`
   - 说明：验证便捷脚本功能

### 改进功能测试文档

3. **final-improved.docx** - 最终改进版本测试
   - 命令：`python main.py -i test-project -o final-improved.docx -n "最终改进版本" -v`
   - 说明：验证所有改进功能

4. **encoding-test.docx** - 编码处理测试
   - 命令：`python main.py -i encoding-test -o encoding-test.docx -s -v`
   - 说明：验证多编码支持功能

### 追加模式测试文档

5. **append-final.docx** - 追加功能测试
   - 命令：`python main.py -i test-project -o append-final.docx -a -v`
   - 说明：验证文档追加功能

6. **append-test.docx** - 追加功能测试（简单模式）
   - 命令：`python main.py -i test-project -o append-test.docx -a -s -v`
   - 说明：验证追加功能的简单模式

### 其他测试文档

7. **improved-test.docx** - 改进版本测试
   - 说明：中间版本的测试结果

8. **simple-test.docx** - 简单模式测试
   - 命令：`python main.py -i test-project -o simple-test.docx -s -v`
   - 说明：验证简单模式功能

## 测试命令汇总

### 基础测试
```bash
# 基本功能测试
uv run python main.py -i test/projects/test-project -o test/results/test-output.docx -n "测试项目" -v

# 脚本测试
bash test/scripts/merge.sh test/projects/test-project test/results/script-test.docx "脚本测试项目"
```

### 改进功能测试
```bash
# 编码处理测试
uv run python main.py -i test/projects/encoding-test -o test/results/encoding-test.docx -s -v

# 追加模式测试
uv run python main.py -i test/projects/test-project -o test/results/append-test.docx -a -s -v
```

### 各种模式测试
```bash
# 完整模式
uv run python main.py -i test/projects/test-project -o test/results/full-mode.docx -n "完整模式测试" -v

# 简单模式
uv run python main.py -i test/projects/test-project -o test/results/simple-mode.docx -s -v

# 追加模式
uv run python main.py -i test/projects/test-project -o test/results/append-mode.docx -a -v
```

## 测试结果验证

所有测试文档应该：
1. ✅ 正常打开，无损坏
2. ✅ 包含预期的代码文件内容
3. ✅ 格式正确，代码使用等宽字体
4. ✅ 中文内容正确显示（编码测试）
5. ✅ 追加模式文档包含多次追加的内容

## 清理测试文件

如果需要重新测试，可以清理结果文件：
```bash
cd test/results
rm -f *.docx
```

然后重新运行测试命令。