#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
花卉分类评估脚本
评估模型性能
"""

import os
import sys
import argparse


def main():
    """主评估函数"""
    
    parser = argparse.ArgumentParser(description='花卉分类模型评估脚本')
    parser.add_argument(
        '--model',
        type=str,
        default='./output/MobileNetV3_small_x1_0/best_model',
        help='模型路径（默认：best_model）'
    )
    
    args = parser.parse_args()
    
    # 配置文件
    config_file = './flower_config.yaml'
    paddleclas_dir = './PaddleClas'
    model_path = args.model
    
    # 检查必要文件
    if not os.path.exists(config_file):
        print(f"❌ 错误：找不到配置文件 {config_file}")
        sys.exit(1)
    
    if not os.path.exists(paddleclas_dir):
        print(f"❌ 错误：找不到 PaddleClas 目录")
        sys.exit(1)
    
    if not os.path.exists(model_path):
        print(f"⚠️  模型不存在：{model_path}")
        print("请确保已完成训练")
        sys.exit(1)
    
    # 进入 PaddleClas 目录
    os.chdir(paddleclas_dir)
    
    # 执行评估命令
    import subprocess
    
    print("📊 开始评估模型...")
    print(f"📋 配置文件：{config_file}")
    print(f"🤖 模型：{model_path}")
    print("=" * 60)
    
    cmd = [
        sys.executable,
        'tools/eval.py',
        '-c', f'../{config_file}',
        '-o', f'Global.pretrained_model=../{model_path}'
    ]
    
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        print("=" * 60)
        print("✅ 评估完成！")
    else:
        print("❌ 评估失败")
        sys.exit(1)


if __name__ == '__main__':
    main()
