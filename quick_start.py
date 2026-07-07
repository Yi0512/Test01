#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速开始脚本 - 一键运行所有步骤
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(cmd, description):
    """运行命令并显示结果"""
    print("\n" + "=" * 60)
    print(f"▶️  {description}")
    print("=" * 60)
    result = subprocess.run(cmd, shell=True)
    return result.returncode == 0


def main():
    """主函数"""
    
    print("""
    ╔══════════════════════════════════════════════════════╗
    ║        🌹 花卉分类项目 - 快速开始                      ║
    ║        PaddleClas Flower Classification               ║
    ╚══════════════════════════════════════════════════════╝
    """)
    
    # 检查环境
    print("🔍 检查环境...")
    
    if not os.path.exists('./flower_config.yaml'):
        print("❌ 找不到 flower_config.yaml")
        sys.exit(1)
    
    if not os.path.exists('./PaddleClas'):
        print("⚠️  需要克隆 PaddleClas 框架...")
        if run_command(
            'git clone https://github.com/PaddlePaddle/PaddleClas.git',
            '克隆 PaddleClas 仓库'
        ):
            run_command('cd PaddleClas && pip install -r requirements.txt', '安装依赖')
        else:
            print("❌ 克隆失败")
            sys.exit(1)
    
    # 检查数据集
    if not os.path.exists('./dataset/train'):
        print("""
        ⚠️  需要准备数据集！
        
        请创建以下目录结构：
        
        mkdir -p dataset/train/{rose,sunflower,tulip}
        mkdir -p dataset/val/{rose,sunflower,tulip}
        
        然后将花卉图片放入对应文件夹：
        - dataset/train/rose/        # 玫瑰训练集（20-50张）
        - dataset/train/sunflower/   # 向日葵训练集
        - dataset/train/tulip/       # 郁金香训练集
        - dataset/val/               # 验证集（5-10张/类）
        
        下载图片资源：
        - Unsplash: https://unsplash.com (搜索 "rose flower")
        - Pexels: https://www.pexels.com (搜索 "sunflower")
        - Pixabay: https://pixabay.com (搜索 "tulip")
        """)
        print("准备好数据后再运行此脚本")
        sys.exit(0)
    
    print("✅ 环境检查完成")
    
    # 选择操作
    print("""
    请选择操作：
    1. 🚀 训练模型
    2. 📊 评估模型
    3. 🖼️  图片分类
    4. 📈 启动可视化（VisualDL）
    5. 🔄 完整流程（训练 → 评估 → 预测）
    """)
    
    choice = input("请输入选项（1-5）：").strip()
    
    if choice == '1':
        # 训练
        print("\n🚀 开始训练...")
        run_command(
            'cd PaddleClas && python tools/train.py -c ../flower_config.yaml',
            '模型训练'
        )
    
    elif choice == '2':
        # 评估
        print("\n📊 开始评估...")
        model_path = input("请输入模型路径（默认：output/MobileNetV3_small_x1_0/best_model）：").strip()
        if not model_path:
            model_path = 'output/MobileNetV3_small_x1_0/best_model'
        
        run_command(
            f'cd PaddleClas && python tools/eval.py -c ../flower_config.yaml -o Global.pretrained_model=../{model_path}',
            '模型评估'
        )
    
    elif choice == '3':
        # 推理
        print("\n🖼️  开始分类...")
        image_path = input("请输入图片路径：").strip()
        if not image_path:
            print("❌ 未输入路径")
            sys.exit(1)
        
        model_path = input("请输入模型路径（默认：output/MobileNetV3_small_x1_0/best_model）：").strip()
        if not model_path:
            model_path = 'output/MobileNetV3_small_x1_0/best_model'
        
        run_command(
            f'cd PaddleClas && python tools/infer.py -c ../flower_config.yaml -o Global.pretrained_model=../{model_path} -o Infer.infer_imgs=../{image_path}',
            '图片分类'
        )
    
    elif choice == '4':
        # 可视化
        print("\n📈 启动 VisualDL...")
        print("打开浏览器访问：http://localhost:8040")
        run_command(
            'visualdl --logdir=./PaddleClas/output --port 8040',
            'VisualDL 可视化'
        )
    
    elif choice == '5':
        # 完整流程
        print("\n🔄 执行完整流程...")
        
        # 训练
        if not run_command(
            'cd PaddleClas && python tools/train.py -c ../flower_config.yaml',
            '1️⃣  模型训练'
        ):
            print("❌ 训练失败")
            sys.exit(1)
        
        # 评估
        if not run_command(
            'cd PaddleClas && python tools/eval.py -c ../flower_config.yaml -o Global.pretrained_model=../output/MobileNetV3_small_x1_0/best_model',
            '2️⃣  模型评估'
        ):
            print("❌ 评估失败")
            sys.exit(1)
        
        # 预测
        test_image = input("\n请输入测试图片路径（用于预测）：").strip()
        if test_image:
            run_command(
                f'cd PaddleClas && python tools/infer.py -c ../flower_config.yaml -o Global.pretrained_model=../output/MobileNetV3_small_x1_0/best_model -o Infer.infer_imgs=../{test_image}',
                '3️⃣  图片分类'
            )
        
        print("\n" + "=" * 60)
        print("✅ 完整流程执行完成！")
        print("=" * 60)
    
    else:
        print("❌ 无效的选项")
        sys.exit(1)
    
    print("\n✨ 谢谢使用！")


if __name__ == '__main__':
    main()
