# 个人作品集网站 (Personal Portfolio)

基于 Google Material Design 3 (MD3) 设计规范构建的响应式个人主页，用于展示数据分析项目、代码工程能力及摄影作品。

**在线访问**: [https://trainingcqy.com](https://trainingcqy.com)

## 项目简介

本项目是一个静态网站，旨在通过工程化的手段管理个人数字资产。网站包含主页概览、项目展示卡片及瀑布流摄影图库，完全适配桌面端与移动端。

## 技术栈

- **前端核心**: HTML5, CSS3 (Flexbox/Grid, CSS Variables)
- **设计规范**: Material Design 3
- **工程自动化**: Python (Pillow 库) - 用于图像压缩与格式转换
- **部署托管**: Cloudflare Pages (自动构建与 CDN 分发)

## 目录结构

```text
.
├── index.html        # 首页 (个人概览/入口)
├── projects.html     # 项目展示页 (含 GitHub 跳转与弹窗交互)
├── gallery.html      # 摄影图库 (纯 CSS 瀑布流布局)
├── visuals.html      # 视觉效果
├── img.py            # 图像处理自动化脚本
├── img/              # 静态资源目录
└── README.md         # 项目说明文档
```


## 自动化工作流 (Image Optimization)

本项目包含一个 Python 脚本 (`convert_img.py`)，用于自动化处理静态图片资源。

**脚本功能**:
1.  **格式转换**: 将 `img/` 目录下的 JPG/PNG 图片自动转换为 WebP 格式。
2.  **尺寸限制**: 若图片宽度超过 1600px，自动按比例缩放以优化加载性能。
3.  **自动清理**: 转换成功后自动删除原图，保持仓库整洁。

**使用方法**:

1. 确保已安装 Python 依赖:
   ```bash
   pip install Pillow
   ```

2. 将原始图片放入 `img/` 目录。

3. 在项目根目录运行脚本:
   ```bash
   python img.py
   ```

## 本地开发与部署

1. **克隆仓库**:
   ```bash
   git clone https://github.com/Trainingdlu/Portfolio.git
   ```

2. **本地预览**:
   直接使用浏览器打开 `index.html`。

3. **部署**:
   本项目已连接 Cloudflare Pages。推送到 `main` 分支将触发自动构建并发布至 trainingcqy.com。

## 版权说明

本项目的源代码 (HTML/CSS/JS) 基于 **MIT License** 开源。
本项目的文字内容及 `/img` 目录下的所有摄影作品版权归作者所有，**保留所有权利**，未经允许禁止转载或商用。