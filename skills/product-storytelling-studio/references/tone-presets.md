# Tone：24 种语气预设

## 用途和来源

用于角色对白、画外旁白及对应表演说明。2026-10-17 根据用户对语气选择的需求扩充：保留原有 Natural / Emosi / Puitis / Komedi，新增 20 种本地创作预设。以下代码用于本 Skill 的名称匹配，不是 Studiova 的 API 字段或新观察到的网站选项；历史 option-catalog.json 的 12 组、107 项计数不因此改变。

## 如何选择与落实

- 接受中文、英文、下表代码或自然语言。用户明确的表达优先，菜单不是限制。用途明确为带货、商品销售推广且未指定语气时，按本用户偏好默认“亢奋／高能兴奋”：第14项 `excited_celebratory` 配强情绪；其他任务未指定时沿用 Natural，不因服装颜色或真人外观推断人格。
- 一般选一个主语气。用户要混合时，可再选一个辅助语气并写清“主／辅”或“带一点……”，避免把互相冲突的表演同时塞进同一句。允许分幕改变，但要说明情绪转折由什么事件造成。
- 情绪强度可以写轻／中／强；带货默认强，其他任务未指定时采用适度表达。亢奋落实为明亮上扬的语调、清楚重音、兴奋笑容和自然手势，仍需保留换气与展示时间。已指定情绪转折的故事保留铺垫，在分享／推荐或高潮段采用亢奋。语气不等于音色、说话速度、镜头节奏、皮肤质感或电影观感；“温柔”不自动变成耳语，“有活力”不自动加速，“浪漫”不自动加入粉红灯或爱情关系。
- 在对白中改变措辞和句式，在声音说明中写重音、气息与停顿，在人物画面中给少量相应表情。不要仅在提示词末尾添加一个语气标签。
- 例句只演示表达，需按实际商品、事件和语言重写；不默认逐字套用。笑声、叹气与停顿占用时长；减少台词以容纳它们。纯静态图片只描述可见表情，不声称已实现声音。
- 所有语气沿用商品事实规则；自信、热情和强势不能变成虚假功效、假证言、假稀缺或购买压力。克制浪漫的关系与互动服从用户故事，悬念应按时揭示具体内容。

## 完整菜单

| 编号 | 语气／本地代码 | 措辞、声音与表情 | 马来西亚马来语示例（虚构角色台词） |
|---|---|---|---|
| 01 | 自然日常 Natural / `natural` | 简短口语，正常起伏，像平常说话；不刻意表演 | Hari ni saya padankan navy dengan pink. |
| 02 | 情绪叙事 Emosi / `emosi` | 让具体事件引出情绪变化；先确认是期待、难过或喜悦，再安排停顿与反应 | Tadi masih ragu-ragu. Sekarang, saya dah bersedia. |
| 03 | 诗意留白 Puitis / `puitis` | 少量意象和含蓄句式，句尾留白；不堆砌抽象比喻 | Cahaya petang jatuh perlahan. Saya pun melangkah keluar. |
| 04 | 轻松喜剧 Komedi / `komedi` | 围绕故事事件建立笑点，铺垫后停一拍再反应 | Baju dah siap. Saya pula masih cari kunci. |
| 05 | 闺蜜聊天 Friend Chat / `friend_chat` | 像跟熟悉朋友分享；有自然称呼、回应感和轻微侧头 | Korang tengok, saya suka padanan macam ni. |
| 06 | 温柔体贴 Gentle / `gentle_caring` | 柔和重音，给对方空间，轻声但清楚；不强制耳语 | Tak perlu tergesa-gesa. Kita pilih satu-satu. |
| 07 | 明亮俏皮 Bright & Playful / `bright_playful` | 轻盈语调，短促的小重音，带一点调皮微笑；不需要完整笑话 | Navy dengan pink? Eh, masuk juga rupanya! |
| 08 | 冷静沉着 Calm / `calm_composed` | 起伏克制，完整清楚地说完，呼吸稳定；保留必要信息 | Saya pilih yang ini. Sekarang, boleh keluar. |
| 09 | 自信利落 Confident / `confident_direct` | 选择明确，句尾收稳，少犹豫词；姿态自然 | Saya pilih navy. Itu padanan saya hari ini. |
| 10 | 专业讲解 Professional / `professional_clear` | 指向具体细节，逻辑清楚，关键词适度重读；不假装专家资历 | Perhatikan lapisan depan dan tiga perincian bulat ini. |
| 11 | 真诚走心 Heartfelt / `sincere_heartfelt` | 直接表达本场景中的动机与在意之处，少修辞、重真诚；不编造参考人物经历 | Saya nak tampil kemas untuk pertemuan hari ini. |
| 12 | 好奇发现 Curious / `curious_discovery` | 问句或观察引出发现，语调轻扬，视线跟随可见细节 | Eh, perasan tak bahagian depan dia berlapis? |
| 13 | 悬念逗引 Teasing / `suspense_tease` | 短暂延迟揭示，压低一点重音，揭示后恢复自然；不能只有空钩子 | Tunggu… tengok bila saya kemaskan bahagian depan. |
| 14 | 兴奋分享 Excited / `excited_celebratory` | 明显喜悦与较大语调幅度，给反应留时间；不自动大喊或加快 | Ha, ini padanan yang saya nak tunjuk tadi! |
| 15 | 怀旧感怀 Nostalgic / `nostalgic_wistful` | 回望语气、轻柔停顿；回忆须来自用户设定或明确虚构故事 | Suasana kedai ni buat saya teringat petang dulu. |
| 16 | 克制浪漫 Romantic / `romantic_subtle` | 对明确对象的含蓄期待，轻微微笑，话不说满；不自动变成诱惑式耳语 | Saya sampai awal sikit. Nak tunggu awak di sini. |
| 17 | 简短留白 Minimal / `restrained_minimal` | 减少台词，让动作承担信息；每句话有目的，停顿占比高 | Dah siap. Jom. |
| 18 | 鼓励激励 Encouraging / `inspiring_encouraging` | 承认具体困难，再给可执行的小行动；语气向前，不承诺必然成功 | Tak perlu tunggu sempurna. Cuba satu langkah dulu. |
| 19 | 优雅从容 Refined / `refined_elegant` | 用词简洁而精确，吐字清楚，轻微停顿和稳定姿态；不等同压低音高 | Cukup satu perincian untuk melengkapkan padanan ini. |
| 20 | 坦率随性 Candid / `candid_casual` | 自然自我修正、小犹豫或真实当下反应，保留即兴感；不编造使用体验 | Hmm, yang ni… ya, saya pilih yang ni. |
| 21 | 鲜明有态度 Bold / `bold_assertive` | 强调个人立场与选择，重音明确；不贬低观众或制造购买压力 | Ini pilihan saya. Saya suka gayanya begini. |
| 22 | 温暖邀请 Welcoming / `warm_inviting` | 面向对方、主动邀请参与，语调开放，微笑与短停顿 | Jom, kita tengok padanan ni sama-sama. |
| 23 | 共情安抚 Reassuring / `empathetic_reassuring` | 先回应情境里的顾虑，再给具体下一步；避免空泛保证 | Kalau masih tak pasti, cuba tengok dari depan dulu. |
| 24 | 干脆有活力 Energetic / `brisk_energetic` | 短句、明确动作动词、清楚节拍；动力来自推进事件，不靠高音量 | Ambil beg, semak kunci, jom keluar! |

## 容易混淆的选择

- Natural 是普通日常表达；Friend Chat 增强对熟悉观众的回应感；Candid 保留当下犹豫和自我修正。
- Komedi 需要铺垫与笑点；Bright & Playful 可以只靠轻盈反应；Teasing 靠信息揭示。
- Calm 可以解释完整信息；Minimal 主动减少说话；Refined 注重吐字和从容的表达。
- Confident 清楚表达选择；Bold 加强个人立场；Professional 重点是细节与逻辑。
- Gentle 是柔和说话；Reassuring 要回应一个顾虑；Welcoming 重点是邀请对方参与。
- Emosi 是按事件选择情绪的通用入口；Heartfelt 重在真诚动机；Romantic 需要故事里明确的期待对象。

## 调用示例

“语气选闺蜜聊天，带一点明亮俏皮，情绪强度轻。马来西亚马来语，自然语速。她发现前摆挡住圆环时轻笑，整理后再向镜头分享。不要笑场或连续大笑。”

“语气选优雅从容，台词简短。王家卫电影观感，保留商品原色。以视线和停顿推进故事，只有最后一幕说一句话。”

“前两幕好奇发现，看到完整造型后转为兴奋分享；转折由画面里的造型完成触发。维持同一音色，不把情绪变化写成换了配音演员。”
