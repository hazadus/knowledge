## Eloquent JavaScript, 3rd edition
### Marijn Haverbeke · «No Starch Press» · 2019 г. · 476 с.

#JavaScript #programming #book 

[[Books Reading]]

http://library.hazadus.ru/books/78/details/

> [!abstract]
> JavaScript lies at the heart of almost every modern web application, from social apps like Twitter to browser-based game frameworks like Phaser and Babylon. Though simple for beginners to pick up and play with, JavaScript is a flexible, complex language that you can use to build full-scale applications.
>
This much anticipated and thoroughly revised third edition of Eloquent JavaScript dives deep into the JavaScript language to show you how to write beautiful, effective code. It has been updated to reflect the current state of JavaScript and web browsers and includes brand-new material on features like class notation, arrow functions, iterators, async functions, template strings, and block scope. A host of new exercises have also been added to test your skills and keep you on track.
>
As with previous editions, Haverbeke continues to teach through extensive examples and immerses you in code from the start, while exercises and full-chapter projects give you hands-on experience with writing your own programs. You start by learning the basic structure of the JavaScript language as well as control structures, functions, and data structures to help you write basic programs. Then you’ll learn about error handling and bug fixing, modularity, and asynchronous programming before moving on to web browsers and how JavaScript is used to program them. As you build projects such as an artificial life simulation, a simple programming language, and a paint program, you’ll learn how to:
>
>- Understand the essential elements of programming, including syntax, control, and data
>- Organize and clarify your code with object-oriented and functional programming techniques
>- Script the browser and make basic web applications
>- Use the DOM effectively to interact with browsers
>- Harness Node.js to build servers and utilities
>
Isn’t it time you became fluent in the language of the Web?
>
_All source code is available online in an interactive sandbox, where you can edit the code, run it, and see its output instantly._
>
[Книга доступна онлайн на официальном сайте](https://eloquentjavascript.net)

>[!info]
>##### Marijn Haverbeke
>
Marijn Haverbeke is a programming language enthusiast and polyglot. He's worked his way from trivial BASIC games on the Commodore, through a C++ phase, to the present where he mostly hacks on database systems and web APIs in dynamic languages. He recently won the JS1K—JavaScript demo in 1024 bytes—contest, and is the author of a wide range of open-source software.
>
>[Сайт автора](https://marijnhaverbeke.nl)

---

#### Creating a Regular Expression

```
let re1 = new RegExp("abc");
let re2 = /abc/;
```

----

#### Rest Parameters (p.96)
It can be useful for a function to accept any number of arguments. For example, `Math.max` computes the maximum of all the arguments it is given. To write such a function, you put three dots before the function’s last parameter, like this:
```
function max(...numbers) {
               let result = -Infinity;
               for (let number of numbers) {
                 if (number > result) result = number;
               }
               return result;
             }
console.log(max(4, 1, 9, -2));
// → 9
```
You can use a similar three-dot notation to call a function with an array of arguments.

```
let numbers = [5, 1, 7]; console.log(max(...numbers));
// → 7
```

This “spreads” out the array into the function call, passing its elements as separate arguments. It is possible to include an array like that along with other arguments, as in `max(9, ...numbers, 2)`.

----
📂 [[Reading]]