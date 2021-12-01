# VS Code and PlatformIO IDE for ESP32 and ESP8266 Arudino platform  code introduction

In this article, we will introduce how to program the ESP32 and ESP8266 boards using VS Code with PlatformIO IDE.

![Getting Started with VS Code and PlatformIO IDE for ESP32 and NodeMCU ESP8266 boards: Windows, Mac OS X, Linux Ubuntu](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/Getting-Started-Visual-Studio-VS-Code-PlatformIO-IDE-ESP32-ESP8266-NodeMCU-Windows-Mac-OS-X-Linux-Ubuntu.jpg?resize=828%2C466&quality=100&strip=all&ssl=1)

The Arduino IDE works great for small applications. However, for advanced projects with more than 200 lines of code, multiple files, and other advanced features like auto completion and error checking, VS Code with the PlatformIO IDE extension is the best alternative.

In this tutorial, we’ll cover the following topics:

- Installing VS Code (Visual Studio Code):
- Installing PlatformIO IDE Extension on VS Code
- Visual Studio Quick Interface Overview
- PlatformIO IDE Overview
- Uploading Code using PlatformIO IDE: ESP32/ESP8266
- Changing the Serial Monitor Baud Rate – PlatformIO IDE
- Installing Libraries on PlatformIO IDE

## Installing VS Code

Go to [Visual Studio Code](https://code.visualstudio.com/) and download the stable build for your operating system (Windows).

![](C:\Project\Website\docs\docs\esp32\images\2021-06-05-10-17-00-image.png)

Click on the installation wizard to start the installation and follow all the steps to complete the installation.

Make sure click `Add to PATH` option, and click **Next**. 

![Microsoft Visual Studio Code VS Code Installation wizard step 2](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/3-Install-VS-Code.png?resize=598%2C464&quality=100&strip=all&ssl=1)

Then follow the wizard complete the installation.

Open VS Code and you’ll be greeted by a Welcome tab with the released notes of the newest version.

![Microsoft Visual Studio Code VS Code Installation wizard welcome screen on a Windows PC](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/VS-Code-Welcome-Screen.png?resize=828%2C617&quality=100&strip=all&ssl=1)

That’s it. Visual Studio Code was successfully installed.

### Installing Python on Windows

To program the ESP32 and ESP8266 boards with PlatformIO IDE you need Python 3.5 or higher installed in your computer. We’re using Python 3.8.5.

Go to [python.org/download](https://python.org/download) and download Python 3.8.5 or a newest version.

Open the downloaded file to start the Python installation wizard.

The following window shows up.

![Installing Python 3.8.5 on a Windows PC and Add to Path](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/Install-Python-Add-to-path.png?resize=666%2C410&quality=100&strip=all&ssl=1)

**IMPORTANT: Make sure you check the option Add Python 3.8 to PATH.** Then, you can click on the **Install Now** button.

When the installation is successful you’ll get the following message.

![Python Installation successful on Windows PC](https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/Python-Installation-successful.png?resize=666%2C410&quality=100&strip=all&ssl=1)

You can click the **Close** button.

## Installing PlatformIO IDE Extension on VS Code

It is possible to program the [ESP32](https://randomnerdtutorials.com/projects-esp32/) and [ESP8266](https://randomnerdtutorials.com/projects-esp8266/) boards using VS Code with the PlatformIO IDE extension. Follow the next steps to install the PlatformIO IDE extension.

Open VS Code:

1. Click on the **Extensions** icon or press **Ctrl**+**Shift**+**X** to open the **Extensions** tab
2. Search for “**PlatformIO IDE**”
3. Select the first option
4. Finally, click the **Install** button (Note: the installation may take a few minutes)

![Install PlatformIO IDE Extension on VS Code](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/Install-Platformio-Extension-VS-Code.png?resize=828%2C457&quality=100&strip=all&ssl=1)

After installing, make sure that PlatformIO IDE extension is enabled as shown below.

![PlatformIO IDE Extension Enabled on VS Code](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/Platformioextension-enabled.png?resize=828%2C247&quality=100&strip=all&ssl=1)

After that, the PlatformIO icon should show up on the left sidebar as well as an **Home** icon that redirects you to PlatformIO home.

![PlatformIO Extension Installed Successfully](https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatformIO-extension-installed-successfully.png?resize=828%2C533&quality=100&strip=all&ssl=1)

That’s it, PlatformIO IDE extension was successfully added to VS Code.

If you don’t see the **PIO** icon and the quick tools at the bottom, you may need to restart VS code for the changes to take effect.

Either way, we recommend restarting VS Code before proceeding.

## VS Code Quick Interface Overview

Open VS Code. The following print screen shows the meaning of each icon on the left sidebar and its shortcuts:

![VS Code Visual Studio Application Interface Overview](https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/VS-Code-Interface-Overview.png?resize=828%2C457&quality=100&strip=all&ssl=1)

- File explorer
- Search across files
- Source code management (using gist)
- Launch and debug your code
- Manage extensions

Additionally, you can press **Ctrl**+**Shift**+**P** or go to **View** > **Command Palette…** to show all the available commands. If you’re searching for a command and you don’t know where it is or its shortcut, you just need to go to the Command Palette and search for it.

At the bottom, there’s a blue bar with PlatformIO commands.

![PlatformIO IDE extension Quick Tools Icons](https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatformIO-Quick-Tools-Icons.png?resize=183%2C20&quality=100&strip=all&ssl=1)

Here’s the what icon does from left to right:

- PlatformIO Home
- Build/Compile
- Upload
- Clean
- Serial Monitor
- New Terminal

If you hover your mouse over the icons, it will show what each icon does.

Alternatively, you can also click on the PIO icon to see all the PlatformIO tasks. 

![PlatformIO IDE extension Tasks menu](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatformIO-Tasks.png?resize=820%2C501&quality=100&strip=all&ssl=1)

If the tasks don’t show up on your IDE when you click the icon, you may need to click on the three dot icon at the top and enable PlatformIO tasks as shown below.

![Enable PlatformIO IDE extension tasks](https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/Enable-PlatformIO-Tasks.png?resize=828%2C508&quality=100&strip=all&ssl=1)

## PlatformIO IDE Overview

For you to get an overview on how PlatformIO works on VS code, we’ll show you how to create, save and upload a “Blinking LED” sketch to your ESP32 or ESP8266 board.

### Create a New Project

On VS Code, click on the PlartfomIO **Home** icon. Click on **+ New Project** to start a new project.

![Create New Project PlatformIO VS Code](https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatformIO-Create-New-Project.png?resize=828%2C356&quality=100&strip=all&ssl=1)

Give your project a name (for example *Blink_LED*) and select the board you’re using. In our case, we’re using the [DOIT ESP32 DEVKIT V1](https://makeradvisor.com/tools/esp32-dev-board-wi-fi-bluetooth/). The Framework should be “**Arduino**” to use the Arduino core.

You can choose the default location to save your project or a custom location.

The default location is in this path *Documents* >*PlatformIO* >*Projects*. For this test, you can use the default location. Finally, click “Finish”.

![PlatformIO with VS Code Create New ESP32 Project](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatformIO-Create-New-Project-ESP32.png?resize=598%2C470&quality=100&strip=all&ssl=1)

For this example, we’ll be using the [DOIT ESP32 DEVKIT board](https://makeradvisor.com/tools/esp32-dev-board-wi-fi-bluetooth/). If you are using an [ESP8266 NodeMCU board](https://makeradvisor.com/tools/esp32-dev-board-wi-fi-bluetooth/) the process is very similar, you just need to select your ESP8266 board:

![PlatformIO IDE extension with VS Code Create New ESP8266 Project](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatformIO-Create-New-Project-ESP8266.png?resize=602%2C472&quality=100&strip=all&ssl=1)

The Blink_LED project should be accessible from the Explorer tab.

![PlatformIO IDE Extension Project Folder Structure](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatfomIO-project-created-folder-structure.png?resize=828%2C338&quality=100&strip=all&ssl=1)

VS Code and PlatformIO have a folder structure that is different from the standard *.ino* project. If you click on the Explorer tab, you’ll see all the files it created under your project folder. It may seem a lot of files to work with. But, don’t worry, usually you’ll just need to deal with one or two of those files.

**Warning:** you shouldn’t delete, modify or move the folders and the *platformio.ini* file. Otherwise, you will no longer be able to compile your project using PlatformIO.

### platformio.ini file

The *platformio.ini* file is the PlatformIO Configuration File for your project. It shows the platform, board, and framework for your project. You can also add other configurations like libraries to be included, upload options, changing the Serial Monitor baud rate and other configurations.

![PlatformIO IDE extension Configuration File for ESP32](https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatformIO-Config-init-file-ESP32.png?resize=820%2C330&quality=100&strip=all&ssl=1)

- **platform**: which corresponds to the SoC used by the board.
- **board**: the development board you’re using.
- **framework**: the software environment that will run the project code.

With the ESP32 and ESP8266, if you want to use a baud rate of 115200 in your Serial Monitor, you just need to add the following line to your *platformio.ini* file.

```c
monitor_speed = 115200
```

After that, make sure you save the changes made to the file by pressing **Ctrl**+**S**.

In this file, you can also include the identifier of libraries you’ll use in your project using the lib_deps directive, as we’ll see later.

### src folder

The *src* folder is your working folder. Under the *src* folder, there’s a *main.cpp* file. That’s where you write your code. Click on that file. The structure of an Arduino program should open with the setup() and loop() functions.

![PlatformIO IDE extension main.cpp file under src folder](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatformIO-scr-folder-main-file.png?resize=828%2C286&quality=100&strip=all&ssl=1)

In PlatformIO, all your Arduino sketches should start with the #include <Arduino.h>.

## Uploading Code using PlatformIO IDE: ESP32/ESP8266

Copy the following code to your *main.cpp* file. 

```c
/*********  Rui Santos  Complete project details at https://RandomNerdTutorials.com/vs-code-platformio-ide-esp32-esp8266-arduino/*********/

#include <Arduino.h>

#define LED 2

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED, HIGH);
  Serial.println("LED is on");
  delay(1000);
  digitalWrite(LED, LOW);
  Serial.println("LED is off");
  delay(1000);
}
```

This code blinks the on-board LED every second. It works with the ESP32 and ESP8266 boards (both have the on-board LED connected to GPIO 2). 

We recommend that you copy this code manually, so that you see the autocompletion and other interesting features of the IDE in action. Additionally, if you have a syntax error somewhere in your program, it will underline it in red even before compiling.

After that, press **Ctrl**+**S** or go to **File** > **Save** to save the file.

Now, you can click on the Upload icon to compile and upload the code. Alternatively, you can go to the PIO Project Tasks menu and select **Upload**.

![Upload Code ESP32 board PlatformIO VS Code Visual Studio](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/Upload-Code-ESP32-PlatformIO-VS-Code.png?resize=828%2C379&quality=100&strip=all&ssl=1)

If the code is successfully uploaded, you should get the following message.

![Upload Code to ESP32 PlatformIO VS Code Success](https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/Upload-Code-ESP32-PlatformIO-VS-Code-Success.png?resize=828%2C595&quality=100&strip=all&ssl=1)

After uploading the code, the ESP32 or ESP8266 should be blinking its on-board LED every second.

![ESP32 board Built in LED turned on HIGH](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/04/ESP32-board-Built_in-LED-turned-on-HIGH.jpg?resize=750%2C422&quality=100&strip=all&ssl=1)

Now, click on the Serial Monitor icon and you should see it printing the current LED state.

![PlatformIO IDE VS Code Visual Studio Serial Monitor ESP32 board](https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/Platformio-VS-Code-Serial-Monitor-ESP32.png?resize=828%2C428&quality=100&strip=all&ssl=1)

**Note:** if you don’t see the Terminal window, go to the menu Terminal > New Terminal.

### Detect COM Port

PlatformIO will automatically detect the port your board is connected to. To check the connected devices you can go to the **PIO Home** and click the **Devices** icon.

![PlatformIO IDE extension VS Code Visual Studio Connected Devices COM Port Serial](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatformIO-VS-Code-Devices-COM-port.png?resize=828%2C550&quality=100&strip=all&ssl=1)

### Troubleshooting

If when trying to upload code you get the following error: “F*ailed to connect to ESP32: Timed out waiting for packet header*” it usually means that your board is not in flashing mode when you’re uploading the code. 

When this happens you need to press the ESP32 on-board BOOT button when you start seeing a lot of dots in the debugging window.

If you don’t want to have to press the BOOT button every time you upload new code, you can follow this guide: [[SOLVED] Failed to connect to ESP32: Timed out waiting for packet header.](https://randomnerdtutorials.com/solved-failed-to-connect-to-esp32-timed-out-waiting-for-packet-header/)

## Changing the Serial Monitor Baud Rate – PlatformIO IDE

The default baud rate used by PlatformIO is 9600. However, it is possible to set up a different value as mentioned previously. On the File Explorer, under your project folder, open the *platformio.ini* file and add the following line:

```c
monitor_speed = baud_rate
```

For example:

```c
monitor_speed = 115200
```

![PlatformIO IDE extesion Change Serial Monitor Baud Rate 115200](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatformIO-change-serial-monitor-baud-rate.png?resize=828%2C323&quality=100&strip=all&ssl=1)

After that, save that file.

## Installing ESP32/ESP8266 Libraries on PlatformIO IDE

Follow the next procedure if you need to install libraries in PlatformIO IDE.

Click the **Home** icon to go to PlatformIO Home. Click on the **Libraries** icon on the left side bar.

Search for the library you want to install. For example *Adafruit_BME280*.

[![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKQAAAAUCAMAAAA0oWYGAAAANlBMVEUAAACkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKT0RuBeAAAAEXRSTlMAECAwQFBgcHuEj5+vv8/f7w0rGDcAAANcSURBVEjHzZbLlsMoDEQLMMYBPaj//9lZCDt2Oj1nZtesHCKbS0klwLFnACh9SwDQWkaM1Cj4I2OSDUAjtQAw8gUAyD6V9e9AcgA7SW6AktQEJPeMKQCaqqpKBoDDVNX2c1JVVW0k1PUsvRUAQLOIA4BNVVUK0FRUKwBsomIdaajoyEhdRaUAQFfRkZC6yjm0wUmyBSQTlAH9YgLMAQySJHcAyUiS/ZokSc6Mdv3wUXC+1AOyne/3a/IgSUH2kCa+ewBISnKW9c8agkmSc0G+ApIFOoFEeUN2ANtcUbHeN8i1nb7iznVJWa8bAAhJ1kCZZYXMbQV7RnpCxq9SSZKWZGHIBIQbLh5NpyZvSJ8+fVpaW/TYA7cH5NrZLME2CwLOErKR9BOSCiRZkEaSM8YIJblvS5SAHGjcPXyzIM9FbpBHziWXkhe9lLL7Eu0GeYreVlgD6krNByRf4YkTctZccsklLyUXJBekAJOyfSxS/Am5X+5rj4KY2w0yGTktdMoeBd+X3tnu6SZZcFdylru7b0qOpSTKtgI6yemkoMbDBemiotpPyHFV236DrCR186AakWZb5fOpJA39nm4TUbEd35Uctx7VSfqYtHSQIj+MY+kOOT4hB8kODaV3kiz59PJDSZ8kj3aH5Anzm5IPyNmMswp5/F/I7CQbDpKewrS1Lis/lRyNqzB+Qv4nJbkP0ia93iF9iIgej3RrNJcLcilTYhqD5OgkJX0qqauz3NM9RMT2S8n6r0pyjyYj2X43zgBQZzTOC1JJej/GOtgqSc7w+IeSM+X5hJz5q3F+VzI+cKS7cY6Ucsr5akE575M3/76Ajc+ufzZpz/hRk+Xsw+8WlFJKKYfTyJYXZP8FMuLqA3KamZnbFoaYFgTz1sxfd0i2q5jjfvVQ0q9GfKXbYwFdbx1L0bR9h2zhn8jIx7HI/ddjMVlk+3WMdWotaSu+KYnI14dxOKOk2deyCfMTUmITe1wJvlwwWG+QM46AdcF4G+p0VBh1poCc9wtGwepRzDjLM8Z1WkRgjtK+QzYz84piZg1J3XyPyTXcCup6VjnWVc3NfMfuZlavGavAy8183Y+yuLkWpOHmmgFkdXPJSOLvFWRZs68LSAkD/pkr+XuUPg8AqDozgPya/W8B/gPQAm/tWHkI8wAAAABJRU5ErkJggg==)](https://www.mediavine.com/)

![PlatformIO IDE extension VS Code Visual Studio Search for BME280 Library](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatformIO-VS-Code-Search-BME280-library.png?resize=828%2C550&quality=100&strip=all&ssl=1)

Click on the library you want to include in your project. Then, click **Add to Project**.

![PlatformIO with VS Code Add Library to Project](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatformIO-add-library-to-project.png?resize=745%2C243&quality=100&strip=all&ssl=1)

Select the project were you want to use the library.

![PlatformIO with VS Code Add Library to Project Choose Project](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatformIO-VS-Code-Add-Library-to-Project-Choose-Project.png?resize=701%2C419&quality=100&strip=all&ssl=1)

This will add the library identifier using the lid_deps directive on the *platformio.ini* file. If you open your project’s *platformio.ini* file, it should look as shown in the following image.

![Add Library Identifier to Configuration File PlatformIO](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PIO-Configuration-File-Add-Library.png?resize=828%2C385&quality=100&strip=all&ssl=1)

Alternatively, on the library window, if you select the **Installation** tab and scroll a bit, you’ll see the identifier for the library. You can choose any of those identifiers depending on the options you want to use. The library identifiers are highlighted in red.

![PlatformIO IDE Extension Library Registry menu](https://i1.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatformIO-Library-registry.png?resize=828%2C646&quality=100&strip=all&ssl=1)

Then, go to the *platformio.ini* file of your project and paste the library identifier into that file, like this:

```
lib_deps = adafruit/Adafruit BME280 Library@^2.1.0
```

If you need multiple libraries, you can separate their name by a coma or put them on different lines. For example:

```
lib_deps =
  arduino-libraries/Arduino_JSON @ 0.1.0
  adafruit/Adafruit BME280 Library @ ^2.1.0
  adafruit/Adafruit Unified Sensor @ ^1.1.4
```

PlatformIO has a built-in powerful Library Manager, that allows you to specify custom dependencies per project in the Project Configuration File *platformio.ini* using lib_deps. This will tell PlatformIO to automatically download the library and all its dependencies when you save the configuration file or when you compile your project.

## Open a Project Folder

To open an existing project folder on PlatformIO, open VS Code, go to PlatformIO Home and click on **Open Project**. Navigate through the files and select your project folder.

![VS Code with PlatformIO Open Project Folder](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/PlatformIO-open-project-folder.png?resize=828%2C419&quality=100&strip=all&ssl=1)

PlatformIO will open all the files within the project folder.

## VS Code Color Themes

VS Code lets you choose between different color themes. Go to the **Manage** icon and select **Color Theme**. You can then select from several different light and dark themes.

![VS Code Visual Studio Change Color Themes Dark Light](https://i2.wp.com/randomnerdtutorials.com/wp-content/uploads/2020/09/VS-Code-Change-Color-Theme.png?resize=318%2C429&quality=100&strip=all&ssl=1)

## Shortcuts’ List

For a complete list of VS Code shortcuts for Windows, Mac OS X or Linux, check the next link:

- [VS Code Keyboard Shortcuts Reference](https://code.visualstudio.com/docs/getstarted/keybindings#_keyboard-shortcuts-reference).

## Wrapping Up

In this tutorial you’ve learned how to install and prepare Visual Studio Code to work with the ESP32 and ESP8266 boards. VS Code with the PlatformIO IDE extension is a great alternative to the classical Arduino IDE, especially when you’re working on more advanced sketches for larger applications.

Here’s some of the advantages of using VS Code with PlatformIO IDE over Arduino IDE: 

- It detects the COM port your board is connected to automatically; 
- VS Code IntelliSense: Auto-Complete. IntelliSense code completion tries to guess what you want to write, displaying the different possibilities and provides insight into the parameters that a function may expect;
- Error Highlights: VS Code + PIO underlines errors in your code before compiling;
- Multiple open tabs: you can have several code tabs open at once;
- You can hide certain parts of the code;
- Advanced code navigation;
- And much more…

If you’re looking for a more advanced IDE to write your applications for the ESP32 and ESP8266 boards, VS Code with the PlatformIO IDE extension is a great option.
