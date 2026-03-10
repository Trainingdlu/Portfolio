# Portfolio | Trainingcqy

参考 Material Design 3 风格构建的响应式个人主页，用于展示项目与摄影作品。

**在线访问**: [https://trainingcqy.com](https://trainingcqy.com)

## 项目简介

纯静态个人网站，包含主页、项目展示、摄影图库和视觉效果页，适配桌面端与移动端。

### 核心特性

- **浅色/深色主题** — 通过 CSS Variables + `prefers-color-scheme` 自动适配
- **响应式导航** — 桌面端顶部导航栏，移动端底部导航栏
- **Canvas 粒子背景** — 首页使用 Canvas 绘制粒子效果，响应鼠标移动
- **项目卡片** — 悬浮效果、技术栈标签、Live Demo / Source 链接
- **瀑布流图库** — CSS Multi-column 实现
- **基础 SEO** — Meta Description / Open Graph / Canonical / Sitemap / Robots.txt
- **图像处理脚本** — Python 脚本批量转 WebP + 缩放 + 增量命名

## 技术栈

| 分类 | 技术 |
|---|---|
| **前端核心** | HTML5, CSS3 (Flexbox / Grid / CSS Variables / Media Queries) |
| **设计参考** | Material Design 3 风格, Google Material Symbols 图标 |
| **字体** | Google Fonts (Roboto, Great Vibes) |
| **视觉特效** | Canvas API, Three.js, Vanta.js |
| **工程自动化** | Python 3 (Pillow) |
| **部署托管** | Cloudflare Pages (GitOps 自动构建 + CDN) |
| **SEO** | Sitemap XML, Robots.txt, Open Graph Protocol |

## 目录结构

```text
.
├── index.html          # 首页 — 个人概览
├── projects.html       # 项目展示 — 卡片布局
├── gallery.html        # 摄影图库 — CSS 瀑布流
├── visuals.html        # 视觉效果 — Vanta.js Waves 动态背景
├── style.css           # 公共样式 — CSS 变量 / 导航组件 / 响应式
├── convert_img.py      # 图像处理脚本 — JPG/PNG → WebP 转换 + 缩放
├── img/                # 静态图片资源 (WebP 格式)
│   ├── avatar.webp     # 头像
│   ├── favicon.png     # 站点图标
│   └── photo_*.webp    # 摄影作品 (26 张)
├── music/              # 音频资源
│   └── Rain after Summer.mp3
├── sitemap.xml         # 站点地图
├── robots.txt          # 爬虫协议
├── LICENSE             # MIT License (代码部分)
├── .gitignore          # Git 忽略规则
└── README.md           # 本文档
```

## 页面架构

```
index.html (首页)
  ├── Canvas 粒子背景
  ├── Rain after summer
  └── Chip 导航 (科技前沿 / 项目 / 摄影 / 联系)

projects.html (项目)
  ├── AI-Driven Tech News Intelligence
  ├── Personal Digital Hub
  └── Python Alien Invasion Game

gallery.html (摄影)
  └── CSS Multi-column 瀑布流

visuals.html (视觉效果)
  └── Vanta.js Waves (Three.js + 色相循环 + 陀螺仪适配)
```

## 图像处理自动化

`convert_img.py` 用于自动化处理静态图片资源：

1. **格式转换** — 将 `img/` 下的 JPG/PNG 自动转为 WebP
2. **尺寸限制** — 超过 1600px 宽度的图片自动等比缩放
3. **增量命名** — 自动检测现有编号，从最大编号 +1 开始命名
4. **自动清理** — 转换成功后删除原图

**使用方法**:

```bash
pip install Pillow
python convert_img.py
```

## 本地开发

```bash
# 克隆仓库
git clone https://github.com/Trainingdlu/Portfolio.git

# 本地预览 — 直接用浏览器打开 index.html 即可
```

## 部署

本项目通过 **Cloudflare Pages** 托管，采用 GitOps 工作流：

推送至 `main` 分支 → 自动构建 → CDN 分发至 [trainingcqy.com](https://trainingcqy.com)

## 版权说明

- **源代码** (HTML / CSS / JS / Python) — 基于 [MIT License](LICENSE) 开源
- **内容与作品** (文字 / `img/` 目录下的摄影作品) — © 作者所有，保留所有权利，未经允许禁止转载或商用