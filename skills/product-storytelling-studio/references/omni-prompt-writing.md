# Omni 提示词写法：输入模式、动作和保留项

## 来源与适用范围

2026-10-17 根据用户提供的 `OMNI_FLASH_1.1_PROMPT_WRITING.md` 整理。原文件自述核验日期为 2026-10-03，性质是助手编写的官方网页摘要、工作规则和 KM 业务要求，非 Google 发布的独立手册。本引用保留这一界限：下面的方法是经用户要求采用的本地写作指导，不宣称是 Omni 的强制语法或经验证的生成能力。

原文标签 `[OFFICIAL SUMMARY]` 表示它对网页的概括，`[CODEX RULE]` 表示自编规则，`[KM RULE]` 表示用户业务要求，`[AUTHORED EXAMPLE]` 表示自编示例。下面的示例同样属于自编写法。此次更新只吸收提示词结构，未重新核验原文关于模型功能、轮数、音频、时长、费用的说法；实际执行仍按当前平台核实。

原文件列出的来源（查询当前能力时再读取，不把链接本身当作证据）：

- S1，Create videos in Google Flow：https://support.google.com/flow/answer/16353334?hl=en
- S2，Edit videos & build scenes in Google Flow：https://support.google.com/labs/answer/16935718?hl=en
- S3，Learn about Google Flow models & supported features：https://support.google.com/flow/answer/16352836?hl=en

## 先匹配真实输入

| 当前实际素材与任务 | 提示词重点 | 不能假设的输入 |
|---|---|---|
| 只有文字，从零生成 | 主体、商品已知外观、场景、动作、镜头、光线、声音 | 未上传的图片、人物库或声音绑定 |
| 商品图＋人物参考图 | 按实际顺序说明哪张定义商品、哪张定义脸与指定头巾；再写穿着后的行动 | 商品图中的另一个人物就是目标人物；照片能确认所有材质／功能 |
| 一张已合成的首帧，做动画 | 从该图现状开始，写接下来的动作和必要保留项 | 原始商品图和肖像也已经同时传入平台 |
| 真实首帧＋尾帧 | 两帧之间可实现的动作、转向或过渡 | 通过服装／人物／空间冲突的帧也能无故连续 |
| 已有视频，需要编辑 | 修改对象、区域、目标及其余需保留的部分 | 未提供的视频、未授权的背景／声音／身份更换 |

以实际上传顺序编号；输入换了顺序就同步改提示词。只有用户明确调用且真实可用的人物参考才能绑定到角色名；不从学习文档里的 Farah、Hawra、Alyasofea 等示例名字推定已有人物素材。素材名称在提示词中只是说明，不会自动完成平台上传或绑定。

## 一份可直接粘贴的提示词

每幕优先提供一个完整代码块，内部用清楚的自然语言按以下关系组织，不必机械加入所有标题：

1. 从实际首帧／参考开始，说明初态；无参考时直接描述主体与场景。
2. 写一段与时长相容的动作序列，动作之间有接触、受力、视线和姿态的连续关系。
3. 写景别、角度与具体机位变化。两镜就说明一次切镜，不能同时要求整幕一镜到底。
4. 写确实需要新增或保持的地点、光线和视觉特征。首帧已体现的风格以保持为主，不重新搭建相互冲突的场景。
5. 写逐字对白、说话者、语言、语气和必要时间关系，以及环境声／配乐需求。
6. 保留少量关键商品、人物与画面约束；排除当前任务明确不需要的字幕、标识或多余细节。

把时长和比例作为创作设置提示，不能说写进正文即已设置界面。时间码用于必要的对白、反应或切点；不必把每次眨眼都编成密集时间指令。用户明确要求的幕数、镜头数、时长、电影观感和输出范围仍然有效。

商品锁定只使用确认可见的颜色、结构和细节。只见纹理时不能推断面料成分。人物身份与遮盖方式沿用实际参考和当前用户要求；KM 的 Muslimah 穿搭要求适用时保留头发、颈部、胸口、手臂、腰腹与腿部遮盖，不从商品照片里另一人的露肤搭配改写目标模特。搭配不能遮住本镜头要展示的细节。除非用户要求，不新增屏幕文字、价格或字幕。字幕与发布 Caption 分别处理。

## 自编写法示例

### 已提供首帧：两镜动画

```text
Begin from the supplied start image. The woman is seated, eyes lowered, with her right hand on the desk and her left hand resting on her thigh.

During the first shot, she raises her eyes toward the doorway, straightens and smiles. She says in excited Malaysian Malay, "Dekat mana?!"

Cut once to a wider front three-quarter view. She stands, turns toward the side cabinet, closes her left fingers around the short bag handle and lifts the bag clear of the surface. End with the bag hanging beside her left thigh, right hand empty.

Maintain the starting image's face, pink hijab, cream long-sleeved top, deep navy asymmetric overlay and its three silver circular details. Keep the existing cool window light, warm desk lamp and neutral garment colour.
Audio: only the visible woman's quoted line, soft office ambience and light chair movement. No other speech or music. No added text or graphics.
```

这个示例针对已经决定单独处理另一条音轨的情况，不能直接套用为所有故事都只允许一个说话人；若保留多说话人，按实际故事分别标注。

### 商品图＋人物参考：先分工

当实际上传顺序是产品在前、人物在后时，开头可以写：

```text
Use the supplied references with separate roles. Image 1 defines the navy garment's visible colour, asymmetric overlay and three silver circular details. Image 2 defines the woman's face and specified pink hijab styling. Dress that woman in the referenced garment with the requested cream long-sleeved top.
```

后接具体动作、场景、镜头和声音；不能停在参考锁定句，也不能在只上传首帧时沿用这段开头。

### 首尾帧与定向编辑

首尾帧描述从起始姿态到最终姿态的自然运动，先检查两帧的人物、服装和空间关系。编辑已有视频时，先写“改变哪里”，再写“保留什么”。如果用户只要改头巾颜色，需保留其他衣着、动作、镜头与音轨；若用户也要改音轨，就相应移除“保留原音轨”的冲突要求。

只对已观察到的偏差做针对性修正；“保持人物／产品”是目标，不是逐像素保证。不要因采用这个写法就自动发起生成、上传、编辑或付费重试。

## 说话人问题与后期音轨

逐字对白需要说明：说话者是谁、是否在画面里、听者何时反应，哪些台词不应对口型。用稳定的角色标识，让两条发言在时间上可区分。上述标注属于写作目标，未实测就不能保证 Omni 一定准确分配。

用户反馈画外音被主角说出时，可在保留故事的前提下，把视频生成与画外音制作分开：视频提示词只包含本次要生成的台词，另一句放入单独的后期音轨说明，标明插入点及主角闭嘴倾听的区间。不要把待后期添加的逐字台词又塞进视频生成提示词，造成另一条可被读出的内容。

后期音轨只是出现说话人混淆时的一种项目补救。未实际生成、录制和混音，交付状态必须写清“提示词／后期安排”，不能称为已合成完成。这不是原参考文件提供的多角色控制验证，也不是模型官方要求。音轨的实际时长会影响反应与对白的入点，制作后再校准。
