# LDTGaffer

## English

LDTGaffer is a personal Gaffer toolset: presets, configs, startup scripts and boxed nodes.

**Requirements**

```Requires Gaffer 1.6.15.0 (Python 3)```

**Windows Notes (Paths)**

This toolset is intended to work on Windows as well. To avoid `.grf` reference loading issues and missing icons:

- Set plugin root (recommended):
  - `LDTGaffer=<absolute path to this repo>`
  - (Fallback supported) `LDTGAFFER=<absolute path to this repo>`
- Ensure icons can be found by Gaffer:
  - `GAFFERUI_IMAGE_PATHS` must include `<LDTGaffer>/icons`
- Ensure boxed nodes / references can be found:
  - `GAFFER_REFERENCE_PATHS` must include `<LDTGaffer>/resources/boxes`

> Tip: Paths passed into Gaffer reference loading are normalized to POSIX style (`/`) for cross-platform consistency.

**Credits / Origin**

- This repository was originally based on: https://github.com/ezequielmastrasso/LDTGaffer
- It has been upgraded for **Gaffer 1.6.15.0 compatibility** by **adu** (https://www.aducg.com).

> Note: Many tools here are based on examples shared on the Gaffer community mailing list : https://www.gafferhq.org/community/

### Folders and Variables
- Custom Variables (LDT resources)
- Bookmarks (LDT folders)

### LDT Menu
- Export Extension
- Node Annotations
- Register `includeInNavigationMenu`

### Node Defaults - `nodeGadget:color`
Same as Gaffer defaults, but paler colours easier on the eye.  
Except lights (yellow color), and filters (similar color to the filter plugs colors).

<img width="30%" src="docs/nodeGadget_color.png" alt="Node gadget colors" />

### Viewer
#### SceneView: Phong, Graph Editor Phong, and Diagnostics 2k/4k textures

<img width="31%" src="docs/sceneViewPhong.png" alt="SceneView Phong" /><img width="31%" src="docs/sceneViewPhong_2.png" alt="SceneView Phong 2" /><img width="32%" src="docs/gafferDiagnosticPatterns.png" alt="Diagnostics patterns" />

Phong courtesy of [Irene Hernández](https://www.linkedin.com/in/ireneher/).  
Cs and transparency plugs.

### ShaderView: Shader Balls
<img width="40%" src="docs/gafferShaderView2.png" alt="ShaderView" /><img width="50.5%" src="docs/gafferShaderTeapot.png" alt="Shader teapot" />

### Arnold Outputs
- `Lightgroup_[a-g]`
- `Lightgroups_denoise[a-g]` with optix filter.

### NameSwitch and Spreadsheet Presets
```
${sequence}/${shot}/${layer}
${sequence}/${shot}
${sequence}
${shot}/${layer}
${shot}
${layer}
```

### Node Defaults - EditScopes
- IncludeInNavigationMenu:
  - `GafferArnold.ArnoldLight`
  - `GafferScene.ShaderTweaks`
  - `GafferScene.StandardOptions`
  - `GafferArnold.ArnoldOptions`
  - `GafferScene.StandardAttributes`
  - `GafferArnold.ArnoldAttributes`
  - And some LDT nodes

<img src="docs/editscopes.png" alt="EditScopes" />

### Scene Inspector - `registerShaderParameter`
- aiStandardVolume: density, scatter_anisotropy, transparent_depth
- aiLights: all contributions

<img width="11.7%" src="docs/editscopes_2.png" alt="Scene Inspector" />

### Boxes (3D)

#### LightCreator
<img width="50%" src="docs/LightCreator.png" alt="LightCreator" />

#### Attribute Sets
Give it an attribute name and a scene path, and it will create a Set per unique attribute value containing the geometry.

<img width="50%" src="docs/gafferSets.png" alt="Attribute sets" />

#### LDTRenderLayer
<img src="docs/LDTRenderLayer.png" alt="LDTRenderLayer" />

#### contextEnabled EditScope and Box
Contents will only be enabled when in the given context. Both EditScope and Box based.  
The EditScope based contains Edit TweaksNodes ready to use.

<img width="50%" src="docs/contextEnabled.png" alt="contextEnabled" />

#### LightsMuteSolo
Mutes/Solo lights, using intensity or prune.

<img width="50%" src="docs/LightsMuteSolo.png" alt="LightsMuteSolo" />

#### Center To Origin
Centers the given objects to the origin.

<img width="50%" src="docs/CenterToOrigin.png" alt="CenterToOrigin" />

#### UvSizeMultipler
Scales the objects UVs. Useful for the ShaderBall scene, where you want to scale the UVs
for visualization instead of modifying the material tiling.

#### Inspection Camera
Inspection camera drop-in.

<img width="50%" src="docs/InpectionCamera.png" alt="InspectionCamera" />

### Boxes (2D)
#### ShowMetadata
Search metadata keys with partial matching, and overlay them on the image.  
For example: `/stats/geo` will display all `/arnold/stats/geo...`, and `samples` will display all keys containing the word `samples`.  
Leave blank to display all available keys.

<img src="docs/gafferLDTShowMetadataKeys.png" alt="ShowMetadata keys" />
<img width="100%" src="docs/gafferLDTShowMetadata.png" alt="ShowMetadata" />

### Misc
- Gaffer Cache MemoryLimit

---

## 中文

LDTGaffer 是一套个人 Gaffer 工具集：包含预设、配置、startup 脚本以及 boxed nodes。

**运行环境**

```需要 Gaffer 1.6.15.0 (Python 3)```

**Windows 说明（路径）**

本工具集同样面向 Windows 环境。为避免 `.grf` 引用加载失败与图标丢失，请确认：

- 设置插件根目录（推荐）：
  - `LDTGaffer=<本仓库的绝对路径>`
  -（兼容）`LDTGAFFER=<本仓库的绝对路径>`
- 确保 Gaffer 能找到图标：
  - `GAFFERUI_IMAGE_PATHS` 需包含 `<LDTGaffer>/icons`
- 确保 Gaffer 能找到 boxed nodes / references：
  - `GAFFER_REFERENCE_PATHS` 需包含 `<LDTGaffer>/resources/boxes`

> 提示：传给 Gaffer 引用加载的路径会被规范化为 POSIX 风格（`/`），以保证跨平台一致性。

**来源 / 致谢**

- 本仓库最初基于： https://github.com/ezequielmastrasso/LDTGaffer
- 由 **adu** (https://www.aducg.com) 进行 **Gaffer 1.6.15.0 兼容升级**与维护。

> 说明：此处的许多工具均参考了 Gaffer 社区邮件列表中的示例与讨论 : https://www.gafferhq.org/community/

### 文件夹与变量
- Custom Variables（LDT 资源变量）
- Bookmarks（LDT 常用路径书签）

### LDT 菜单
- 导出 Extension（Export Extension）
- 节点注释（Node Annotations）
- 注册 `includeInNavigationMenu`

### 节点默认值 - `nodeGadget:color`
配色逻辑与 Gaffer 默认一致，但整体更柔和，便于长时间使用。  
灯光节点为黄色，Filter 节点颜色更接近 Filter plugs 的颜色。

<img width="30%" src="docs/nodeGadget_color.png" alt="节点颜色" />

### Viewer
#### SceneView:Phong、Graph Editor Phong、以及 Diagnostics 2k/4k 纹理

<img width="31%" src="docs/sceneViewPhong.png" alt="Phong" /><img width="31%" src="docs/sceneViewPhong_2.png" alt="Phong2" /><img width="32%" src="docs/gafferDiagnosticPatterns.png" alt="Diagnostics" />

Phong 由 [Irene Hernández](https://www.linkedin.com/in/ireneher/) 提供。  
包含 Cs 与 transparency 等插口。

### ShaderView：ShaderBall
<img width="40%" src="docs/gafferShaderView2.png" alt="ShaderView" /><img width="50.5%" src="docs/gafferShaderTeapot.png" alt="ShaderTeapot" />

### Arnold 输出预设
- `Lightgroup_[a-g]`
- `Lightgroups_denoise[a-g]`（带 optix filter）

### NameSwitch 与 Spreadsheet 预设
```
${sequence}/${shot}/${layer}
${sequence}/${shot}
${sequence}
${shot}/${layer}
${shot}
${layer}
```

### 节点默认值 - EditScopes
- IncludeInNavigationMenu：
  - `GafferArnold.ArnoldLight`
  - `GafferScene.ShaderTweaks`
  - `GafferScene.StandardOptions`
  - `GafferArnold.ArnoldOptions`
  - `GafferScene.StandardAttributes`
  - `GafferArnold.ArnoldAttributes`
  - 以及部分 LDT 自定义节点

<img src="docs/editscopes.png" alt="EditScopes" />

### Scene Inspector - `registerShaderParameter`
- aiStandardVolume：density、scatter_anisotropy、transparent_depth
- aiLights：所有 contributions

<img width="11.7%" src="docs/editscopes_2.png" alt="Scene Inspector" />

### 盒子节点（3D）

#### LightCreator
<img width="50%" src="docs/LightCreator.png" alt="LightCreator" />

#### Attribute Sets
输入 attribute 名称与 scene:path，将按 attribute 的唯一值自动创建 Set，并把对应几何加入 Set。

<img width="50%" src="docs/gafferSets.png" alt="Attribute Sets" />

#### LDTRenderLayer
<img src="docs/LDTRenderLayer.png" alt="LDTRenderLayer" />

#### contextEnabled EditScope / Box
仅在指定 context 下启用内容（同时提供 EditScope 与 Box 两种方式）。  
EditScope 版本内置了可直接使用的 Edit Tweaks 节点。

<img width="50%" src="docs/contextEnabled.png" alt="contextEnabled" />

#### LightsMuteSolo
通过 intensity 或 prune 实现灯光的 mute/solo。

<img width="50%" src="docs/LightsMuteSolo.png" alt="LightsMuteSolo" />

#### Center To Origin
将选定对象居中并移动到世界原点。

<img width="50%" src="docs/CenterToOrigin.png" alt="CenterToOrigin" />

#### UvSizeMultipler
缩放对象 UV。常用于 ShaderBall 场景中，仅用于可视化（而不是修改材质的 tiling）。

#### Inspection Camera
开箱即用的 Inspection Camera。

<img width="50%" src="docs/InpectionCamera.png" alt="InspectionCamera" />

### 盒子节点（2D）
#### ShowMetadata
按关键字模糊匹配 metadata key，并将结果叠加显示在图像上。  
例如：`/stats/geo` 会显示所有 `/arnold/stats/geo...`，`samples` 会显示所有包含 samples 的 key。  
留空则显示所有可用 key。

<img src="docs/gafferLDTShowMetadataKeys.png" alt="ShowMetadataKeys" />
<img width="100%" src="docs/gafferLDTShowMetadata.png" alt="ShowMetadata" />

### 其他
- Gaffer 缓存内存上限（Cache MemoryLimit）
