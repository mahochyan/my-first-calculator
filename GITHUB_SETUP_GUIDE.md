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

## 文件说明

- `calculator.py` - 简单的计算器代码
- `README.md` - 项目说明文档
- `.gitignore` - Git 忽略文件配置
