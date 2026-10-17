# 故事板输出约定

完整模式需要本约定；用户只要 Story、对白或单幕时，只交付相应部分，不强行输出所有字段。

## 完整交付

展示顺序固定为 **Story → 分镜 → 各幕实际首帧图片 → 基于这些图片的视频提示词 → Caption**。先完成并检查出图，再写视频提示词；Caption 放在交付末尾。用户明确只要文本或某个中间产物时按其范围缩减。

先写标题、总时长、市场／语言、模式、主要角色和产品。将用户指定项与补全假设简短区分；不要展开与任务无关的后台参数。

使用创作参数时附“采用参数”摘要：列明用户指定和自动补全的视觉风格、类型、电影风格、镜头、灯光、皮肤、幕数×单幕时长、每幕镜头数、比例、语言及目标模型。仅展示本任务实际采用的项目，模型未指定则不假定已选平台。参数变化必须反映在下方分镜和提示词中；改写用户参数或解决冲突时说明具体调整。

**Story**：用一段完整叙述讲清开头、行动、变化和结尾。人物动机与商品出现的原因具体可见。若用户在研究另一个网站的结果，先忠实保存和说明其原 Story，再另列改进建议，不能将改写冒充提取结果。

**连续性要点**：列出商品关键外观、人物参考、固定服装、允许变化的场景／道具和镜头间状态。参考图只能锁定可见部分，未见背面或遮挡处不应伪称已确认。

**分镜表**：

| 幕与作用 | 全片时间／单幕时长 | 幕内镜头与动作 | 对白／旁白 | 首帧与收尾状态 |
|---|---|---|---|---|
| Scene N：本幕具体推进 | 连续全片时间；明确是否含转场 | 每个镜头的相对时间、景别、人物／产品动作、必要机位变化 | 原语言；标出讲话者与开始时机 | 第一镜头开始状态；本幕结束位置与产品状态 |

两套时间需相互一致：例如第 2 幕全片 8–16 秒，内部镜头 0–3 和 3–8 秒，总计 8 秒。不能把“3 个 8 秒场景”写成“8 秒成片”。

每幕后可给中文对白翻译，避免把翻译混入提交给视频模型的原对白。声音设计用简短明确的环境声／音效／配乐描述，别重复填写相同内容。

模式专用交付：Timelapse 增加“起始状态→阶段行动→可见变化→最终状态”及各阶段的连续性锚点，标明时间压缩或阶段跳切；Narrative 先给可连续朗读的 Full Narrator Script，再给逐幕原文分配、入出点、停顿、语速意图和配套画面。逐幕片段按顺序拼接应与整段旁白一致，除明确的无声段外不漏句、不重复；Cinematic 保留角色动作、反应及必要对白。只交付用户要求的部分。

## 每幕生成包

保持以下概念分开；如用户只需要一种模型的提示词，可合并展示，但不丢失首帧逻辑。完整任务先完成 Image Direction 和实际出图，再交付视频提示词。

### Storyboard Prompt

用于描述整幕计划，包含人物、商品、场景、光线、镜头时间、动作、对白和声音。它不等于所有模型的通用 API 输入。

### Image Direction / Proposed Image Prompt

```text
Reference roles: [character reference] determines the presenter's appearance and required coverings. [product reference] determines [the exact hero item, not the whole reference outfit].
First frame: [initial pose, hands, gaze, exact product position and state].
Product details: [specific visible colour, silhouette, construction and distinguishing details].
Wardrobe: [fixed clothing; clearly separate newly chosen complementary pieces].
Setting and framing: [location, time of day, shot size, camera position, light].
Visual treatment: [concrete composition, palette and skin rendering from the selected controls; preserve identifiable product colour and reference features].
Continuity requirements: [the few constraints material to this scene].
Exclusions: [only relevant unwanted text, logos, wardrobe substitutions or artifacts].
```

删去不适用字段，填成具体描述，不在最终可复制提示词中遗留占位符。不能因为写了“match exactly”就省略可辨认的产品细节或承诺完全复现。

### 实际首帧图片与验收

按各幕 Image Direction 生成并查看图片，交付可打开的结果位置。核对人物、领口／袖子／标识／图案等商品关键细节、首帧姿势及跨幕连续性；不合格的结果不作为视频提示词的起点。记录实际使用的图片输入与提示词，把未执行的方案标为 Proposed。要求原图完全保真时，优先保留原图画面，不能将生成式重绘称为 100% 对版。

### Proposed Video Prompt

在选定实际首帧后撰写，与该图片中已经可见的人物、商品、手势、道具和机位一致。用户明确只要纯文本时，才按拟定首帧写并明确标为 Proposed。

先按实际输入模式选择开头。以下框架以已提供首帧为例；只有参考图时写真实参考分工，从文字生成时直接写主体与场景，首尾帧模式写中间动作如何连接，编辑模式先写修改范围。Omni 的模式写法及用户参考文档的来源说明见 [omni-prompt-writing.md](omni-prompt-writing.md)。实际交付填成自然语言段落，保留用户需要的切镜与关键时点，不必逐行复述所有栏目。

```text
Start from the supplied first frame: [initial state, identical to the image prompt].
Keep [reference character appearance and coverings], [hero product details] and [fixed wardrobe] consistent.
Scene: [location and lighting/time of day]. Planned duration: [D seconds].
Visual treatment: [resolved visual style, cinematic look and skin texture; express observable properties rather than only preset names].
[0–t seconds]: [one feasible action, framing and camera behaviour].
[t–D seconds]: [next action and resulting state, with explicit cut only if intended].
Dialogue/voiceover: [speaker, language, exact line, performance and start cue].
Sound: [ambience, needed SFX, music if requested].
End state: [pose, product and location that support the next scene].
Relevant exclusions: [short list].
```

时间与控制是否可执行依目标模型而定；文本时间码是计划，不是已保证的镜头控制。如果平台不支持多镜头，优先按每镜生成并说明后期拼接需求，或在用户要求下改成可连续完成的单镜头。

## 可选发布文案

仅在用户需要广告／社媒交付时给 Caption 与合适的标签。使用真实产品称呼和故事中的具体事件；不宣称“SEO 已优化”或保证流量。价格、材质、性能、优惠、证言都要有依据。

本用户的 TikTok 商品短视频项目默认在最终交付末尾附可直接复制的 Caption；用户只要某个中间产物或明确不要文案时尊重其范围。Caption 用“首句具体 Hook → 一两句故事共鸣 → 自然互动问题”的结构，语言沿用项目市场设置，附 3–5 个相关标签即可。Hook 可以用反差、疑问或故事中的原话，但必须有成片内容支撑；不为了吸睛捏造剧情或商品承诺。Caption 与视频内字幕是独立交付，不能因需要发布文案自动添加烧录字幕。

## 实际执行的记录

执行媒体生成时，用紧凑表记录：平台／所选模型、参考图用途、实际提交提示词、时长／比例／分辨率、界面报价、已知前后余额、输出位置、成功／失败与观察到的问题。界面扣点与实际余额差异都要保留；不凭套餐均摊替代真实现金支出。

如果导出为资料包，保留原始提示词与结果，再附中文解释和人工评价。外部结果标题叫“Actual Submitted”时，也要明确它来自平台导出，并不能据此确认后台隐藏设置。
