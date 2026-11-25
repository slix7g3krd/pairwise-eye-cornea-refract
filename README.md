# pairwise-eye-cornea-refract

## 领域

游戏、图形与多媒体

## 主题

眼角膜折射与虹膜视差

## 说明

双层角膜折射、瞳孔视差深度、虹膜接缝连续。

初始状态下 `graphics/eye_cornea.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
