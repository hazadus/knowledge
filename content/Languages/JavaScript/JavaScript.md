### Libraries
[[Axios]]
[[Vue.js]]
# JavaScript Language
### Various Snippets and Tips
```JavaScript
// crypto.randomUUID is a method built into the browser (it's not a third-party package).
// It's available in all major browsers. It has nothing to do with cryptocurrencies.
// This method generates a unique string, like `d9bb3c4c-0459-48b9-a94c-7ca3963f7bd0`.
crypto.randomUUID()
```
## JavaScript Basics
### References

> [!info] JavaScript | MDN  
> JavaScript (JS) is a lightweight, interpreted, or just-in-time compiled programming language with first-class functions.  
> [https://developer.mozilla.org/en-US/docs/Web/JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)  

> [!info] Operator Lookup - Search JavaScript operators  
> Friendly tutorials for developers.  
> [https://www.joshwcomeau.com/operator-lookup/](https://www.joshwcomeau.com/operator-lookup/)  
### Browser Console
[How To Use the JavaScript Developer Console | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-use-the-javascript-developer-console)
```JavaScript
console.log("Hello, World!");
let today = new Date();
console.log("Today's date is " + today);
```
If you need to modify a command that you passed through the Console, you can type the up arrow (**↑**) key on your keyboard to retrieve the previous command. This will allow you to edit the command and send it again.
### **Working with an HTML File**
```HTML
<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Today's Date</title>
</head>
<body>
</body>
</html>
```
```JavaScript
let today = new Date();
document.body.innerHTML = "<h1>Today's date is " + today + "</h1>";
document.body.style.backgroundColor = "lightblue";
document.body.style.color = "white";
let p = document.createElement("P");
let t = document.createTextNode("Paragraph text.");
p.appendChild(t);
document.body.appendChild(p);
```
### **Adding JavaScript into an HTML Document**
[How To Add JavaScript to HTML | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-add-javascript-to-html)
You can add JavaScript code in an HTML document by employing the dedicated HTML tag `<script>` that wraps around JavaScript code.  
  
The  
`<script>` tag can be placed in the `<head>` section of your HTML or in the `<body>` section, depending on when you want the JavaScript to load.  
  
Generally, JavaScript code can go inside of the document  
`<head>` section in order to keep them contained and out of the main content of your HTML document.  
  
However, if your script needs to run at a certain point within a page’s layout — like when using  
`document.write` to generate content — you should put it at the point where it should be called, usually within the `<body>` section.
```JavaScript
<!DOCTYPE html>
<html lang="en-US">
 
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Today's Date</title>
    <script>
        // run the JavaScript script before loading in the rest of the page.
    </script>
</head>
<body>
 
</body>
</html>
```
```JavaScript
<!DOCTYPE html>
<html lang="en-US">
 
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Today's Date</title>
</head>
 
<body>
  
  <script>
      let d = new Date();
      document.body.innerHTML = "<h1>Today's date is " + d + "</h1>"
  </script>
</body>
</html>
```
```JavaScript
<!DOCTYPE html>
<html lang="en-US">
 
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Today's Date</title>
    <link rel="stylesheet" href="css/style.css">
</head>
 
<body>
	<script src="js/script.js"></script>
</body>
</html>
```
### Operators
```JavaScript
let odyssey = 2001;
console.log(typeof odyssey);  // 'number'
```
```JavaScript
// Check if variable is equal to value
if (username === "sammy_shark") {
  console.log(true);
}
```
### Common Functions
```JavaScript
console.log("Hello, World!");
alert("Hello, World!");
let name = prompt("What is your name?");
```
### Variables
[Understanding Variables, Scope, and Hoisting in JavaScript | DigitalOcean](https://www.digitalocean.com/community/tutorials/understanding-variables-scope-hoisting-in-javascript)
In JavaScript, there are three keywords used to declare a variable — `var`, `let`, and `const` — and each one affects how the code will interpret the variable differently.
![[attachments/Untitled 20.png|Untitled 20.png]]
```JavaScript
// Assignment of various variables
var name = "Sammy";
var spartans = 300;
var kingdoms = [ "mammals", "birds", "fish" ];
var poem = { roses: "red", violets: "blue" }; 
var success = true;
var nothing = null;
```
### Syntax
```JavaScript
// An example of if statement syntax
if () { }
// Check math equation and print a string to the console
if (4 < 5) {
	console.log("4 is less than 5.");
}
// An example of for loop syntax
for () { }
// Iterate 10 times, printing out each iteration number to the console
for (let i = 0; i <= 10; i++) {
	console.log(i);
}
```
```JavaScript
// An example function
function functionName() {}
// Initialize a function to calculate the volume of a cube
function cube(number) {
	return Math.pow(number, 3);
}
// Invoke the function
cube(5);
```
```JavaScript
// A single JavaScript statement
const now = new Date();
// Get the current timestamp and print it to the console
const now = new Date(); console.log(now);
// Two statements separated by newlines
// If statements are separated by a newline, the semicolon is optional.
const now = new Date()
console.log(now)
// Two statements separated by newlines and semicolons
const now = new Date();
console.log(now);
// An example object
const objectName = {};
// Initialize triangle object
const triangle = {
	type: "right",
	angle: 90,
	sides: 3,
};
// Initialize a function to calculate the area of a square
function square(number) {
	return Math.pow(number, 2);
}
// Calculate the area of a number greater than 0
if (number > 0) {
	square(number);
}
```
The convention of JavaScript names is that they are written in camelCase, meaning the first word is lowercase but every following word starts with an uppercase letter. You may also see global variables or constants written in all uppercase, separated by underscores.
```JavaScript
// Var names are case-sensitive
var myVariable = 1;
var myvariable = 2;
// PascalCase in class names
// Initialize a class
class ExampleClass {
	constructor() { }
}
```
## Arrays
### `with()`

> [!info] Array.prototype.with() - JavaScript | MDN  
> The with() method of Array instances is the copying version of using the bracket notation to change the value of a given index.  
> [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/with](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/with)  
```JavaScript
const arr = [1, 2, 3, 4, 5];
console.log(arr.with(2, 6)); // [1, 2, 6, 4, 5]
console.log(arr); // [1, 2, 3, 4, 5]
```
## Data Types
### Dynamic Typing
With dynamically typed languages, a variable of the same name can be used to hold different data types.
For example, the variable `t`, defined as a variable by the `let` keyword (note that `let` keeps a given variable limited in scope), can be assigned to hold different data types, or can be initialized but left undefined:
```JavaScript
let t = 16;		  	// t is a number
let t = "Teresa";	// t is a string
let t = true;		  // t is a Boolean
let t;			    	// t is undefined
```
```JavaScript
let fish = ["shark", "cuttlefish", "clownfish", "eel"];
```
The JavaScript **object** data type can contain many values as **name:value** pairs. These pairs provide a useful way to store and access data. The object literal syntax is made up of name:value pairs separated by colons with curly braces on either side `{ }`.
```JavaScript
let sammy = {
    firstName: "Sammy",
    lastName: "Shark",
    color: "blue",
    location: "Ocean"
};
```
[https://www.digitalocean.com/community/tutorials/understanding-objects-in-javascript](https://www.digitalocean.com/community/tutorials/understanding-objects-in-javascript)
### String Manipulation and Formatting
[How To Index, Split, and Manipulate Strings in JavaScript | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-index-split-and-manipulate-strings-in-javascript)
```JavaScript
const poem = "The Wide Ocean";
const author = "Pablo Neruda";
// Variables in Strings with Template Literals:
const favePoem = `My favorite poem is ${poem} by ${author}.`;
// NB: Template literals are defined with backticks, and therefore 
// both quotes and apostrophes can be used safely without any sort of 
// extra escaping or consideration.
```
```JavaScript
const threeLines = "This is a string\n" +
"that spans across\n" +
"three lines.";
```
```JavaScript
// Initializing a new string primitive
const stringPrimitive = "A new string.";
// Initializing a new String object
const stringObject = new String("A new string.");
```
```JavaScript
"How are you?"[5];
"How are you?".charAt(5);
"How are you?".indexOf("o"); // lastIndexOf() also exists
"How are you?".indexOf("are");
"How are you?".slice(8, 11); // you
"How are you?".slice(8); // you?
```
```JavaScript
"How are you?".length;
"How are you?".toUpperCase();
"How are you?".toLowerCase();
```
```JavaScript
const originalString = "How are you?";
// Split string by whitespace character
const splitString = originalString.split(" ");
console.log(splitString);  // [ 'How', 'are', 'you?' ]
```
```JavaScript
const tooMuchWhitespace = "     How are you?     ";
const trimmed = tooMuchWhitespace.trim();
console.log(trimmed);  // How are you?
```
```JavaScript
const originalString = "How are you?"
// Replace the first instance of "How" with "Where"
const newString = originalString.replace("How", "Where"); // Only affects first value!
console.log(newString);
```
### Regular Expressions (RegExp)

> [!info] RegExr: Learn, Build, & Test RegEx  
> Regular expression tester with syntax highlighting, PHP / PCRE & JS Support, contextual help, cheat sheet, reference, and searchable community patterns.  
> [https://regexr.com/](https://regexr.com/)  

> [!info] Regular expressions - JavaScript | MDN  
> Regular expressions are patterns used to match character combinations in strings.  
> [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)  
In addition to being able to replace a value with another string value, we can also use [Regular Expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) to make `replace()` more powerful. For instance, `replace()` **only affects the first value**, but we can use the `g` (global) flag to catch all instances of a value, and the `i` (case insensitive) flag to ignore case.
```JavaScript
const originalString = "Javascript is a programming language. I'm learning javascript."
// Search string for "javascript" and replace with "JavaScript"
const newString = originalString.replace(/javascript/gi, "JavaScript");
console.log(newString);
```
## Converting types
[How To Convert Data Types in JavaScript | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-javascript)
```JavaScript
// to String
String(49);
let blows = 400;
blows.toString();
(1776).toString();			// returns "1776"
(false).toString();			// returns "false"
(100 + 200).toString();		// returns "300"
// to Numbers
Number("1984");
Number(" ");	// returns 0
Number("");		// returns 0
Number("twelve");	// returns NaN
Number("20,000");	// returns NaN
Number("2 3");		// returns NaN
Number("11-11-11");	// returns NaN
Number(false);	// returns 0
Number(true);		// returns 1
Boolean(0);			// returns false
Boolean("");		// returns false
Boolean(undefined);	// returns false
Boolean(NaN);		// returns false
Boolean(null);		// returns false
Boolean(2000);		// returns true
Boolean(" ");		// returns true
Boolean("Maniacs");	// returns true
Boolean("0");	// returns true
```
## Math
[How To Do Math in JavaScript with Operators | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-do-math-in-javascript-with-operators)
## Advanced
### References
[Understanding the Event Loop, Callbacks, Promises, and Async/Await in JavaScript | DigitalOcean](https://www.digitalocean.com/community/tutorials/understanding-the-event-loop-callbacks-promises-and-async-await-in-javascript)
### async / await / fetch
```JavaScript
// Handling success and errors with async/await
async function getUser() {
  try {
    // Handle success in try
    const response = await fetch('https://api.github.com/users/hazadus')
    const data = await response.json()
    console.log(data)
  } catch (error) {
    // Handle error in catch
    console.error(error)
  }
}
```
### Audio playback
[Аудиоплеер на JavaScript и HTML для чайников - ProgNote.ru](https://prognote.ru/web-dev/front-end/html-and-javascript-audio-player/)
[HTML Audio (w3schools.com)](https://www.w3schools.com/html/html5_audio.asp)
[HTML DOM Audio Object (w3schools.com)](https://www.w3schools.com/jsref/dom_obj_audio.asp)
[Create a Music Player using JavaScript - GeeksforGeeks](https://www.geeksforgeeks.org/create-a-music-player-using-javascript/)
```Bash
# Python Regexp
^\s*\[(\d{3})\]
```
CSS Styling: [https://svelte.dev/tutorial/deferred-transitions](https://svelte.dev/tutorial/deferred-transitions) (grid, labels with buttons)
### MediaSession API

> [!info] Customize media notifications and playback controls with the Media Session API  
> How to integrate with hardware media keys, customize media notifications, and more.  
> [https://web.dev/media-session/](https://web.dev/media-session/)  

> [!info] Media Session API - Web APIs | MDN  
> The Media Session API provides a way to customize media notifications.  
> [https://developer.mozilla.org/en-US/docs/Web/API/Media_Session_API](https://developer.mozilla.org/en-US/docs/Web/API/Media_Session_API)

----
📂 [[JavaScript]]