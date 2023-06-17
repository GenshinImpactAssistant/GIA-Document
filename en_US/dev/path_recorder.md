# 路径记录器

位置：flow/path_recorder_flow.py

**该文件用于游戏内路径记录。目前推荐使用GUI版的VideoToPath达到相似功能。**

## Usage

### Loading

1. 运行path_recorder_flow.py。
2. Waiting for loading, the `input your path name` prompt will appear, enter your path name.
3. Wait for the prompt `Load over.` `ready to start.` and the preparation is complete.

### Run

06. It should prompt `recording save as {jsonname}` within 1 second. If not, press `\` again.
07. After a series of operations, mention `start recording` to start moving.
08. While moving, all coordinates will be recorded. At the same time, the action state of the character (walking, climbing, etc.) will also be recorded.
09. When the movement direction of the character changes by more than 5°, a break position will be recorded. The minimum distance between break positions is 5.2.
10. When you're done walking, press the `\` key again. Prompt `ready to stop recording`.
11. It should prompt `recording save as {jsonname}` within 1 second. If not, press `\` again.
12. json文件将保存为 `name+timestamp.pydict` 。如果想继续记录，就重复这些步骤。
