// String assignment:
// Questions 1,2,3
//Question 1: Remove all space in the sentence
var question = "Hello Hai How are you?";

var questionSpace = question.replace(/\s+/g, '');
console.log(questionSpace);

// Question 2: Extract the word 'hai' from the string
var questionExtracted = question.match(/hai/i);
console.log(questionExtracted ? questionExtracted[0] : 'Word not found');

// Question 3: Check whether the sentence contains the word 'hello'
let containsHello = /hello/i.test(question);
console.log(containsHello);

// Questions 4,5,6
// Question 4: Using match method find the occurrence of 'are' and 'xyz' in the i/p string
var inputString = 'We are what we believe we are.';
var matchesAre = inputString.match(/are/g);
console.log('Occurrences of "are":', matchesAre ? matchesAre.length : 0);
var matchesXyz = inputString.match(/xyz/g);
console.log('Occurrences of "xyz":', matchesXyz ? matchesXyz.length : 0);

// Question 5: Using test method check wheteher the sentence contains 'what'
var containsWhat = /what/.test(inputString);
console.log(containsWhat);

//Question 6: Find how many times the word 'are' occur in the sentence
var countAre = inputString.match(/\bare\b/g);
console.log('The word "are" occurs:', countAre ? countAre.length : 0);

// Question 7: Replace 'hello' with 'hai' in the sentence 'hello how are you?'
var sentence = 'hello how are you?';
var modifiedSentence = sentence.replace('hello', 'hai');
console.log(modifiedSentence);

// Question 8: Replace all the occurrence of 'we' with 'I am' in the sentence 'We are what we believe we are.'
var sentence = 'We are what we believe we are.';
var modifiedSentence = sentence.replace(/\bwe\b/gi, 'I am');
console.log(modifiedSentence);




