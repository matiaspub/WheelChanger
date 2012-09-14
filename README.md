# WheelChanger (Sublime Text 2 plugin)

Whith WheelChanger you can change numbers(as in google chrome css editor) and lists with mouse wheel.

## Instalation
Recommended way is using [PackageControll] package.

### Using Sublime Package Control

It is preferred and simplest way for most users. 

- Install Package Control http://wbond.net/sublime_packages/package_control
- Open Package Control
- Select 'Install Package'
- Find and select 'Table Editor'

### Using Git

If you like work with HEAD you can locate SublimeTableEditor in your packages directory.

- Go to your Packages directory, you can locate to your Packages directory by using the menu item 
  Preferences ->   Browse Packages...
- Inside the Packages directory, clone the SublimeTableEditor repository using the command below: 
  git clone https://github.com/vkocubinsky/SublimeTableEditor.git SublimeTableEditor

### Download Manually

- Download the files using the GitHub .zip download option.
- Unzip the files and rename the folder to something like SublimeTableEditor.
- Copy the folder to your Sublime Text 2 Packages directory.

## Configuration
There is currently no way to get list of available build systems in [Sublime], so you need to explicitly specify the ones you wanna list. Just add into your `XXX.sublime-project` something like this:

````
{
    "settings": {
        "build_switcher_systems": ["Unit tests", "CoffeeScript"]
    }
}
````

If you don't specify any build system, BuildSwitcher will just execute the currently selected build (the same behavior as Sublime's default `super+b` shortcut).

If you specify only one build system, it will execute it without asking.

If you specify multiple systems, you always get a pop up with options (sorted by usage).

## Defining key shortcut
By default, "build_switcher" is mapped to `CMD+B`, however you can easily change that, just add to your keymap preferences:

````
{ "keys": ["super+b"], "command": "build_switcher" }
````



[Sublime]: http://www.sublimetext.com/
[PackageControll]: http://wbond.net/sublime_packages/package_control/installation
[tarball]: https://github.com/vojtajina/sublime-BuildSwitcher/tarball/master
