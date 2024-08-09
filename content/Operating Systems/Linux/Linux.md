📂 [[Tooling]]

----

## Internals
### Processes

> [!info] Архитектура UNIX. Процессы  
> Презентация 3-01: ядро UNIX  
> [http://heap.altlinux.org/tmp/unix_base/ch01s03.html](http://heap.altlinux.org/tmp/unix_base/ch01s03.html)  
The most central concept in any operating system is the **process**: an abstraction of a running program.
**A process is just an instance of an executing program, including the current values of the program counter, registers, and variables.** Conceptually, each process has its own virtual CPU. In reality, of course, each real CPU switches back and forth from process to process, but to understand the system, it is much easier to think about a collection of processes running in (pseudo)  
parallel than to try to keep track of how each CPU switches from program to program.  
The difference between a process and a program is subtle, but absolutely crucial. An analogy may help you here. Consider a culinary-minded computer scientist who is baking a birthday cake for his young daughter. He has a birthday cake recipe and a kitchen well stocked with all the input: flour, eggs, sugar, extract of vanilla, and so on. In this analogy, the recipe is the program, that is, an algorithm expressed in some suitable notation, the computer scientist is the processor (CPU), and the cake ingredients are the input data. The process is the activity consisting of our baker reading the recipe, fetching the ingredients, and baking the cake.
Now imagine that the computer scientist’s son comes running in screaming his head off, saying that he has been stung by a bee. The computer scientist records where he was in the recipe (the state of the current process is saved), gets out a first-aid book, and begins following the directions in it. Here we see the processor being switched from one process (baking) to a higher-priority process (administering medical care), each having a different program (recipe versus first aid book). When the bee sting has been taken care of, the computer scientist goes back to his cake, continuing at the point where he left off.
The key idea here is that a process is an activity of some kind. It has a program, input, output, and a state. A single processor may be shared among several processes, with some scheduling algorithm being accustomed to determine when to stop work on one process and service a different one. In contrast, a program is something that may be stored on disk, not doing anything.
The main active entities in a Linux system are the processes. Each process runs a single program and initially has a single thread of control. In other words, it has one program counter, which keeps track of the next instruction to be executed. Linux allows a process to create additional threads once it starts.
![[attachments/Untitled 15.png|Untitled 15.png]]
### Threads
In traditional operating systems, each process has an address space and a single thread of control. In fact, that is almost the definition of a process. Nevertheless, in many situations, it is useful to have multiple threads of control in the same address space running in quasi-parallel, as though they were (almost) separate processes (except for the shared address space).
The main reason for having **threads** is that in many applications, multiple activities are going on at once. Some of these may block from time to time. By decomposing such an application into multiple sequential threads that run in quasi-parallel, the programming model becomes simpler.
We have seen this argument once before. It is precisely the argument for having processes. Instead of thinking about interrupts, timers, and context switches, we can think about parallel processes. Only now with threads we add a new element: the ability for the parallel entities to share an address space and all of its data among themselves. This ability is essential for certain applications, which is why having multiple processes (with their separate address spaces) will not work.
A second argument for having threads is that since they are lighter weight than processes, they are easier (i.e., faster) to create and destroy. In many systems, creating a thread goes 10–100 times faster than creating a process. When the number of threads needed changes dynamically and rapidly, this property is useful to have.
A third reason for having threads is also a performance argument. Threads yield no performance gain when all of them are CPU bound, but when there is substantial computing and also substantial I/O, having threads allows these activities to overlap, thus speeding up the application.
Finally, threads are useful on systems with multiple CPUs, where real parallelism is possible.
### IO Streams

> [!info] Стандартные потоки ввода/вывода — Xgu.ru  
> Стандартные потоки ввода и вывода в UNIX/Linux наряду с файлами  
> [http://xgu.ru/wiki/Стандартные_потоки_ввода/вывода](http://xgu.ru/wiki/Стандартные_потоки_ввода/вывода)  
![[attachments/Untitled 1 5.png|Untitled 1 5.png]]
## CLI and UI
### CLI

> [!info] GitHub - NisreenFarhoud/Bash-Cheatsheet  
> The main topics of this cheatsheet include an intro to the shell, navigating around the shell, common commands, environment variables, connectors, piping, I/O redirection, permissions, and keyboard shortcuts.  
> [https://github.com/NisreenFarhoud/Bash-Cheatsheet](https://github.com/NisreenFarhoud/Bash-Cheatsheet)  

> [!info] 9 Bash Script Examples to Get You Started on Linux  
> If you're starting out with Bash scripting on Linux, getting a solid grasp of the basics will stand you in good stead.  
> [https://www.howtogeek.com/808593/bash-script-examples/](https://www.howtogeek.com/808593/bash-script-examples/)  

> [!info] Работаем в терминале Linux как профи: подборка полезных команд  
> Видели про-юзеров Linux, которые эффективно работают в терминале?  
> [https://tproger.ru/articles/useful-linux-commands/](https://tproger.ru/articles/useful-linux-commands/)  

> [!info] Оболочка Bash - шпаргалка для начинающих  
> В данной шпаргалке затрагиваются следующие темы: введение в оболочку, навигация, основные команды, переменные окружения, коннекторы, конвейеры, перенаправление ввода/вывода, права доступа и комбинации клавиш.  
> [https://tproger.ru/translations/bash-cheatsheet/](https://tproger.ru/translations/bash-cheatsheet/)  

> [!info]  
>  
> [https://www.cyberciti.biz/faq/bash-shell-change-the-color-of-my-shell-prompt-under-linux-or-unix/](https://www.cyberciti.biz/faq/bash-shell-change-the-color-of-my-shell-prompt-under-linux-or-unix/)  
[[CLI - Shell]]
[[Bash script]]
[[SSH]]
### Environment Variables

> [!info] How to Set an Environment Variable in Linux  
> In programming, you use variables to store information like strings and numbers temporarily.  
> [https://www.freecodecamp.org/news/how-to-set-an-environment-variable-in-linux/](https://www.freecodecamp.org/news/how-to-set-an-environment-variable-in-linux/)  
```Bash
# show env vars
env
# print env var
echo $PATH
```
### Desktop GUI

> [!info] How to Integrate Applications and Scripts to a Linux Desktop  
> On Linux, an application without a desktop file won't integrate with your desktop environment.  
> [https://www.howtogeek.com/833003/how-to-integrate-applications-and-scripts-to-a-linux-desktop/](https://www.howtogeek.com/833003/how-to-integrate-applications-and-scripts-to-a-linux-desktop/)  
```JavaScript
[Desktop Entry]
Name=PyCharm Professional
Comment=Python IDE
Exec=/home/hazadus/Apps/pycharm-2022.2.3/bin/pycharm.sh
Path=/home/hazadus/Apps/pycharm-2022.2.3/bin
Icon=/home/hazadus/Apps/pycharm-2022.2.3/bin/pycharm.png
Terminal=false
Type=Application
Categories=Development;
```
```Bash
sudo cp PyCharm.desktop /usr/share/applications/
cp PyCharm.desktop ~/.local/share/applications
cp PyCharm.desktop ~/Desktop
sudo update-desktop-database
```