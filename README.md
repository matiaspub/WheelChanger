# WheelChanger (Sublime Text 2 plugin)

Whith WheelChanger you can change numbers(as in google chrome css editor) and lists with mouse wheel.

## Instalation
Recommended way is using [PackageControll] package.

### Using Sublime Package Control

It is preferred and simplest way for most users. 

- Install Package Control http://wbond.net/sublime_packages/package_control
- Open Package Control
- Select 'Install Package'
- Find and select 'WheelChanger'

### Using Git

If you like work with HEAD you can locate SublimeTableEditor in your packages directory.

- Go to your Packages directory, you can locate to your Packages directory by using the menu item 
  Preferences ->   Browse Packages...
- Inside the Packages directory, clone the SublimeTableEditor repository using the command below: 
  git clone https://github.com/matiaspub/WheelChanger.git SublimeTableEditor

### Download Manually

- Download the files using the GitHub .zip download option.
- Unzip the files and rename the folder to something like SublimeTableEditor.
- Copy the folder to your Sublime Text 2 Packages directory.

## Configuration
You can add self lists, but you must remember: everithing string in lists must be unique
````
{
  // lists of change words, words must be unique for all lists
	"lists": [
		["true","false"],
		["True","False"],
		["TRUE","FALSE"],
		["inherit","pointer","crosshair","progress","help","move","wait"],
		["bold","normal"],
		["hidden","scroll","visible"],
		["inside","outside"],
		["capitalize","lowercase","uppercase","none"],
		["absolute","relative","fixed","static"]
	],
	// if list ending - start anew
	"anew": true,
	// pattern for decimalic substrings
	"decimal_pattern": "[+-]?\\d+[.\\d]*"
}
````

## Key Map
It contain redefine standart keys as ctrl++(encrease font size), but you can change it.
````
[
  { "keys": ["ctrl++"], "command": "wheel_changer" },
	{ "keys": ["ctrl+="], "command": "wheel_changer" },
	{ "keys": ["ctrl+keypad_plus"], "command": "wheel_changer" },
	{ "keys": ["ctrl+-"], "command": "wheel_changer", "args": {"back": true} },
	{ "keys": ["ctrl+keypad_minus"], "command": "wheel_changer", "args": {"back": true} },
	{ "keys": ["ctrl+shift++"], "command": "wheel_changer", "args": {"step": 10} },
	{ "keys": ["ctrl+shift+="], "command": "wheel_changer", "args": {"step": 10} },
	{ "keys": ["ctrl+shift+keypad_plus"], "command": "wheel_changer", "args": {"step": 10} },
	{ "keys": ["ctrl+shift+-"], "command": "wheel_changer", "args": {"back": true, "step": 10} },
	{ "keys": ["ctrl+shift+keypad_minus"], "command": "wheel_changer", "args": {"back": true, "step": 10} },
	{ "keys": ["ctrl+shift+alt++"], "command": "wheel_changer", "args": {"step": 100} },
	{ "keys": ["ctrl+shift+alt+="], "command": "wheel_changer", "args": {"step": 100} },
	{ "keys": ["ctrl+shift+alt+keypad_plus"], "command": "wheel_changer", "args": {"step": 100} },
	{ "keys": ["ctrl+shift+alt+-"], "command": "wheel_changer", "args": {"back": true, "step": 100} },
	{ "keys": ["ctrl+shift+alt+keypad_minus"], "command": "wheel_changer", "args": {"back": true, "step": 100} }
]
````

## Mouse Map
It contain redefine standart keys as first line in code below, but you can change it.
````
[
  { "button": "scroll_up", "modifiers": ["ctrl"], "command": "wheel_changer" },
	{ "button": "scroll_down", "modifiers": ["ctrl"], "command": "wheel_changer", "args": {"back": true} },
	{ "button": "scroll_up", "modifiers": ["ctrl","shift"], "command": "wheel_changer", "args": {"step": 10} },
	{ "button": "scroll_down", "modifiers": ["ctrl","shift"], "command": "wheel_changer", "args": {"back": true, "step": 10} },
	{ "button": "scroll_up", "modifiers": ["ctrl","shift","alt"], "command": "wheel_changer", "args": {"step": 100} },
	{ "button": "scroll_down", "modifiers": ["ctrl","shift","alt"], "command": "wheel_changer", "args": {"back": true, "step": 100} }
]
````

[Sublime]: http://www.sublimetext.com/
[PackageControll]: http://wbond.net/sublime_packages/package_control/installation
