# GitHub 设置指南

## 步骤 1：安装 Git

访问 https://git-scm.com/download/win 下载并安装 Git for Windows

## 步骤 2：在 GitHub 上创建代码库

1. 访问 https://github.com/new
2. 填写信息：
   - Repository name: `my-first-calculator`
   - Description: `My first Python calculator project`
   - 选择 Public
   - 勾选 "Add a README file"
3. 点击 "Create repository"

## 步骤 3：在本地初始化并推送

打开 PowerShell 或 CMD，进入项目目录，执行以下命令：

```bash
cd my-first-calculator

git init
git config user.name "mahochyan"
git config user.email "your-email@example.com"
git add .
git commit -m "Initial commit: Add simple calculator"
git branch -M main
git remote add origin https://github.com/mahochyan/my-first-calculator.git
git push -u origin main
```

## 步骤 4：验证

访问 https://github.com/mahochyan/my-first-calculator 查看你的代码库

## 步骤 5：日常更新代码到 GitHub

每次修改文件后，需要手动推送到 GitHub（**不会自动同步**）：

### 5.1 查看修改状态
```bash
git status
```
显示哪些文件被修改或新增

### 5.2 添加修改的文件
```bash
git add .
```
- `git add .` - 添加所有修改
- `git add 文件名` - 只添加指定文件

### 5.3 提交修改
```bash
git commit -m "描述你的修改"
```
例如：`git commit -m "Fix calculator division bug"`

### 5.4 推送到 GitHub
```bash
git push origin main
```
将本地提交推送到远程仓库

### 完整示例
```bash
# 修改了 calculator.py 后 (假设文件在 tutorial/04_functions/ 目录下)
git add tutorial/04_functions/calculator.py
git commit -m "Add modulo operation"
git push origin main
```

## 步骤 6：处理合并冲突

如果推送时出现冲突（远程有你没有的更改）：

```bash
# 先拉取远程更改
git pull origin main --allow-unrelated-histories

# 手动解决冲突（编辑冲突文件）
# 然后提交
git add .
git commit -m "Merge remote changes"
git push origin main
```

## 文件说明

- `tutorial/` - 包含所有分阶段学习代码的目录 (如 `calculator.py`)
- `README.md` - 项目说明文档
- `.gitignore` - Git 忽略文件配置
