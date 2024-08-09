## Language
### Docs

> [!info] Handbook - The TypeScript Handbook  
> Over 20 years after its introduction to the programming community, JavaScript is now one of the most widespread cross-platform languages ever created.  
> [https://www.typescriptlang.org/docs/handbook/intro.html](https://www.typescriptlang.org/docs/handbook/intro.html)  
### Basics
```TypeScript
let name : string;
let age: number | string; // 'union' -> 'age' could be any of two types!
age = 'thirty eight';
age = 38;
let isReady: boolean;
let hobbies: string[];  // array of strings
let role:[number, string]; // tuple - can contain one number, one string
let anyTypeVar: any;  // can be anything - not recommended!
let unknownTypeVar: unknown;  // better use this instead of above
// Declare object:
type Person = {
    name: string;
    age: number;
    size?: number; // optional property
};
// Declare and assign variable of new type:
let person: Person = {
    name: 'Sasha',
    age: 38
    // size is optional, so it may be not assigned
};
interface Kid {
    name : string;
    age : number;
};
interface Guy extends Kid {  // interface can be extended like this!
    hobby: string;
}
// Array of objects:
let people: Person[];
// role = [5, 5]; // Wrong!
role = [5, 'admin']; // OK!
function printName(name: string) {
    console.log(name);
}
let funcNew: Function;
let funcAgain: (name: string) => void; // returns undefined
let funcThree: (name: string) => never; // returns nothing
const handleOnSubmit = (event: React.FormEvent): boolean => {
	// ...
	return true;
}
```