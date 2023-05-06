# GUI


GIA's GUI is implemented by PyWebIO. The following functions are included:

- Select auto assist mode, status display

- Start/Stop

- Set Configuration

- Remote Control

## Function usage


### Task

Task is the basic module of GIA execution, all fully automated functions are started from Task.

When starting, check the checkbox for the corresponding function and press the button. Press the same button when stopping.

### Mission

Mission is a portable, integrated unit in GIA that performs functions in the Teyvat world, using a unified interface that is simple to write and use.

Mission can achieve the functions of gathering, combat, NPC dialogue (crafting) and walking. The combination of functions allows for fixed route gathering, mission automation and more.

The organizational call form for Mission is MissionGroup. A MissionGroup can include multiple Missions and MissionGroup. Select the MissionGroup to be run in the Main screen, and then start the Mission in Task to run the MissionGroup. A brief description of the features of the Group is available at the bottom of the MissionGroup.

## Auxiliary Functions


The auxiliary functions are some semi-automatic function modules that can automatically assist some operations.

Press the hotkey (default is `[`) in the Genshin to start/stop.

## Setup Configuration


You can configure the settings in the settings page.

Select the file to be configured in the drop-down box and follow the prompts to configure it.

## Remote Control


Press `Get ip` in the `main` screen to get the LAN connection ip, you can enter that ip on your computer to connect to the GIA control panel and operate the GIA on another computer.


