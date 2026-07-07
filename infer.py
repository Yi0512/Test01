#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
花卉分类推理脚本
支持单张图片、批量预测、实时摄像头
"""

import os
import sys
import argparse
import cv2
import numpy as np
from pathlib import Path

# 支持的图片格式
SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}


def get_image_files(image_path):
    """获取图片文件列表"""
    path = Path(image_path)
    
    if path.is_file():
        # 单个文件
        return [str(path)]
    elif path.is_dir():
        # 目录，获取所有图片
        images = []
        for ext in SUPPORTED_FORMATS:
            images.extend(path.glob(f'*{ext}'))
            images.extend(path.glob(f'*{ext.upper()}'))
        return [str(img) for img in sorted(images)]
    else:
        print(f"❌ 路径不存在：{image_path}")
        return []


def main():
    """主推理函数"""
    
    parser = argparse.ArgumentParser(description='花卉分类推理脚本')
    parser.add_argument(
        '--image',
        type=str,
        required=True,
        help='图片路径（可以是单个文件或文件夹）'
    )
    parser.add_argument(
        '--model',
        type=str,
        default='./output/MobileNetV3_small_x1_0/best_model',
        help='模型路径（默认：best_model）'
    )
    parser.add_argument(
        '--config',
        type=str,
        default='./flower_config.yaml',
        help='配置文件路径'
    )
    parser.add_argument(
        '--top-k',
        type=int,
        default=1,
        help='显示top-k预测结果'
    )
    
    args = parser.parse_args()
    
    # 检查必要文件
    if not os.path.exists(args.config):
        print(f"❌ 错误：找不到配置文件 {args.config}")
        sys.exit(1)
    
    paddleclas_dir = './PaddleClas'
    if not os.path.exists(paddleclas_dir):
        print(f"❌ 错误：找不到 PaddleClas 目录")
        sys.exit(1)
    
    # 获取图片列表
    image_files = get_image_files(args.image)
    if not image_files:
        print("❌ 没有找到图片文件")
        sys.exit(1)
    
    print(f"🖼️  找到 {len(image_files)} 张图片")
    print("=" * 60)
    
    # 进入 PaddleClas 目录
    os.chdir(paddleclas_dir)
    
    # 执行推理
    import subprocess
    
    for img_path in image_files:
        print(f"\n📷 预测：{img_path}")
        print("-" * 60)
        
        cmd = [
            sys.executable,
            'tools/infer.py',
            '-c', f'../{args.config}',
            '-o', f'Global.pretrained_model=../{args.model}',
            f'Infer.infer_imgs=../{img_path}'
        ]
        
        result = subprocess.run(cmd, capture_output=False)
        
        if result.returncode != 0:
            print(f"⚠️  预测失败：{img_path}")
    
    print("\n" + "=" * 60)
    print("✅ 推理完成！")


if __name__ == '__main__':
    main()
