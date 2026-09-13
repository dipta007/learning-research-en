<!--
source: notion page 设备配置
source page id: 59569d7b-6695-4578-b21b-f1dc6ea35776
source fetched: 2026-09-11
status: verified against the Chinese source over 4 rounds, last on 2026-09-12. The final round found nothing. Still needs review by a Chinese reader.
figures: 0
-->

# Machine Setup

> [Original Article](https://pengsida.notion.site/59569d7b66954578b21bf1dc6ea35776)

> **Translator's note.** Command blocks are reproduced as written, including their typos, because silently "fixing" a command someone will paste is worse than leaving it. The only change is that a few non-breaking spaces used as comment padding became ordinary spaces, which affects nothing. Four things worth knowing before you paste:
>
> - The `python -c "import torch; print(torch.version.cuda)”` line opens with a straight quote and closes with a curly one (`”`, U+201D), so the quote never closes and a shell will sit waiting for more input. This is the one that fails quietly; the other three fail loudly.
> - `cacdt /path_to_cuda_your_using/version.txt` should be `cat`.
> - `setw- g mouse-resize-pane` should be `setw -g`.
> - `chsh -s /usr/bin/zsh  #更改默认shellOx` has a stray `Ox` at the end of the comment.
>
> One inline reference in the tools list did not resolve when the page was fetched, and appears as `‣` in the source. He notes it holds some usage instructions for fzf.
>
> The [getting started page](../../en/getting-started-in-research.md) credits He Xingyi with collecting these.

## 1. Shell configuration

Using zsh as the default shell is very handy.

First, installing oh my zsh, the zsh management tool: [https://github.com/ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)

Then the plugins.

**1. Copying the shell configuration between machines**: [https://github.com/rutchkiwi/copyzshell](https://github.com/rutchkiwi/copyzshell)

If a machine already has an oh my zsh configuration and a new machine needs configuring, then as long as zsh is present you do not need to run the few steps below again. Do not install oh my zsh; just transfer it. If you do install it, it cannot be overwritten directly, which is fairly troublesome. Just transfer it instead. If you need to add the machine's port, see the issue.

**2. Command highlighting and command syntax checking (must install)**: [https://github.com/zsh-users/zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)

*Note: use the oh my zsh installation method given there, which makes migration easier.

**3. Auto suggestion (must install)**: [https://zhuanlan.zhihu.com/p/111707433](https://zhuanlan.zhihu.com/p/111707433)

If the completion shows the line you want, select it directly with ctrl+f.

If you need to show all the options: pressing tab once only shows all the options and you still need to type manually; pressing tab twice lets you select an option directly with the arrow keys.

**4. fzf together with history (must install).**

Switching the default shell manually:

```
cat /etc/shells  #查看所有shell

echo $SHELL      #查看当前使用的shell

chsh -s /usr/bin/zsh  #更改默认shellOx
```

(In order: list all shells; show the shell currently in use; change the default shell.)

If changing the default shell needs a password and you do not know it, a fairly good way round it is to add the line `zsh` at the end of `~/.bashrc`. That starts zsh directly, and once started it will run `~/.zshrc` once.

### Some commonly used tools

- **ncdu**: `apt-get install ncdu`, to see what a folder is taking up.
- **nvtop**, and if it will not install, use **nvitop** (install into the Python environment from GitHub).
- **fzf**: ‣ which also holds some usage instructions.
- **ctop**: monitors the resource usage of each docker container (needs sudo).
- **tmux**: see below.
- **vim**: see below.

### tmux configuration

Adding the mouse in tmux:

```
touch ~/.tmux.conf
echo "set -g mouse on" >> ~/.tmux.conf 

#如果上面的不行就先在~/.tmux.conf中添加：
setw -g mode-mouse on
setw- g mouse-resize-pane
setw -g mouse-select-pane
setw -g mouse-select-window
set-option -g history-limit 5000

#然后
tmux source-file ~/.tmux.conf
```

(The first comment: if the above does not work, first add the following to `~/.tmux.conf`. The second: then run.)

A good all-round tmux configuration (strongly recommended): [https://github.com/samoshkin/tmux-config](https://github.com/samoshkin/tmux-config)

It needs tmux newer than 2.4; check the version with `tmux -V`. I found 2.1 works too.

Note that you still need `tmux souce-file xx`.

If there is a syntax error, see: [https://github.com/samoshkin/tmux-config/issues/38](https://github.com/samoshkin/tmux-config/issues/38)

### vim configuration

[https://github.com/amix/vimrc](https://github.com/amix/vimrc)

`ssh-keygen -t rsa`

```
vim ~/.vimrc
set nu   # 在vimrc文件中添加set nu打开显示行
let g:snipMate = { 'snippet_version' : 1 } # 在vimrc文件最后加上防止一打开vim就报xxdecrepit
```

(The comments: add `set nu` in the vimrc file to turn on line numbers; add the second line at the end of the vimrc file to stop vim complaining about a deprecation as soon as it opens.)

Adding a file tree to vim: [https://github.com/preservim/nerdtree](https://github.com/preservim/nerdtree)

Then, to make NERDTree open and close automatically: [https://riptutorial.com/vim/example/30660/nerd-tree](https://riptutorial.com/vim/example/30660/nerd-tree)

If you want the cursor to sit in the current file after opening, use this instruction rather than the one in that link:

```
# Start NERDTree and put the cursor back in the other window.
autocmd VimEnter * NERDTree | wincmd p
```

## 2. Downloading and configuring anaconda / miniconda

anaconda:

```
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2019.10-Linux-x86_64.sh
```

If that is too slow, use miniconda: [https://repo.anaconda.com/miniconda/](https://repo.anaconda.com/miniconda/)

```
wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.3-Linux-x86_64.sh
```

Find the version you want there and swap the anaconda path for the one you want.

Installing and refreshing:

```
zsh Anaconda3-2019.10-Linux-x86_64.sh

source ~/.zshrc
```

Change the name to the filename you downloaded.

If after this conda cannot find the command, it was installed under bashrc. Open `vi ~/.bashrc`, find everything relevant, copy it into `~/.zshrc`, then source again.

### 2.1 conda environment commands

[https://blog.csdn.net/hejp_123/article/details/92151293](https://blog.csdn.net/hejp_123/article/details/92151293)

Creating a new environment:

```
conda create --name your_env_name python=3.6
```

Creating a new environment from a yaml file:

```
conda env create -f filepath.yaml
```

Deleting an environment:

```
conda remove -n your_env_name --all

conda remove --name your_env_name --all
```

Using a domestic conda mirror to speed things up:

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes
```

Using a company conda mirror to speed things up: [https://dx-mirrors.sensetime.com/help/use-conda-mirror.html](https://dx-mirrors.sensetime.com/help/use-conda-mirror.html)

### 2.2 Specifying a pip source

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple tensorboard
```

**Note: check whether the pip you are using is the one in the current conda environment:

```
which pip 
# if not(经常会掉）
conda deactivate
conda activate
which pip
```

(The comment: if not, which happens often.)

If pip was installed through conda, then pip and conda are connected and can each find the packages the other installed.

```
# update package
pip install -U name
```

Using a domestic pip mirror to speed things up:

```
1.临时设置方法：

可以在使用pip的时候加在最后面加上参数 -i https://pypi.tuna.tsinghua.edu.cn/simple

例如：pip install jieba -i https://pypi.tuna.tsinghua.edu.cn/simple  # jieba 是一个包

2.永久设置方法：

pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

配置完之后就可以像平常一样安装包，速度提升几十倍

例如：pip install jieba

切换为阿里云进行下载

pip install pandas -i http://mirrors.aliyun.com/pypi/simple/   --trusted-host mirrors.aliyun.com
pip install pandas -i http://mirrors.aliyun.com/pypi/simple/


阿里云 http://mirrors.aliyun.com/pypi/simple/
豆瓣(douban) http://pypi.douban.com/simple/ 
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
```

That block, in English: method 1, set it temporarily, by adding `-i https://pypi.tuna.tsinghua.edu.cn/simple` at the end when you use pip, for example `pip install jieba -i ...`, where jieba is a package. Method 2, set it permanently, with `pip install pip -U` then `pip config set global.index-url ...`; after configuring it you install packages as usual and the speed improves by tens of times. Then switching to Aliyun to download, with the two `pip install pandas` forms. The four mirrors listed are Aliyun, Douban, Tsinghua University and the University of Science and Technology of China.

## 3. Choosing the cuda version

To choose the cuda version, configure the following in `~/.zshrc`. If `nvcc -V` fails, you also need to add the following:

```
export CUDA_VER=版本号（例如：9.0）

export PATH=/usr/local/cuda-$CUDA_VER/bin:$PATH

export LD_LIBRARY_PATH=/usr/local/cuda-$CUDA_VER/lib64:$LD_LIBRARY_PATH
```

(`版本号（例如：9.0）` means the version number, for example 9.0.)

The paths below should follow where cuda actually is. Finally `source ~/.zshrc` to enable it.

The matter of matching cuda versions: the major versions of pytorch, of cudatoolkit, and of the cuda the system uses all need to match.

```
python -c "import torch; print(torch.version.cuda)”    #查看pytorch的版本

conda list | grep cudatoolkit                          #查看cudatoolkit版本

cacdt /path_to_cuda_your_using/version.txt               #查看系统使用的cuda版本，路径还得看~/.zshrc

或者用：nvcc --version                                  #查看系统使用的cuda版本
```

(In order: check pytorch's version; check the cudatoolkit version; check the cuda version the system uses, where the path depends on `~/.zshrc`; or use `nvcc --version` to check the cuda version the system uses.)

Note: even when those three match, if the GPU driver version does not match the cuda version, cuda cannot be used. Check whether cuda is available:

```
import torch
print(torch.cuda.is_available())
```

## 4. Passwordless login to a server

Using an ssh key: copy the key from your own machine's `id_rsa.pub` into the `authorized_keys` file in `.ssh/` on the target server. If that file does not exist, create it and cat your local `id_rsa.pub` into it.

If there is a problem, the folder permissions may be wrong: [https://serverfault.com/questions/525045/ssh-connection-asks-for-password-although-key-is-accepted](https://serverfault.com/questions/525045/ssh-connection-asks-for-password-although-key-is-accepted)

```
chmod 755 ~/.ssh                  #修改.ssh目录权限755
```

(The comment: change the `.ssh` directory permissions to 755.)

Or the copy went wrong, in which case it is suggested that you first rsync your machine's `id_rsa.pub` to the target machine, then:

```
cat temp.pub >> authorized_keys
```
