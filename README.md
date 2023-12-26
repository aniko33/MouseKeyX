<div align="center">
    <h1>MouseKeyX</h1>
    <img src="https://github.com/aniko33/MouseKeyX/assets/76649588/22660334-12ce-46c8-90b5-34586cfffce7">
</div>

# Installation
Clone repository
```
git clone https://github.com/aniko33/MouseKeyX
```

Open folder
```
cd MouseKeyX
```

Run setup script: 
```
bash setup.sh
```

# Configuration
The installation script will have created you the folder: `.config/mousekeyx`, in this folder you can add configuration files.
files must be format: `.xbindkeys`

**Configuration template**:
```
"some_command"
    b:button_number
```

You have to replace "some_command" with the command you want to run and then replace "button_number" with the number of the button you can get using *xev* (`xev -event button | grep button`)

**Sample configuration**:
```
"xte 'key y'"
    b:8
```

`xte` is a Xorg tool for sending keyboard inputs

# Useful links
[Arch wiki](https://wiki.archlinux.org/title/Mouse_buttons)

[Stackoverflow](https://stackoverflow.com/questions/10408816/how-do-i-use-the-nohup-command-without-getting-nohup-out#10408906)
