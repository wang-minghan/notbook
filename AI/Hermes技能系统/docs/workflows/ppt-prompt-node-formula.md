# PPT 生图 Prompt 节点公式

适用范围：
- PPT 封面图
- 章节页主视觉
- 内容页插图
- 说明页 / 概念页配图

核心公式：

`[基础设定（画什么）] + [核心5维（怎么画）]`

---

## 一、基础设定（画什么）

1. **载体**
   - presentation cover
   - PPT illustration
   - section opener visual
   - slide background
   - editorial presentation asset

2. **主体**
   - 这张图的核心对象是什么
   - 例：AI workflow, data stream, abstract material form, product concept

3. **场景 / 关系**
   - 主体处于什么环境、与什么发生关系
   - 例：in a clean abstract spatial environment, surrounded by structured light ribbons

4. **风格 / 媒介**
   - 例：3D render, editorial illustration, cinematic abstract composition, minimal material design

5. **约束**
   - 例：clean negative space, restrained palette, no text in image, no poster layout, no collage

---

## 二、核心5维（怎么画）

1. **艺术形式**
   - 3D render
   - editorial illustration
   - material abstraction
   - UI/UX design language

2. **光影氛围**
   - cinematic lighting
   - soft studio lighting
   - subtle volumetric glow
   - premium contrast

3. **画质描述**
   - highly detailed
   - premium quality
   - refined material rendering
   - masterpiece
   - 8k

4. **构图视角**
   - asymmetrical composition
   - off-center focal point
   - clean negative space on the left/right
   - title-safe layout
   - 16:9-friendly composition

5. **风格指向**
   - Apple-like minimalism
   - Dribbble-grade polish
   - keynote-style corporate aesthetic
   - luxury editorial mood

---

## 三、封面图 Prompt 节点模板

### Positive Prompt
```text
editorial presentation title-slide background asset for [主题/主体], [场景/关系], [风格/媒介], [艺术形式], [光影氛围], [画质描述], [构图视角：强调大面积留白与标题安全区], [风格指向], clean, restrained, spacious, calm, contemporary, no text in image
```

### Negative Prompt
```text
text, letters, words, typography, caption, subtitle, watermark, logo, signage, label, poster, magazine cover, brochure mockup, collage, UI screenshot, infographic, chart, table, busy background, clutter, multiple focal points, centered subject, noisy texture, oversaturated colors, blurry, low quality, deformed
```

### 封面图额外要求
- 标题安全区必须清晰
- 主体不要占满整张图
- 尽量避免像“成品海报”一样自带版式感
- 不要默认蓝，除非用户明确要科技蓝

---

## 四、插图 / 配图 Prompt 节点模板

### Positive Prompt
```text
editorial presentation illustration asset for [主题/主体], [场景/关系], [风格/媒介], [艺术形式], [光影氛围], [画质描述], [构图视角：强调单一焦点和页面嵌入适配], [风格指向], clean, restrained, page-embed-friendly, low-distraction, no text in image
```

### Negative Prompt
```text
text, letters, words, typography, watermark, logo, signage, poster layout, magazine cover, brochure mockup, collage, UI screenshot, infographic, chart, table, fake interface, crowded composition, multiple focal points, noisy texture, low quality, blurry, deformed
```

### 插图额外要求
- 不一定保留超大标题区
- 但仍要避免文字污染
- 更强调单一视觉中心
- 更像“可放进页面的资产”，而不是“完成排版的海报”
- 可以借用海报感的构图节奏和电影感氛围，但不能带出标题、字幕、演职员表、标语等文字内容

---

## 五、当前建议参数（SDXL）

- width: 1216
- height: 704
- steps: 28~36
- cfg: 6.0~7.0
- sampler: dpmpp_2m
- scheduler: karras

适合目标：
- clean editorial look
- restrained modern PPT aesthetics
- generous white space
- clear title-safe or page-friendly composition
- 用于 PPT 封面或插图

---

## 六、使用原则

1. 先定载体，再定主体
2. 先做减法，再加细节
3. 先保证页面适配，再追求单图炫技
4. 封面图和插图要分开写 prompt，不要混用
