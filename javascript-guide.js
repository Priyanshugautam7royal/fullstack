// ============================================
// COMPLETE JAVASCRIPT GUIDE
// ============================================

// ============================================
// 1. VARIABLES AND DATA TYPES
// ============================================

// Variables: Used to store data values
// var: Old way (avoid using, has scope issues)
var name = "John";

// let: Block-scoped variable (preferred)
let age = 25;

// const: Constant variable (cannot be reassigned, preferred for non-changing values)
const PI = 3.14159;

// Data Types:
// String: Text values
let string = "Hello World";
let string2 = 'Single quotes also work';
let string3 = `Template literal: ${name} is ${age} years old`; // Used for string interpolation

// Number: Integer and decimal values
let integer = 42;
let decimal = 3.14;
let negative = -10;
let exponential = 5e2; // 500

// Boolean: True or false values
let isActive = true;
let isCompleted = false;

// Null: Intentional absence of value
let empty = null;

// Undefined: Variable declared but not assigned
let notAssigned;

// Symbol: Unique identifier
let sym = Symbol('unique');

// BigInt: For very large numbers
let bigNumber = 123456789012345678901234567890n;

// Array: Ordered collection of values
let fruits = ['apple', 'banana', 'orange'];

// Object: Collection of key-value pairs
let person = {
  name: "John",
  age: 25,
  city: "New York"
};

// ============================================
// 2. OPERATORS
// ============================================

// Arithmetic Operators: Perform mathematical operations
let a = 10;
let b = 3;
console.log(a + b);  // Addition: 13
console.log(a - b);  // Subtraction: 7
console.log(a * b);  // Multiplication: 30
console.log(a / b);  // Division: 3.333...
console.log(a % b);  // Modulus (remainder): 1
console.log(a ** 2); // Exponentiation: 100

// Assignment Operators: Assign values to variables
let x = 5;
x += 3;  // x = x + 3; Result: 8
x -= 2;  // x = x - 2; Result: 6
x *= 2;  // x = x * 2; Result: 12
x /= 3;  // x = x / 3; Result: 4

// Comparison Operators: Compare values and return true/false
console.log(5 == "5");   // Equal to (loose): true
console.log(5 === "5");  // Strictly equal to: false
console.log(5 != "5");   // Not equal to: false
console.log(5 !== "5");  // Strictly not equal: true
console.log(5 > 3);      // Greater than: true
console.log(5 < 3);      // Less than: false
console.log(5 >= 5);     // Greater than or equal: true
console.log(5 <= 3);     // Less than or equal: false

// Logical Operators: Combine boolean values
console.log(true && false);  // AND: false (both must be true)
console.log(true || false);  // OR: true (at least one must be true)
console.log(!true);          // NOT: false (inverts boolean)

// Ternary Operator: Shorthand if-else
let age2 = 20;
let status = age2 >= 18 ? "Adult" : "Minor"; // Used for simple conditional assignment

// Increment/Decrement Operators: Increase or decrease by 1
let count = 5;
count++;  // Increment: 6
count--;  // Decrement: 5

// ============================================
// 3. CONDITIONAL STATEMENTS
// ============================================

// If statement: Execute code if condition is true
let score = 80;
if (score >= 90) {
  console.log("Grade: A");
} else if (score >= 80) {
  console.log("Grade: B");
} else if (score >= 70) {
  console.log("Grade: C");
} else {
  console.log("Grade: F");
}

// Switch statement: Execute different blocks for different cases
let day = 3;
switch(day) {
  case 1:
    console.log("Monday");
    break; // Stop execution
  case 2:
    console.log("Tuesday");
    break;
  case 3:
    console.log("Wednesday");
    break;
  default:
    console.log("Other day");
}

// ============================================
// 4. LOOPS
// ============================================

// For loop: Repeat code for specific number of times
// Used when you know how many times to iterate
for (let i = 0; i < 5; i++) {
  console.log(i); // Prints 0, 1, 2, 3, 4
}

// While loop: Repeat code while condition is true
// Used when you don't know how many iterations
let i = 0;
while (i < 5) {
  console.log(i); // Prints 0, 1, 2, 3, 4
  i++;
}

// Do-while loop: Execute code first, then check condition
// Used when you need to run code at least once
let j = 0;
do {
  console.log(j);
  j++;
} while (j < 5);

// For-in loop: Iterate over object keys
// Used to loop through object properties
let user_1 = { name: "John", age: 25, city: "NYC" };
for (let key in user) {
  console.log(key + ": " + user[key]);
}

// For-of loop: Iterate over array values
// Used to loop through array elements
let colors = ["red", "green", "blue"];
for (let color of colors) {
  console.log(color);
}

// forEach: Built-in array method to loop through elements
// Used for array iteration with callback
colors.forEach((color, index) => {
  console.log(index + ": " + color);
});


// ============================================
// 5. ARRAYS , mutable
// ============================================

// Array declaration
let numbers = [1, 2, 3, 4, 5];
let mixed = [1, "hello", true, null];

// Access array elements using index (0-based)
console.log(numbers[0]); // 1
console.log(numbers[2]); // 3

// Array length
console.log(numbers.length); // 5

// Array methods:

// push(): Add element to end
numbers.push(6); // [1, 2, 3, 4, 5, 6]

// pop(): Remove element from end
numbers.pop(); // [1, 2, 3, 4, 5]

// unshift(): Add element to beginning
numbers.unshift(0); // [0, 1, 2, 3, 4, 5]

// shift(): Remove element from beginning
numbers.shift(); // [1, 2, 3, 4, 5]

// slice(): Extract part of array without modifying original
let sliced = numbers.slice(1, 3); // [2, 3]

// splice(): Add/remove elements from array (modifies original)
numbers.splice(2, 1, 10); // Remove 1 element at index 2, insert 10

// indexOf(): Find index of element
console.log(colors.indexOf("green")); // 1

// includes(): Check if array contains element
console.log(colors.includes("red")); // true

// join(): Combine array elements into string
console.log(colors.join(", ")); // "red, green, blue"

// split(): Convert string to array (opposite of join)
let text = "apple,banana,orange";
let fruits2 = text.split(","); // ["apple", "banana", "orange"]

// map(): Transform each element and return new array
let doubled = numbers.map(num => num * 2); // [2, 4, 6, 8, 10]

// filter(): Keep only elements that match condition
let even = numbers.filter(num => num % 2 === 0); // [2, 4]

// reduce(): Combine all elements into single value
let sum = numbers.reduce((total, num) => total + num, 0); // 15

// find(): Find first element matching condition
let found = numbers.find(num => num > 3); // 4

// reverse(): Reverse array order
let reversed = [1, 2, 3].reverse(); // [3, 2, 1]

// sort(): Sort array
let sorted = [3, 1, 4, 1, 5].sort(); // [1, 1, 3, 4, 5]

// ============================================
// 6.STRINGS , immutable
// ============================================

// String methods:


// length: Get number of characters
let text_ = "Hello World";
console.log(text_.length); // 11

// substring(): Extract part of string
console.log(text_.substring(0, 5)); // "Hello"

// slice(): Extract part of string (similar to array slice)
console.log(text_.slice(6)); // "World"

// indexOf(): Find position of substring
console.log(text_.indexOf("World")); // 6

// includes(): Check if string contains substring
console.log(text_.includes("World")); // true

// replace(): Replace substring with another
console.log(text_.replace("World", "Universe")); // "Hello Universe"

// toUpperCase() / toLowerCase(): Change case
console.log(text_.toUpperCase()); // "HELLO WORLD"
console.log(text_.toLowerCase()); // "hello world"

// trim(): Remove whitespace from both ends
let spacedText = "   Hello   ";
console.log(spacedText.trim()); // "Hello"

// split(): Convert string to array (opposite of join)
let words = text_.split(" "); // ["Hello", "World"]
  
// ============================================
// 7. FUNCTIONS
// ============================================

// Function declaration: Define reusable block of code
// Used to perform specific task
function greet(name) {
  return "Hello, " + name;
}
console.log(greet("John")); // "Hello, John"

// Function with default parameters
function add(a = 0, b = 0) {
  return a + b;
}
console.log(add(5, 3)); // 8

// Function expression: Store function in variable
// Used when you need to pass function as argument or return it
const multiply = function(a, b) {
  return a * b;
};
console.log(multiply(4, 5)); // 20

// Arrow function: Short syntax for functions
// Used for cleaner, concise function writing
const square = (num) => {
  return num * num;
};
const square2 = (num) => num * num; // Single line arrow function

// Function with multiple parameters
function calculateTotal(price, quantity, tax = 0.1) {
  return (price * quantity) * (1 + tax);
}

// Function with no return value
function printMessage(msg) {
  console.log(msg);
}

// Function returning multiple values using object
function getUserInfo() {
  return {
    name: "John",
    age: 25,
    email: "john@example.com"
  };
}

// Function with rest parameters (multiple arguments)
// Used to accept any number of arguments
function sumAll(...numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}
console.log(sumAll(1, 2, 3, 4, 5)); // 15

// ============================================
// 8. OBJECTS
// ============================================

// Object literal: Collection of key-value pairs
// Used to group related data
let student = {
  name: "Alice",
  age: 20,
  grade: "A",
  courses: ["Math", "Science", "English"],
  
  // Method: Function inside object
  getInfo: function() {
    return this.name + " is " + this.age + " years old";
  }
};

// Access object properties
console.log(student.name);        // "Alice"
console.log(student["age"]);      // 20
console.log(student.getInfo());   // "Alice is 20 years old"

// Add new property
student.city = "Boston";

// Modify existing property
student.age = 21;

// Delete property
delete student.city;

// Check if property exists
console.log("name" in student);   // true

// Get object keys
console.log(Object.keys(student)); // ["name", "age", "grade", "courses", "getInfo"]

// Get object values
console.log(Object.values(student)); // ["Alice", 21, "A", [...], ...]

// Destructuring: Extract values from object
let { name: studentName, age: studentAge } = student;
console.log(studentName, studentAge); // "Alice", 21

// ============================================
// 9. SPREAD OPERATOR
// ============================================

// Spread operator: Expand array or object elements
// Used to copy, merge, or pass multiple arguments

// Array spread
let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];
let combined = [...arr1, ...arr2]; // [1, 2, 3, 4, 5, 6]

// Object spread
let obj1 = { name: "John", age: 25 };
let obj2 = { city: "NYC", country: "USA" };
let mergedObj = { ...obj1, ...obj2 };

// ============================================
// 10. DOM (DOCUMENT OBJECT MODEL)
// ============================================

// DOM: Represents HTML structure as objects
// Used to access and manipulate HTML elements

// Select single element by ID
let element = document.getElementById("myId");

// Select single element by selector
let element2 = document.querySelector(".myClass");

// Select all elements by class
let elements = document.querySelectorAll(".myClass");

// Select by tag name
let paragraphs = document.getElementsByTagName("p");

// Get element properties
console.log(element.textContent);  // Get text content
console.log(element.innerHTML);    // Get HTML content
console.log(element.value);        // Get form input value

// Set element properties
element.textContent = "New text";
element.innerHTML = "<p>New HTML</p>";
element.style.color = "red";

// Add/remove CSS classes
element.classList.add("active");
element.classList.remove("hidden");
element.classList.toggle("selected");

// Get/set attributes
element.getAttribute("data-id");
element.setAttribute("data-id", "123");
element.removeAttribute("data-id");

// Create new element
let newDiv = document.createElement("div");
newDiv.textContent = "Hello";
newDiv.className = "container";

// Add element to DOM
document.body.appendChild(newDiv);

// Insert before another element
let parent = document.querySelector(".container");
let newP = document.createElement("p");
parent.insertBefore(newP, parent.firstChild);

// Remove element
element.remove();

// Get parent, children elements
let parent2 = element.parentElement;
let children = element.children;
let firstChild = element.firstChild;

// ============================================
// 11. EVENTS
// ============================================

// Events: Actions triggered by user interaction
// Used to respond to user actions

// Click event
let button = document.querySelector("button");
button.addEventListener("click", function(event) {
  console.log("Button clicked!");
});

// Using arrow function
button.addEventListener("click", (event) => {
  console.log("Clicked");
});

// Other common events:
// Input event: When user types in form field
let input = document.querySelector("input");
input.addEventListener("input", (e) => {
  console.log(e.target.value); // Get input value
});

// Change event: When form value changes
input.addEventListener("change", (e) => {
  console.log("Value changed to: " + e.target.value);
});

// Submit event: When form is submitted
let form = document.querySelector("form");
form.addEventListener("submit", (e) => {
  e.preventDefault(); // Prevent page reload
  console.log("Form submitted");
});

// Mouse events
document.addEventListener("mouseover", (e) => {
  console.log("Mouse over element");
});

document.addEventListener("mouseout", (e) => {
  console.log("Mouse left element");
});

// Keyboard events
document.addEventListener("keydown", (e) => {
  console.log("Key pressed: " + e.key);
});

document.addEventListener("keyup", (e) => {
  console.log("Key released: " + e.key);
});

// Load event: Page has finished loading
window.addEventListener("load", () => {
  console.log("Page loaded");
});

// Remove event listener
// button.removeEventListener("click", functionName);

// ============================================
// 12. CALLBACKS
// ============================================

// Callback: Function passed as argument to another function
// Used to execute code after async operation completes

// Simple callback example
function greetUser(name, callback) {
  console.log("Hello " + name);
  callback(); // Execute the callback function
}

greetUser("John", function() {
  console.log("Nice to meet you!");
});

// Callback with parameters
function processData(data, callback) {
  // Do some processing
  callback(data * 2); // Pass result to callback
}

processData(5, function(result) {
  console.log("Result: " + result); // Result: 10
});

// Array methods use callbacks
let numbers2 = [1, 2, 3, 4, 5];

// map callback
numbers2.map((num) => {
  return num * 2;
});

// filter callback
numbers2.filter((num) => {
  return num > 2;
});

// forEach callback
numbers2.forEach((num, index) => {
  console.log(index + ": " + num);
});

// Callback hell: Multiple nested callbacks (avoid this!)
// function getData(callback) {
//   setTimeout(() => {
//     callback(data);
//   }, 1000);
// }

// ============================================
// 13. PROMISES
// ============================================

// Promise: Handle async operations more cleanly than callbacks
// Used for async operations like API calls, file reading

// Create a promise
let myPromise = new Promise((resolve, reject) => {
  let success = true;
  
  if (success) {
    resolve("Operation successful!"); // Success
  } else {
    reject("Operation failed!");       // Error
  }
});

// Use promise with .then() and .catch()
myPromise
  .then((result) => {
    console.log(result); // Handle success
  })
  .catch((error) => {
    console.log(error);  // Handle error
  });

// Promise chaining
myPromise
  .then((result) => {
    console.log(result);
    return result + " More";
  })
  .then((newResult) => {
    console.log(newResult);
  })
  .catch((error) => {
    console.log(error);
  });

// ============================================
// 14. ASYNC/AWAIT
// ============================================

// Async/Await: Cleaner way to handle promises
// Used for readable async code

// Async function always returns promise
async function fetchData() {
  try {
    // Wait for promise to resolve
    let response = await myPromise;
    console.log(response);
    return response;
  } catch (error) {
    console.log(error); // Handle error
  }
}

// Call async function
// fetchData();

// ============================================
// 15. FETCH API
// ============================================

// Fetch API: Request data from server
// Used to get JSON data, images, etc. from URLs

// Basic fetch: GET request
fetch("https://api.example.com/users")
  .then((response) => {
    // Check if response is successful
    if (!response.ok) {
      throw new Error("Network response error");
    }
    return response.json(); // Convert response to JSON
  })
  .then((data) => {
    console.log(data); // Use the data
  })
  .catch((error) => {
    console.log("Error: " + error); // Handle errors
  });

// Fetch with async/await (cleaner)
async function getUsers() {
  try {
    let response = await fetch("https://api.example.com/users");
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.log("Error: " + error);
  }
}

// POST request: Send data to server
async function createUser(userData) {
  try {
    let response = await fetch("https://api.example.com/users", {
      method: "POST",           // Request type
      headers: {
        "Content-Type": "application/json" // Data type
      },
      body: JSON.stringify(userData) // Convert object to JSON string
    });
    let data = await response.json();
    console.log("User created:", data);
  } catch (error) {
    console.log("Error: " + error);
  }
}

// PUT request: Update data
async function updateUser(id, userData) {
  let response = await fetch("https://api.example.com/users/" + id, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(userData)
  });
  let data = await response.json();
  return data;
}

// DELETE request: Remove data
async function deleteUser(id) {
  let response = await fetch("https://api.example.com/users/" + id, {
    method: "DELETE"
  });
  console.log("User deleted");
}

// ============================================
// 16. CLASSES
// ============================================

// Classes: Blueprint for creating objects
// Used to organize related data and functions

// Class declaration
class Car {
  // Constructor: Initialize object properties
  constructor(brand, model, year) {
    this.brand = brand;
    this.model = model;
    this.year = year;
  }
  
  // Methods: Functions inside class
  getInfo() {
    return this.brand + " " + this.model + " (" + this.year + ")";
  }
  
  // Method that modifies properties
  updateYear(newYear) {
    this.year = newYear;
  }
}

// Create instance of class
let myCar = new Car("Toyota", "Camry", 2020);
console.log(myCar.getInfo()); // "Toyota Camry (2020)"

// Access properties
console.log(myCar.brand); // "Toyota"

// Call methods
myCar.updateYear(2023);

// Static methods: Can be called on class itself, not instance
class MathUtil {
  static add(a, b) {
    return a + b;
  }
}
console.log(MathUtil.add(5, 3)); // 8

// Inheritance: Extend class from another class
// Used to share properties and methods
class Vehicle {
  constructor(brand) {
    this.brand = brand;
  }
  
  getInfo() {
    return "Brand: " + this.brand;
  }
}

class Truck extends Vehicle {
  constructor(brand, capacity) {
    super(brand); // Call parent constructor
    this.capacity = capacity;
  }
  
  // Override parent method
  getInfo() {
    return super.getInfo() + " Capacity: " + this.capacity; // Use parent method
  }
}

let myTruck = new Truck("Ford", 1000);
console.log(myTruck.getInfo()); // "Brand: Ford Capacity: 1000"

// Getters and Setters
class Person {
  constructor(firstName, lastName) {
    this._firstName = firstName;
    this._lastName = lastName;
  }
  
  // Getter: Get property value
  get fullName() {
    return this._firstName + " " + this._lastName;
  }
  
  // Setter: Set property value
  set fullName(name) {
    let parts = name.split(" ");
    this._firstName = parts[0];
    this._lastName = parts[1];
  }
}

let person2 = new Person("John", "Doe");
console.log(person2.fullName); // "John Doe"
person2.fullName = "Jane Smith";
console.log(person2.fullName); // "Jane Smith"

// ============================================
// 17. CLOSURES
// ============================================

// Closure: Function that "remembers" variables from outer scope
// Used for data privacy and creating function factories

function counter() {
  let count = 0; // Private variable
  
  return function() {
    count++; // Can access outer function's variable
    return count;
  };
}

let increment = counter();
console.log(increment()); // 1
console.log(increment()); // 2
console.log(increment()); // 3

// Closure for private data
function createUser(name) {
  let password = "secret123"; // Private - not accessible directly
  
  return {
    getName: function() {
      return name;
    },
    checkPassword: function(pwd) {
      return password === pwd;
    }
  };
}

let user = createUser("John");
console.log(user.getName()); // "John"
// console.log(user.password); // undefined (private)

// ============================================
// 18. ERROR HANDLING
// ============================================

// Try-catch: Handle errors gracefully
// Used to prevent app from crashing

try {
  // Code that might cause error
  let x = someUndefinedVariable;
} catch (error) {
  console.log("Error caught: " + error.message);
} finally {
  // Runs regardless of error
  console.log("This always runs");
}

// Throw custom error
function validateAge(age) {
  if (age < 0) {
    throw new Error("Age cannot be negative"); // Throw error
  }
  return true;
}

try {
  validateAge(-5);
} catch (error) {
  console.log(error.message); // "Age cannot be negative"
}

// ============================================
// 19. TEMPLATE LITERALS (STRING INTERPOLATION)
// ============================================

// Template literals: Use backticks for string interpolation
// Used for readable multi-line strings and variable insertion

let firstName = "John";
let lastName = "Doe";
let age3 = 30;

// String concatenation (old way)
let oldWay = "My name is " + firstName + " " + lastName + " and I am " + age3;

// Template literal (new way)
let newWay = `My name is ${firstName} ${lastName} and I am ${age3}`;
console.log(newWay);

// Multi-line strings
let multiLine = `
  This is a long
  multi-line string
  that spans multiple
  lines without concatenation
`;

// ============================================
// 20. DESTRUCTURING
// ============================================

// Destructuring: Extract values from arrays or objects
// Used for cleaner variable assignment

// Array destructuring
let [a2, b2, c2] = [1, 2, 3];
console.log(a2); // 1
console.log(b2); // 2

// Skip elements
let [first, , third] = [1, 2, 3];
console.log(first); // 1
console.log(third); // 3

// Object destructuring
let { name: personName, age: personAge } = { name: "John", age: 25 };
console.log(personName); // "John"
console.log(personAge);  // 25

// Default values
let { country = "USA" } = { name: "John" };
console.log(country); // "USA"

// ============================================
// 21. JSON (JAVASCRIPT OBJECT NOTATION)
// ============================================

// JSON: Format for storing and exchanging data
// Used to send/receive data from servers

// JavaScript object
let employee = {
  name: "John",
  position: "Developer",
  salary: 50000,
  skills: ["JavaScript", "Python", "React"]
};

// Convert object to JSON string
let jsonString = JSON.stringify(employee);
console.log(jsonString); // '{"name":"John","position":"Developer",...}'

// Convert JSON string back to object
let parsedObject = JSON.parse(jsonString);
console.log(parsedObject.name); // "John"

// Pretty print JSON (with indentation)
let prettyJson = JSON.stringify(employee, null, 2);

// ============================================
// 22. REGULAR EXPRESSIONS
// ============================================

// RegEx: Pattern for matching text
// Used for validation, search, replace

// Create regex
let pattern = /hello/i; // 'i' = case insensitive
let pattern2 = new RegExp("hello", "i");

// Test if pattern matches
console.log(pattern.test("Hello World")); // true

// Get matching text
console.log("Hello World".match(/hello/i)); // ["Hello", ...]

// Replace matching text
console.log("Hello World".replace(/hello/i, "Hi")); // "Hi World"

// Common patterns:
// \d: Match digit
// \w: Match word character
// \s: Match whitespace
// .: Match any character
// *: 0 or more
// +: 1 or more
// ?: 0 or 1
// ^: Start of string
// $: End of string
// [abc]: Match a, b, or c
// [0-9]: Match any digit

// Email validation
let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
console.log(emailPattern.test("john@example.com")); // true
console.log(emailPattern.test("invalid-email"));    // false

// ============================================
// 23. USEFUL TIPS AND TRICKS
// ============================================

// 1. Nullish coalescing: Use default if value is null/undefined
let value = null;
let result = value ?? "default"; // "default"

// 2. Optional chaining: Safely access nested properties
let user2 = { profile: { name: "John" } };
console.log(user2.profile?.name);     // "John"
console.log(user2.address?.street);   // undefined (no error)

// 3. Array includes for checking
let items = ["apple", "banana", "orange"];
console.log(items.includes("apple")); // true

// 4. Set for unique values
let uniqueNumbers = new Set([1, 2, 2, 3, 3, 4]);
console.log(uniqueNumbers); // Set { 1, 2, 3, 4 }

// 5. Map for key-value storage
let userMap = new Map();
userMap.set("user1", { name: "John", age: 25 });
userMap.set("user2", { name: "Jane", age: 30 });
console.log(userMap.get("user1")); // { name: "John", age: 25 }

// 6. Object.assign for merging objects
let obj_1 = { a: 1, b: 2 };
let obj_2 = { b: 3, c: 4 };
let merged = Object.assign({}, obj_1, obj_2); // { a: 1, b: 3, c: 4 }

// 7. Logical operators for conditional assignment
let isLoggedIn = true;
let username = isLoggedIn && "JohnDoe"; // "JohnDoe"

// 8. Array sorting with custom function
let numbers3 = [3, 1, 4, 1, 5];
numbers3.sort((a, b) => a - b); // [1, 1, 3, 4, 5]

// 9. Debounce function (execute after delay)
function debounce(func, delay) {
  let timeout;
  return function(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), delay);
  };
}

// 10. setTimeout and setInterval for timing
// setTimeout: Execute code after delay (one time)
setTimeout(() => {
  console.log("Executed after 2 seconds");
}, 2000);

// setInterval: Execute code repeatedly
// let intervalId = setInterval(() => {
//   console.log("Repeats every 1 second");
// }, 1000);
// clearInterval(intervalId); // Stop interval

// ============================================
// END OF JAVASCRIPT GUIDE
// ============================================
