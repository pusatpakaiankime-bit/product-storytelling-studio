# 上班电量 1%，听到吃饭瞬间满格

## 实际生成的三张首帧

| 第1幕 | 第2幕 | 第3幕 |
|---|---|---|
| ![第1幕](images/scene-01-office-tired.png) | ![第2幕](images/scene-02-before-invitation.png) | ![第3幕](images/scene-03-mamak-arrival.png) |

[商品参考](inputs/product.jpg) · [人物参考](inputs/model.png)


TikTok 发布文案见本文末尾，或同目录 tiktok-caption.txt；文案用于发布，不烧录进画面。

## Story

她在下班前累得只想回家，坐在办公桌旁低声说“Penat… nak balik terus.”。正准备结束一天，画外闺蜜一句“Jom makan!”让她瞬间抬眼、坐直，兴奋追问“Dekat mana?!”。她站起，拿上小包。时间跳到附近 Mamak 餐厅，她已精神十足地来赴饭局，向画外朋友笑着说：“Penat kerja. Makan tak penat!”。最后停在她的笑容，完成由疲惫到兴奋的反差。

## 采用参数

用户指定：Cinematic；iPhone / Editorial Realism；wong_kar_wai；Commercial / TVC 打工人反差喜剧；Realistic 皮肤；3 幕 × 8 秒 = 24 秒、每幕 2 镜，共 6 个计划镜头；9:16；马来西亚马来语对白。前段缓慢留白，邀请触发提速，结尾留笑容。办公室冷窗光配暖台灯，餐厅暖光配傍晚冷色背景，中性补光保留商品深蓝色。闺蜜只用画外声。未指定目标视频模型或实际生成平台。

为执行补充：小型无品牌办公室、附近无品牌 Mamak 餐厅；新增米白色短提把小包、办公桌和已合上的笔记本电脑作为剧情道具。主角穿参考人物的粉色头巾与浅色长袖风格，搭配浅前塞的奶油色针织上衣。未要求配乐，本包不指定配乐；保留必要环境声。

## 商品与人物依据

- 图 1 只锁定商品下装：深蓝、贴合裤身上方的不对称裙式叠片、画面左侧上部斜向排列的三枚银色圆环、左／中部较长垂落尖折片、右侧较短斜向下摆。圆环功能、面料成分、弹力、舒适度、尺码和价格未确认，不作为卖点。
- 图 2 锁定人物外观、粉色头巾与浅色长袖穿搭方式；不沿用商品图中另一位人物的脸、头发或露腹短上衣。
- 参考只展示有限角度，不把生成的背面和裤脚称为准确商品结构。视频的商品镜头聚焦可核对的正面和可见裤腿。

## 分镜

| 幕与作用 | 全片时间 | 幕内镜头及动作 | 对白及起点 | 首尾状态 |
|---|---|---|---|---|
| 1 疲惫铺垫 | 0–8 秒 | 0–4 秒：从首帧缓慢推进，轻叹气、肩膀微落；4–8 秒：切稍宽同侧机位，右手略收至桌边，仍坐着。 | 主角，约0.8秒起：Penat… nak balik terus. | 起：坐姿疲惫、右手桌面、左手腿上；终：仍疲惫坐着，包留柜上。 |
| 2 邀请触发反差 | 8–16 秒 | 0–3.4 秒：闺蜜画外邀请后，主角抬眼、坐直、惊喜追问；3.4–8 秒：切宽景，起身、稍转向左侧柜子，左手握短提把再提包。 | 闺蜜，约0.3秒：Jom makan!；主角，约1.6秒：Dekat mana?! | 起：首帧仍然疲惫；终：站起、精神变亮、左手提包。 |
| 3 餐厅包袱 | 16–24 秒 | 0–4 秒：头至小腿景别，向画外朋友轻快走两步，展示叠片与圆环；4–8 秒：门框近景，停步说包袱，末尾留1.5–2秒笑容。 | 主角，约4.2秒：Penat kerja. Makan tak penat! | 起：已到餐厅门口、左手提包；终：笑容定住，不追加抢占时间的入座或吃饭动作。 |

对白意思：第一幕“累了……想直接回家”；第二幕“走，吃饭去！”“哪里？！”；第三幕“工作会累，吃饭不会！”

## 连续性

第一、二幕的首帧都在邀请之前，因此两张疲惫坐姿相近。第二幕的画外邀请之后才进入亢奋惊喜；不能拿第三幕的笑脸代替第二幕开头。小包在第一幕和第二幕开头留在主角左后侧柜面，第二幕通过右手扶桌起身→转向柜面→左手触及提把→握稳→垂直提离柜面→垂至左侧完成拿取，第三幕继续左手携带。双手没有手机或食物。办公室至餐厅是明确的时间／地点省略剪辑。

## 实际生成记录与检查

本包已用 Codex 内置图像工具生成三张静态首帧，原文件路径和每次实际提交提示词保存在 production-record.json。工具未提供界面报价或积分余额，未据此编造价格。视频尚未提交；下面的英文内容均为 Proposed Video Prompt。

已目视核对三张图：人物粉色头巾、浅色长袖与主色连续，三枚圆环均可见，叠片方向保留。第一、二张有冷窗光、暖台灯和暗门框前景；第三张转为暖光餐厅与蓝色暮色。深蓝商品仍有可辨色的中性补光。手部、画面边缘及包在当前静态帧中可读；但无法用静态图确认后续站起、拿包、走路、对口型或声音执行。

局限：人物外观为生成演绎，脸部细节和皮肤光泽有修饰；裙片下缘、坐姿产生的褶皱及折片比例与原商品照片存在差异，不能视为版型级复刻。商品准确外观以原参考图为准。为保留展示，电影观感采用边缘遮挡、局部冷暖光和停顿，不用强色偏覆盖商品。

## 视频提示词使用

每段分别上传对应首帧，并复制 video-scene-01/02/03.txt。计划为每段8秒两镜；不同平台对切镜和时间码的服从程度需实际确认。若无法稳定执行，可按写明的切点分别制作后剪辑；先核对目标平台再实际生成。

## 第 1 幕：上班电量耗尽

```text
PROPOSED VIDEO PROMPT — SCENE 1
Planned duration: 8 seconds, exactly 2 planned shots.
First frame: scene-01-office-tired.png.
Vertical 9:16, photorealistic iPhone editorial proportions with Wong Kar-wai-inspired foreground occlusion, intimate framing, warm-cool practical-light separation and expressive pauses. Preserve the supplied woman's facial appearance, pale blush-pink hijab drape, opaque cream long-sleeved crew-neck knit with shallow front tuck and real skin microtexture. Preserve the deep navy fitted trousers under the asymmetric skirt-like front overlay: THREE small silver circular rings diagonally down the viewer-left upper front, long pointed draped panel on viewer-left/center, shorter diagonal hem on viewer-right. Neutral soft fill keeps the hero garment NAVY, not black, purple, green or cobalt. Do not mirror the product. Keep occlusion at image edges, never over the detail being shown. No text, subtitles, battery graphics, watermarks or extra visible people. Do not invent product performance, rear construction or trouser-hem details.
Initial state: the woman is seated and slightly slumped in the charcoal office chair. Eyes down, lips relaxed, no smile. Right hand empty on the desk beside the already-closed laptop, left hand empty on her left thigh. The ivory handbag with its short arched handle stays upright on the cabinet behind and to her LEFT, viewer-right. Cool blue dusk window and warm amber desk lamp stay in the positions shown.
0.0–4.0 seconds — SHOT 1: begin with the supplied composition. An almost imperceptible camera push-in; her shoulders sink slightly with one quiet exhale. At 0.8 seconds she says, softly and flatly in natural Malaysian Malay, "Penat… nak balik terus." Her eyelids remain heavy. Keep the visible three silver rings and navy folds intact.
4.0–8.0 seconds — SHOT 2: clean cut to a slightly wider view from the same side of the doorway. She pauses, draws her empty right hand slightly toward the desk edge and stays seated. Her left hand remains on her thigh. The already-closed laptop does not reopen or require another closing action. Finish with the same low-energy pose and downward gaze needed for scene 2.
Sound: quiet office air-conditioning hum, slight chair or clothing rustle. Only her line is spoken here; the friend's invitation belongs to scene 2. No music.
End state: tired and still seated, hands empty, bag still on the cabinet. No standing, grabbing the bag or sudden smile in this clip.
```

## 第 2 幕：一句 Jom makan，瞬间满格

```text
PROPOSED VIDEO PROMPT — SCENE 2, REVISION 2 — SINGLE SPEAKER
Planned duration: 8 seconds, exactly 2 planned shots.
First frame: scene-02-before-invitation.png. She begins TIRED as pictured. This generation contains ONLY the visible woman's speech; a separate audio cue will be added in editing.
Vertical 9:16, photorealistic iPhone editorial proportions with Wong Kar-wai-inspired foreground occlusion, intimate framing, warm-cool practical-light separation and expressive pauses. Preserve the supplied woman's facial appearance, pale blush-pink hijab drape, opaque cream long-sleeved crew-neck knit with shallow front tuck and real skin microtexture. Preserve the deep navy fitted trousers under the asymmetric skirt-like front overlay: THREE small silver circular rings diagonally down the viewer-left upper front, long pointed draped panel on viewer-left/center, shorter diagonal hem on viewer-right. Neutral soft fill keeps the hero garment NAVY, not black, purple, green or cobalt. Do not mirror the product. Keep occlusion at image edges, never over the detail being shown. No text, subtitles, battery graphics, watermarks or extra visible people. Do not invent product performance, rear construction or trouser-hem details.
Initial state: same office, same dusk and lamp light, chair, closed laptop and cabinet as the supplied image. Right hand on the desk, left hand on her thigh, eyes lowered. The same small structured ivory handbag with one SHORT arched top handle is on the cabinet behind her LEFT side, viewer-right, not in either hand.
0.0–3.4 seconds — SHOT 1: hold the first-frame angle. From 0.0 to 1.1 seconds she stays seated, tired, with her LIPS CLOSED; keep this interval free of all speech. At about 1.1 seconds she raises her eyes toward the office doorway, eyes widen, torso straightens and a delighted grin appears, as a listening reaction to a cue that will be added later. From about 1.6 seconds, ONLY the visible woman speaks, in bright energized Malaysian Malay: "Dekat mana?!" Give "mana" playful emphasis. This is the ONLY spoken line in the generated clip. She finishes by 2.8 seconds, closes her lips and takes a delighted breath. No additional voices, invitation lines, narration or self-question-and-answer dialogue.
3.4–8.0 seconds — SHOT 2: cut to a wider three-quarter FRONT angle of the same office, keeping cabinet and chair positions coherent. She uses her right palm on the stable desk edge to assist one natural rise from the chair. Once upright, she makes a small quarter-turn toward the cabinet on her LEFT. Her left hand reaches the apex of the short bag handle; fingers curl around it and thumb secures the grip. ONLY AFTER contact and grip, lift the bag vertically until its base clears the cabinet, then let it settle beside her left outer thigh. Her right hand releases the desk and remains empty. If needed, allow one small aligning step, but no exit or door-opening action.
Sound: quiet office ambience, chair creak and light bag movement. The ONLY generated speech is the visible woman's exact line specified above. Leave 0.0–1.1 seconds free of speech. No music or sound-effect power-up.
End state: standing with brighter posture, same outfit, same ivory bag held by its short handle in her LEFT hand. Keep the handle short, no shoulder carry, no hand switching, no bag appearing before she grips it. Cut to scene 3 as an explicit elapsed-time/location change.
```

## 第 3 幕：吃饭永远有电

```text
PROPOSED VIDEO PROMPT — SCENE 3
Planned duration: 8 seconds, exactly 2 planned shots.
First frame: scene-03-mamak-arrival.png.
Vertical 9:16, photorealistic iPhone editorial proportions with Wong Kar-wai-inspired foreground occlusion, intimate framing, warm-cool practical-light separation and expressive pauses. Preserve the supplied woman's facial appearance, pale blush-pink hijab drape, opaque cream long-sleeved crew-neck knit with shallow front tuck and real skin microtexture. Preserve the deep navy fitted trousers under the asymmetric skirt-like front overlay: THREE small silver circular rings diagonally down the viewer-left upper front, long pointed draped panel on viewer-left/center, shorter diagonal hem on viewer-right. Neutral soft fill keeps the hero garment NAVY, not black, purple, green or cobalt. Do not mirror the product. Keep occlusion at image edges, never over the detail being shown. No text, subtitles, battery graphics, watermarks or extra visible people. Do not invent product performance, rear construction or trouser-hem details.
Initial state: the woman has arrived at the open entrance of an unbranded Malaysian neighbourhood mamak restaurant, early evening. Warm amber interior lights, blue dusk street and distant restrained red background accent. The camera observes through the dark blurred door edge. She is standing and looking toward the off-camera friend on image LEFT with a small lively smile. Her LEFT hand, image RIGHT, holds the same small structured ivory handbag by its SHORT arched handle beside her left outer thigh; right hand empty. No phone or food in either hand.
0.0–4.0 seconds — SHOT 1: continue the supplied head-to-shin composition, slight tracking movement as she takes two unhurried steps toward the friend near the entrance. Her energized posture contrasts with scene 1. Keep a near-front three-quarter view that clearly shows the THREE silver rings, asymmetric navy overlay and visible trouser legs. Bag swings only a few centimetres with natural gravity, remaining in her LEFT hand at the outer side. The garment moves subtly with the steps, never reshaping or changing colour.
4.0–8.0 seconds — SHOT 2: cut to an intimate chest-up near-front view framed by the doorway, warm light on one side and cool dusk behind. She stops, looks at the off-camera friend on image LEFT and says in playful Malaysian Malay from about 4.2 seconds, "Penat kerja. Makan tak penat!" Pause lightly after "kerja", emphasize the playful contrast, then give a short laugh. Hold on her genuine smile for the final 1.5–2 seconds.
Sound: subdued mamak room ambience, faint dishes and distant traffic without intelligible additional dialogue. No music.
End state: the outing has begun; camera holds her smile, consistent with the requested ending. No additional entrance action after the final smile, no visible friend, no purchase slogan or claimed product benefits.
```


## TikTok Caption

Baru cakap penat… dengar “JOM MAKAN”, terus segar! 😭😂

Masa kerja: bateri 1% 🪫
Member ajak makan: terus 100% 🔋✨

“Penat kerja. Makan tak penat!” 🤭
Korang pun macam ni ke? Tag member yang sekali ajak, terus ON! 👇

#JomMakan #PenatKerja #CeritaOffice #OOTDMalaysia #NavyOutfit



## 第二幕修正：画外邀请单独后期配音

按用户反馈，原做法可能把邀请分配给画面中的主角，形成自问自答。第二幕改用 video-scene-02-v2-single-speaker.txt，只生成主角的 Dekat mana?!。闺蜜的 Jom makan! 按 scene-02-friend-voice-editing.txt 在后期单独加入，邀请期间主角闭嘴。该修正尚未重新生成或配音验证。
