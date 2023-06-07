# 路径记录器

位置：flow/path_recorder_flow.py

## Usage

### Loading

1. 运行path_recorder_flow.py。
2. Waiting for loading, the `input your path name` prompt will appear, enter your path name.
3. Wait for the prompt `Load over.` `ready to start.` and the preparation is complete.

### Run

1. Press the `\` key and prompt `ready to start recording`.
2. After one operation, mention `start recording` to start moving.
3. While moving, all coordinates are recorded.
4. When the character's moving direction changes by more than 5°, a break position will be recorded.
5. After walking, press the `\` key again.
6. Should prompt `recording save as {jsonname}` within 1 second.
   7.json file will be saved as `name timestamp.json` in `assets/TeyvatMovePath`.
