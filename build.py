import os
import subprocess
import shutil
import sys
from pathlib import Path

def install_requirements():
    print("检查并安装依赖...")
    try:
        # 升级 pip
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        
        # 安装必要的包
        requirements = ["PyQt6", "pyinstaller"]
        for package in requirements:
            print(f"安装 {package}...")
            subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
            
        print("依赖安装完成！")
    except subprocess.CalledProcessError as e:
        print(f"依赖安装失败: {e}")
        sys.exit(1)

def build_macos_app():
    print("开始构建 macOS 应用...")
    
    # 首先安装依赖
    install_requirements()
    
    # 清理之前的构建文件
    dist_path = Path("dist")
    build_path = Path("build")
    if dist_path.exists():
        shutil.rmtree(dist_path)
    if build_path.exists():
        shutil.rmtree(build_path)
        
    try:
        # 使用 PyInstaller 构建
        cmd = [
            sys.executable,  # 使用当前 Python 解释器
            "-m",
            "PyInstaller",
            "--name", "视频播放器",
            "--windowed",
            "--onefile",
            "--target-arch", "x86_64",
            "main.py"
        ]
        
        subprocess.run(cmd, check=True)
        
        # 设置执行权限
        app_path = dist_path / "视频播放器"
        if app_path.exists():
            os.chmod(app_path, 0o755)
            
        print("构建完成！")
        print(f"应用程序位置: {app_path.absolute()}")
        
    except subprocess.CalledProcessError as e:
        print(f"构建失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    build_macos_app()