# Omni Flash 1.1 提示词写作参考（供 Codex 读取）

核验日期：2026-10-03（马来西亚时间）
性质：根据 Google 官方页面整理的学习文件，由助手编写，**不是 Google 发布的独立官方手册**。
范围：仅提示词写作；不含 API、收费或 Flow 操作教程。

## 1. 证据标签

- [OFFICIAL SUMMARY]：官方页面内容的概括，附来源。
- [CODEX RULE]：为方便提示词写作归纳的工作规则，不是 Google 原话。
- [KM RULE]：KM Fashion 的业务要求，不代表模型官方能力。
- [AUTHORED EXAMPLE]：助手编写的模板，不是 Google 官方示例。

不得将 Veo 的模型专属技巧、第三方教程或本文件模板宣称为 Omni Flash 1.1 官方要求。

## 2. 官方依据

### [OFFICIAL SUMMARY] 生成与参考素材 — S1

场景提示应具体描述主体、动作、环境、光线与风格。
有参考素材时，说明每份素材在视频中的作用；文字应与图像一致。
干净、纯色或分离背景的主体/产品参考，以及相互协调的视觉风格，有助于融合。
首尾帧模式中，描述两帧之间发生的动作或过渡。

### [OFFICIAL SUMMARY] 编辑 — S2

视频编辑提示说明希望改变的内容。可添加参考素材和后续修改提示；页面注明可保持编辑上下文继续最多三轮对话。
官方编辑例句（本文件唯一原文摘录）：

> Change the lighting to a cinematic sunset

### [OFFICIAL SUMMARY] 模型名称与模式 — S3

官方功能表明确列出 Gemini Omni Flash 1.1，支持文字、首帧、首尾帧、参考素材生成及视频编辑。因此本文件分别提供这些任务的写作框架。
通用 Flow 写作建议不等于独立的 Omni 1.1 专属手册；不要声称所有建议专为该模型发布。

## 3. [CODEX RULE] 写作流程

1. 先判断任务：从零生成 / 参考图生成 / 首帧动画 / 首尾帧过渡 / 编辑现有视频。
2. 识别真实输入。只能引用用户确实提供的图片、视频或语音，不能虚构素材绑定。
3. 列出允许改变与必须保留的内容。发现参考冲突时先指出冲突。
4. 使用自然语言写清一个可执行的动作序列；动作数量与视频时长相匹配。
5. 以具体构图与机位描述取代含糊的“cinematic”。这是编写建议，不是官方强制语法。
6. 有口播时给出逐字台词、语言和语气；无口播时明确声音需求。不要凭空添加音乐或台词。
7. 优先输出一份可直接粘贴的完整提示词，不附 API 参数或操作教程。
8. 锁定指令表达生成目标，不能保证逐像素保留、绝对同脸或产品百分百不变。发现结果偏差时再写针对性修正。
9. 时长与比例是创作需求；写进文字不代表已设置界面选项。能力限制应重新核查 S3，不能沿用其他模型规格。

## 4. [KM RULE] 服装与人物参考

Image 1 = 产品来源：只取服装结构、颜色、材质及可见细节。
Image 2 = 人物来源：只取人物身份、五官、肤色与用户指定的头巾造型。
若输入顺序不同，应跟随实际上传顺序重新标注。

- Farah、Hawra、Alyasofea 各用自己的固定人物参考，不混用。
- 保留产品实际颜色名称与结构；不可凭空加入口袋、纽扣、抽绳、刺绣或 logo。
- 只列产品真实存在且能够确认的细节。看不清时不得猜测。
- Muslimah 默认完整遮盖头发、颈部、胸口、手臂、腰腹与腿部；用户要求更严格遮盖时以其要求为准。
- 产品镜头应让目标服装可辨识；搭配不得遮住需要展示的关键细节。
- 默认不添加屏幕文字、字幕或价格，除非用户要求。
- 背景、服装、头巾等改变权限按当前任务决定，不把历史任务的改变权限套到新任务。

## 5. [AUTHORED EXAMPLE] 参考图生成框架

```text
Use the supplied references with separate roles:
Image 1 defines the exact garment.
Image 2 defines the model's facial identity and specified hijab styling.

Create a [visual style] Malaysian fashion video.
The model wears [confirmed product description].

She [one clear, natural action sequence].
Use [shot size and angle]. The camera [specific movement].
Keep [the relevant garment area] clearly visible throughout.

Location: [specific environment].
Lighting: [specific natural or controlled light].
Audio: [exact dialogue and/or requested ambient sound].

Preserve the garment's [confirmed colour, silhouette and visible construction details].
Maintain the referenced facial identity and body proportions.
Maintain [the user's coverage requirements].
Only change [authorized changes].
Do not add unreferenced garment details.
[Requested text/subtitle policy.]
```

## 6. [AUTHORED EXAMPLE] 首帧动画

```text
Begin from the supplied start image.
The model gently shifts her weight, takes two relaxed steps, then pauses.
Use a steady full-body shot with a subtle backward camera movement.
Maintain the starting image's garment, character, setting and lighting.
Keep the trousers and their silhouette visible.
Audio: soft footsteps and room ambience. No dialogue or music.
```

这是自编示例；用户需要换背景或机位时，相应调整保留列表。

## 7. [AUTHORED EXAMPLE] 首尾帧过渡

```text
Start from the supplied first frame and finish at the supplied last frame.
Between them, the model turns naturally toward her final pose,
using a continuous movement that connects the two body positions.
Use a smooth, continuous shot.
Maintain the same garment and character during the transition.
Avoid introducing an intermediate outfit or an extra person.
```

若首尾帧服装、人物或空间相互冲突，先说明冲突，不把冲突隐藏在提示词中。

## 8. [AUTHORED EXAMPLE] 只修改头巾

```text
Edit the supplied video.
Change only the woman's hijab to [requested colour, material and wrapping style].
Match its folds, shadows and movement to the source footage.
Preserve her face, body proportions, clothing, actions, camera movement,
background, lighting, timing and audio.
Do not add text or other accessories.
```

若用户同时要求 inner、遮颈或遮胸，把这些明确加入允许修改区域；不要声称模型保证其余区域完全不变。

## 9. [AUTHORED EXAMPLE] 后续修正

```text
Refine the current result: restore the trousers' original khaki shade
using the product reference. Preserve the current action, camera,
model identity, background and audio.
```

只处理已观察到的偏差，不重新写一套无关场景。

## 10. [CODEX RULE] 输出前检查

- 任务模式与输入是否一致？
- 每份参考的分工是否明确且真实？
- 产品细节是否来自图片或用户资料？
- 动作、机位和光线是否互相兼容？
- 保留项是否与允许修改项冲突？
- 口播、音乐与文字是否经过用户要求？
- 是否把自编建议或 Veo 规则误写成 Omni 官方规则？
- 是否承诺了提示词无法保证的结果？

## 11. 给 Codex 的读取指令

```text
Read this file as an evidence-labelled prompt-writing reference.
Use OFFICIAL SUMMARY as sourced guidance, CODEX RULE as authored workflow,
and KM RULE as user-specific requirements.
When asked for Omni Flash 1.1 prompts, identify the input mode and write
one paste-ready prompt grounded in the supplied references.
Do not present this document or its examples as a Google-authored manual.
Do not add API explanations, Flow tutorials or unsupported capability claims.
```

## 12. Google 官方来源

S1 — Create videos in Google Flow
https://support.google.com/flow/answer/16353334?hl=en
相关章节：Create videos with the standard Google Flow prompt box；
Add start & end frames；Add visual references；Best practices & advanced tips。

S2 — Edit videos & build scenes in Google Flow
https://support.google.com/labs/answer/16935718?hl=en
相关章节：Edit & refine video clips；Step 3: Edit your video。

S3 — Learn about Google Flow models & supported features
https://support.google.com/flow/answer/16352836?hl=en
相关章节：Supported features in Gemini Omni Flash 1.1。

这些是官方网页链接，本文件是概括与自编规则，不是网页全文备份。

