# Auto Combat Assist


注：自动配置战斗文件默认开启，如果你不想配置，可以不看下面的配置介绍，或者只看`自动配置team文件`项目。

## Introduction


- Location: `config/settings/tactic` or CombatSetting in GUI.

- Auto Combat Assist can automatic switch characters, do attack, use E and Q skill accroding to set character name, tactic group, priorities, tiggers, etc.

- Suitable for characters who do not need to manually aim and use with shield characters. (Barely works with those who need to aim, just barely)

- Require the Genshin to run in 1080p windowing. Not recommend to set color filters.

- Need to set `team.json` file. The setting method is shown below.

- Recommend to bring Zhongli, if not can bring 3~4 shield characters.
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
| type | description |
|-----------|--------------------|
| `Main` | Main damage character |
| `Shield` | Shield character |
| `Support` | Support character |
| `Recovery` | Recovery character |


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

[List of supported roles](../../assets/characters_data/characters_parameters.json)

[Character names file Thanks for xicri/genshin-dictionary](../../assets/characters_data/characters_name.json)

Welcome to contribute character parameters (ﾟ∀ﾟ)ノ

## Automatically generate TEAM files


If automatic TEAM file generation is enabled in the settings, the character list will be scanned and all tactic files under tactic folder will be scanned before the battle starts and the matching tactic files will be selected.

If there is no matching tactic file, then according to [list of supported roles](... /... /assets/characters_data/characters_parameters.json) to automatically generate a set of battle tactic.

If the character does not exist in the [list of supported characters](... /... /assets/characters_data/characters_parameters.json) then the default TEAM file will be used.

## Character elemental battle technique, elemental burst picture setting


Since the new version, there is no need to set up images.

## Other Notes


- The program may pause when the character's blood level is too low or when a character dies.
- The program may pause when it is not in the right interface.

Due to limited capacity and fewer characters, the above configuration is not the optimal solution, if you have a better plan, feel free to `issue`.

If you encounter a problem that cannot be solved, you can also submit an `issue`.

If you have a good character tactic group, welcome to send `issue` too.


You can create a new tactic file and change the `teamfile` in the CombatSettings to your own file.

You cannot modify it directly in the `example json`, otherwise your changes will be cleared after the next startup.

File Example:

[File example 1: Yoimiya, Zhongli Bennett Yun Jin](../team_example_1.json)

[File example 3](../team_example_3.json)

The example file is also available in the tactic folder.


