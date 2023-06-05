# Auto Combat Assist


注：自动配置战斗文件默认开启，如果你不想配置，可以不看下面的配置介绍，或者只看`自动配置team文件`。

## Introduction


- Location: `config/settings/tactic` or CombatSetting in GUI.
- Auto Combat Assist can automatic switch characters, do attack, use E and Q skill accroding to set character name, tactic group, priorities, tiggers, etc.
- Suitable for characters who do not need to manually aim and use with shield characters. (Barely works with those who need to aim, just barely)
- Require the Genshin to run in 1080p windowing. Not recommend to set color filters.
- Need to set `team.json` file. The setting method is shown below.
- 非常推荐带一个钟离，如果没有钟离可以带4个护盾角色。
## tactic_group

Auto Combat Assist support the following tactic:

| Tactic Keyword | Description |
|---------------|--------------------------------|
| `>` | Skip to next group immediately |
| `@e?A:B` | Detect whether the Elemental Skill is in effetc. If it take effect, execute A. Otherwise, execute B. |
| `e?A:B` | Detect whether the Elemental Skill is ready. If ready, execute A, otherwise execute B. |
| `q?A:B` | Detect whether the Elemental Burst is ready. If ready, execute A, otherwise execute B. |
| `#@e?A:B` | Detect whether Elemental Skill is ongoing. If it is ongoing, loop execute A, otherwise execute B. |
| `#@q?A:B` | Detect whether Elemental is ongoing. If it is ongoing, loop execute A, otherwise execute B. |
| `a`/`a~`/`da` | Normal Attack/Heavy Attack/Drop Attack |
| `e`/`e~` | Use Elemental Skill (short/long) |
| `j` | jump |
| `ja` | jump and attack |
| `sp` | Sprint |
| num | delay, unit is milliseconds. |

Each tactic keyword is separated by `,`; different policy groups are separated by `;`. When the execution of a group of policies is finished, execute the next policy group.

Attantion:

- Aiming-to-shoot character can use heavy attack instead.
- Auto Aim will be
- Cannot include space.

- In the judgment expressions, the tactic keyword shoule be separated by `.` .
- In the judgment expressions, the tactic keyword shoule be separated by `.` .
- In the judgment expressions, the tactic keyword shoule be separated by `.` .

A tactic keyword containing `?` tactic keyword usage is similar to the ternary operator, e.g:

`@e?e:a;`: When Elemental is ready, execute `e`(use Elemental Skill), otherwise execute `a`(normal attack)

`@e?e.a.a:none;`：When Elemental is ready, execute`e,a,a`，otherwise not execute anything.

Where `none` can be any other meaningless character, indicating that no action is performed.

Attantion:

- judgment expressions in which judgment expressions cannot be nested;
- Judgment expressions should preferably end with a semicolon and not be followed by any tactic keywords.

Example:

| Character | Tactic |
|---------|----------------------|
| zhongli | `e?e~:none;q?q:none` |
| Yun Jin | `e?e~:none;q?q:none` |
| Yoimiya | `e?e:none;#@e?a:q;`  |

## Trigger


Allows switching to the character when trigger condition is established.

| trigger type | description |
|-----------|--------------------|
| `e_ready` | When a character Elemental Skill is ready, switching is allowed |
| `q_ready` | When a character Burst Skill is ready, switching is allowed |
| `idle` | always enable |

Multiple triggers can be used, with commas sparating the trigger. There can be no space.
When the trigger conditions of multiple characters are established, the order of switching is determinded by the priority.

## Position


Position is the role of the character in the team.

| 类型       | 说明 |
|-----------|--------------------|
| `Main` | Main damage character |
| `Shield` | Shield character |
| `Support` | Support character |
| `Recovery` | Recovery character |

角色定位的设置会影响自动战斗的部分功能。

## 优先级 priority


The priority decreases from smallest to largest, with 0 being the highest priority.
The priority can be the same level.

This is the GIA default priority setting:

n is the character id in the team, n∈{1,2,3,4}

- `Shield`:1000+n
- `Recovery`:1500+n
- `Support`:3000+n
- `Main`:2000+n

You may not use values based on thousands of digits, this is only used to distinguish whether the configuration is automatically generated or not.

## Other Settings


| Settings | Introduction |
|-------------------|--------------------------|
| `Elast_time` | E skill duration, or 0 if none |
| `Qlast_time` | Q skill duration, or 0 if none |
| `E_short_cd_time` | Short Ecd time, can't be 0 |
| `Epress_time` | the time to press and hold E, or 0 if none |
| `E_long_cd_time` | long Ecd time, or 0 if none |
| `Qcd_time`| Q skill cooldown time|
| `n` | The position of the character in the team (1~4), cannot be repeated, cannot be 0 |

## Auto-configure TEAM files


In the GUI, create a new TEAM file, enter the character name and press AutoFill, all empty input boxes and input boxes marked with -1 will be filled automatically.

The character's position in the team, character priority, and some of the character's triggers will not be automatically populated.

完全支持的角色列表：

```python
['Albedo', 'Bennett', 'Ningguang', 'Yoimiya', 'Yun Jin', 'Zhongli', 'Ganyu', 'Yelan', 'Kamisato Ayaka', 'Diona', 'Xiangling', 'Shenhe', 'Kaedehara Kazuha', 'Raiden Shogun', 'Hu Tao', 'Mona', 'Qiqi', 'Keqing', 'Sangonomiya Kokomi', 'Xingqiu', 'Lisa']
```

其余角色只有基本参数，没有经过核对与适配。如果你有兴趣，欢迎贡献角色参数(ﾉﾟ∀ﾟ)ﾉ

默认角色参数文件位置：`assets/characters_data/characters_parameters.json`

## Automatically generate TEAM files


如果在设置中启用了自动生成team文件，则会在战斗开始前扫描角色列表并**优先扫描tactic下的所有策略文件**，选择符合的策略文件。

如果没有符合的策略文件，则自动生成一套战斗策略。

## Character elemental battle technique, elemental burst picture setting


Since the new version, there is no need to set up images.

## Other Notes


- The program may pause when the character's blood level is too low or when a character dies.
- The program may pause when it is not in the right interface.

由于~~是个非酋~~能力有限，角色较少，默认战斗配置并非最优方案，如果你有更好的方案，随时`issue`

If you encounter a problem that cannot be solved, you can also submit an `issue`.

If you have a good character tactic group, welcome to send `issue` too.


You can create a new tactic file and change the `teamfile` in the CombatSettings to your own file.

You cannot modify it directly in the `example json`, otherwise your changes will be cleared after the next startup.

File Example:

[文件示例1 宵宫 钟离 班尼特 云堇](https://github.com/GenshinImpactAssistant/GIA-Document/blob/main/team_example_1.json)

[文件示例3 凌人 钟离 班尼特 纳西妲](https://github.com/GenshinImpactAssistant/GIA-Document/blob/main/team_example_3.json)

The example file is also available in the tactic folder.


