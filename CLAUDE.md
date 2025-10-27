# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Code Merger is a Python tool that consolidates code files from specified directories into formatted Word documents (.docx). It supports Java/Spring Boot and Vue.js projects, along with 14+ file types including archives (ZIP, TAR, RAR).

## Essential Commands

### Development Setup
```bash
# Install dependencies using UV (preferred)
uv sync

# Or using pip
pip install -r requirements.txt
```

### Running the Tool
```bash
# Basic usage
uv run python main.py -i ./input-directory -o output.docx

# With project name
uv run python main.py -i ./project -n "Project Name" -o output.docx

# Append to existing document
uv run python main.py -i ./additional-code -o existing.docx -a

# Verbose mode
uv run python main.py -i ./project -v
```

### Testing
```bash
# Test with sample project
uv run python main.py -i test/projects/test-project -o test/results/test-output.docx -n "Test Project"

# Run test script
bash test/scripts/merge.sh test/projects/test-project test/results/script-test.docx
```

### Code Quality
```bash
# Format code
black main.py

# Type checking
mypy main.py
```

## Architecture Overview

### Core Components

**main.py** - Single-file application (457 lines) containing:
- `CodeMerger` class: Main orchestration logic
- `read_text_file_with_encoding()`: Multi-encoding file reader
- `clean_code_content()`: Code optimization and cleanup
- `append_to_document()`: Document append functionality
- Archive processing for ZIP/TAR/RAR files
- Command-line interface using Click framework

### Key Design Patterns

1. **Encoding Strategy**: Tries multiple encodings (UTF-8, GB18030, CP936, Latin-1) with graceful fallback
2. **Document Structure**: Creates professional Word docs with cover page, table of contents, and formatted code sections
3. **Smart Filtering**: Automatically excludes build directories, IDE files, and system files
4. **Error Handling**: Comprehensive exception management with graceful degradation

### Supported File Types

**Java/Spring Boot**: .java, .xml, .yml/.yaml, .properties
**Vue.js/Frontend**: .js/.jsx, .ts/.tsx, .vue, .html, .css/.scss, .json
**Other**: .md, .py, .go, .sql, .sh

### Archive Support

Direct processing of ZIP, TAR, and RAR archives with automatic extraction to temporary directories.

## Important Notes

- **Chinese Language**: Full Chinese interface and documentation - maintain Chinese language support
- **Legacy Migration**: Project evolved from export.py - see analysis/ folder for migration details
- **Testing Infrastructure**: Complete test projects and scripts in test/ directory
- **Document Append**: Unique feature allowing content addition to existing Word documents
- **Encoding Robustness**: Critical for handling various code file encodings, especially Chinese text

## Common Development Tasks

When modifying file type support, update:
1. `SUPPORTED_EXTENSIONS` dictionary in main.py
2. Language detection logic in `get_language_type()`
3. Test with appropriate sample files in test/projects/

When adding new features, ensure:
1. Command-line arguments are added using Click decorators
2. Error handling includes graceful degradation
3. Chinese language support is maintained
4. Tests are added to test/ directory