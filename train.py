#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
花卉分类训练脚本
简化版本，小白友好
"""

import os
import sys

def main():
    """主训练函数"""
    
    # 配置参数
    config_file = './flower_config.yaml'
    paddleclas_dir = './PaddleClas'
    
    # 检查必要文件是否存在
    if not os.path.exists(config_file):
        print(f"❌ 错误：找不到配置文件 {config_file}")
        print("请确保你在项目根目录运行此脚本")
        sys.exit(1)
    
    if not os.path.exists(paddleclas_dir):
        print(f"❌ 错误：找不到 PaddleClas 目录")
        print("请先克隆 PaddleClas 仓库：")
        print("  git clone https://github.com/PaddlePaddle/PaddleClas.git")
        sys.exit(1)
    
    # 检查数据集是否存在
    if not os.path.exists('./dataset/train'):
        print("⚠️  警告：找不到训练数据集目录")
        print("请创建数据集目录结构：")
        print("  mkdir -p dataset/train/{rose,sunflower,tulip}")
        print("  mkdir -p dataset/val/{rose,sunflower,tulip}")
        print("然后将图片放入对应文件夹")
    
    # 进入 PaddleClas 目录
    os.chdir(paddleclas_dir)
    
    # 执行训练命令
    import subprocess
    
    print("🚀 开始训练...")
    print(f"📋 配置文件：{config_file}")
    print("=" * 60)
    
    cmd = [
        sys.executable,
        'tools/train.py',
        '-c', f'../{config_file}'
    ]
    
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        print("=" * 60)
        print("✅ 训练完成！")
        print("模型已保存到：../output/MobileNetV3_small_x1_0/")
    else:
        print("❌ 训练失败，请检查错误信息")
        sys.exit(1)

if __name__ == '__main__':
    main()
