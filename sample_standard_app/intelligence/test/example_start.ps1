# 忽略管道错误，PowerShell中一般不会出现类似的问题，所以可以忽略

# 判断conda命令是否存在，如果不存在，则检查%USERPROFILE%\miniconda3\bin是否存在，如果存在则将conda添加到路径中
if (-not (Get-Command conda -ErrorAction SilentlyContinue)) {
    if (Test-Path "$env:USERPROFILE\miniconda3\Scripts\conda.exe") {
        Write-Output "conda already installed. Adding $env:USERPROFILE\miniconda3\Scripts to PATH..."
        $env:PATH = "$env:USERPROFILE\miniconda3\Scripts;$env:PATH"
    } else {
        Write-Output "conda is not installed..."
    }
} else {
    Write-Output "conda is already installed."
}

# 定义安装conda的函数
function Install-Conda {
    if (-not (Get-Command conda -ErrorAction SilentlyContinue)) {
        Write-Output "conda is not installed. Please install conda first, and try again"
        New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\miniconda3"

        curl  https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py39_24.3.0-0-Windows-x86_64.exe -o miniconda.exe
        ./miniconda.exe
        exit

        # # 静默安装Miniconda
        # Start-Process -Wait -FilePath "$env:USERPROFILE\miniconda3\miniconda.exe" -ArgumentList "/InstallationType=JustMe", "/RegisterPython=0", "/AddToPath=0", "/S", "/D=$env:USERPROFILE\miniconda3"
        # $env:PATH = "$env:USERPROFILE\miniconda3\Scripts;$env:USERPROFILE\miniconda3;$env:PATH"
        # Remove-Item "$env:USERPROFILE\miniconda3\miniconda.exe"
        
        # # 配置清华源
        # conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
        # conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
        # conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
        # conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
        # Write-Output "conda is installed."
    }
}

# 检查Python是否安装，如果没有安装则安装它，或者Python的版本小于3.10
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Output "Python is not installed. Installing Python..."
    Install-Conda
}
# 获取当前的Python版本
$pythonVersion = & python --version 2>&1

# 如果Python版本不是3.10，则安装Python 3.10
if ($pythonVersion -notmatch "3\.10") {
    if (-not (Get-Command conda -ErrorAction SilentlyContinue)) {
        Write-Output "conda is not installed. Please install conda and try again."
        Install-Conda
    }
    
    # 检查是否已经有名为python_au3.10的环境
    if (-not (& conda env list | Select-String -Pattern "python_au3.10")) {
        Write-Output "Python 3.10 environment is not installed. Installing Python 3.10 environment..."
        conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
        conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
        conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
        conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
        conda create -n python_au3.10 python=3.10 -y
    }
    
    # 获取Conda的基础路径并设置PATH变量
    $CONDA_BASE = & conda info --base
    $env:PATH = "$CONDA_BASE\envs\python_au3.10\Scripts;$CONDA_BASE\envs\python_au3.10;$env:PATH"
}

# 切换到Python 3.10的环境
conda activate python_au3.10

python --version

# 判断pip是否已经安装了agentUniverse
if (-not (& pip list | Select-String -Pattern "agentUniverse")) {
    pip install agentUniverse -i https://pypi.tuna.tsinghua.edu.cn/simple
}

# 检查 custom_key 文件是否存在，如果不存在，从样本复制一份
if (-not (Test-Path "..\..\config\custom_key.toml")) {
    Copy-Item "..\..\config\custom_key.toml.sample" "..\..\config\custom_key.toml"
}

# 替换 config.toml 中的 #custom_key_path 为 custom_key_path
# 确保设置 custom_key_path 正确引用 config 目录下的文件
(Get-Content -Path "..\..\config\config.toml") -replace '^#custom_key_path = ''\.\/custom_key\.toml''', 'custom_key_path = ''custom_key.toml''' | Set-Content -Path "..\..\config\config.toml"

# 设置PYTHONPATH为当前工作目录的上级目录
# 获取当前目录的上两级目录的绝对路径
$upperTwoLevels = Resolve-Path (Join-Path (Get-Location) "..\..\")

# 设置 PYTHONPATH 环境变量
$env:PYTHONPATH = $upperTwoLevels.Path

# 启动服务
python -u .\react_chat_bot.py
