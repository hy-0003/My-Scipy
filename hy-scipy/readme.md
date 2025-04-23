# *hy-scipy*

🌟 项目简介
hy-scipy 是一个基于 Python 的科学计算库，灵感来源于 SciPy，旨在为科研和工程计算提供高效、易用的工具集。目前聚焦于数值计算、线性代数、信号处理等基础模块，未来计划逐步扩展更多科学计算功能。
🚀 核心特性
轻量级架构：基于 NumPy 构建，保持与 NumPy 数组的无缝兼容。
基础数值算法：提供矩阵运算、快速傅里叶变换（FFT）、插值等常用算法。
跨平台支持：支持 Linux、macOS 和 Windows 系统，可通过 Docker 快速部署。
模块化设计：方便扩展新功能，欢迎社区贡献代码！
📦 安装指南
1. 通过 PyPI 安装（推荐）
bash
pip install hy-scipy

📚 使用示例
1. 导入库与基础数组操作
python
import numpy as np
import hy-scipy as *

🛠️ 开发与贡献
1. 环境配置
推荐使用 Conda 管理开发环境：
bash
conda create -n hy-scipy-dev python=3.11.11
conda activate hy-scipy-dev
pip install -e .[dev]  # 安装开发依赖（如 pytest, flake8）

🤝 联系与反馈
问题反馈：提交 GitHub Issue
邮箱：2981130749@qq.com
让我们一起打造更强大的科学计算工具！ 🚀