// Array Assignment
// Questions 1,2,3

var elements = ["Rose","Jasmin","Tulsi"];

// Question 1: loop over the array and print the elements
elements.forEach(element => {
    console.log(element);
});

// Question 2: Find the length of the array
console.log('Length of the array:', elements.length);

// Question 3: add an item to the front and end of the array
elements.unshift('Dalia'); 
elements.push('Sunflower');
console.log('Array after adding items:', elements);

// Question 4: remove an item from the front and end of the array
elements.shift();
elements.pop();
console.log('Array after removing items:', elements);