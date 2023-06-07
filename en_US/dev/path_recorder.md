# 路径记录器

位置：flow/path_recorder_flow.py

## Usage

### Loading

1. 运行path_recorder_flow.py。
2. Waiting for loading, the `input your path name` prompt will appear, enter your path name.
3. Wait for the prompt `Load over.` `ready to start.` and the preparation is complete.

### Run

1. 按下 `\` 键，提示 `ready to start recording` 。如果没有，就再按一次。
2. After one operation, mention `start recording` to start moving.
3. While moving, all coordinates will be recorded. At the same time, the action state of the character (walking, climbing, etc.) will also be recorded.
4. When the movement direction of the character changes by more than 5°, a break position will be recorded. The minimum distance between break positions is 5.2.
5. 走完之后，再次按下 `\` 键。提示 `ready to stop recording` 。
6. 在1秒内应该会提示 `recording save as {jsonname}` 。如果没有，就再按一次 `\` 。
7. The json file will be saved as `name+timestamp.json` in `assets/TeyvatMovePath`. Repeat these steps if you want to continue recording.
