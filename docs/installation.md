# 安装与更新

## 方法一：让Codex安装

把下面一段发给Codex：

~~~text
使用 $skill-installer。
从GitHub仓库 pusatpakaiankime-bit/product-storytelling-studio
安装路径 skills/product-storytelling-studio。
~~~

安装器会下载该目录，默认放到：
- Windows：%USERPROFILE%\.codex\skills\product-storytelling-studio
- macOS／Linux：~/.codex/skills/product-storytelling-studio
- 配置了CODEX_HOME时：CODEX_HOME/skills/product-storytelling-studio

私有仓库需要当前GitHub账号有仓库访问权限。不要把访问令牌放进指令、截图或仓库。

已存在同名Skill时，安装器会停止；更新可用下方本地脚本。安装完成后，在下一轮对话调用Skill。

## 方法二：下载ZIP，手动安装

1. 下载[仅Skill安装包](../dist/product-storytelling-studio.zip)。
2. 解压后应得到一个 product-storytelling-studio 文件夹，里面直接有 SKILL.md、agents、references。
3. 把这个文件夹放到当前Codex的 skills 目录。
4. 确保没有多套一层 product-storytelling-studio/product-storytelling-studio。
5. 下一轮对话输入“使用 $product-storytelling-studio”，并附商品图与任务。

正确结构：

~~~text
.codex/
└── skills/
    └── product-storytelling-studio/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/
            ├── creative-controls.md
            ├── option-catalog.json
            ├── output-contract.md
            ├── story-modes.md
            ├── tone-presets.md
            └── omni-prompt-writing.md
~~~

## 方法三：克隆仓库后用本地脚本安装

先安装Git和Python 3，再运行：

~~~sh
git clone https://github.com/pusatpakaiankime-bit/product-storytelling-studio.git
cd product-storytelling-studio
python scripts/install.py
~~~

macOS／Linux若命令名为python3，可把python替换为python3。私有仓库按Git的正常认证流程访问。

默认安装目录已存在时，脚本会停止，不覆盖。

更新：

~~~sh
git pull --ff-only
python scripts/install.py --update
~~~

更新前会把已有Skill备份成ZIP，保存在所选安装根目录旁的 skill-backups 目录；备份路径会打印出来。更新会覆盖本包中的同名文件，保留额外的本地文件。正式更新前请自行保留有意做过的个性化修改。

自定义安装目录：

~~~sh
python scripts/install.py --dest "/absolute/path/to/skills/product-storytelling-studio"
~~~

## 验证安装

发给Codex：

~~~text
使用 $product-storytelling-studio。
先不要生成媒体，告诉我当前带货语气、画面默认值和交付内容。
~~~

应能读取到：版本v1.1.1；带货默认高能兴奋；人物、背景、皮肤为Realistic；完整任务按故事、分镜、实际首帧图、基于出图的视频提示词、最后Hook Caption的顺序交付。不同任务可以明确覆盖这些默认值。

## 卸载

在文件管理器中将安装目录 product-storytelling-studio 移到系统回收站即可。仓库图片、脚本输出及此前生成的媒体是独立文件，不会随Skill目录一起消失。

