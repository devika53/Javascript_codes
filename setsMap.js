// Question:1 Create a set with some numbers and remove the odd numbers from it.Iterate the set with for...of 


const numberSet = new Set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
 

for (let number of numberSet) {
  if (number % 2 !== 0) { 
    numberSet.delete(number);   
  }
}
console.log(numberSet)


// Question 2: Create weakSet with Person object(having properties name,age,email).Write code to add an object
// delete object,check an object is present.

const weakSet = new WeakSet();

let person = {
    name: 'devika',
    age: "27",
    email: "devika@gmail.com"
}

weakSet.add(person);
console.log(weakSet.has(person));
weakSet.delete(person);

// Question 3:  Create a Map object Activity with key value pair activities and status.


function countActivity(activityMap) {
  let completedCount = 0;
  let todoCount = 0;
  let inProgressCount = 0;
  for (const [activity, status] of activityMap) {
      switch (status) {
          case 'completed':
              completedCount++;
              break;
          case 'todo':
              todoCount++;
              break;
          case 'in progress':
              inProgressCount++;
              break;
          default:
              console.log(`Unknown status for ${activity}`);
      }
  }
  return {
      completed: completedCount,
      todo: todoCount,
      inProgress: inProgressCount
  };
}
const activityMap = new Map();
activityMap.set("Day1 note learning", "completed");
activityMap.set("Day1 assignments", "in progress");
activityMap.set("Day1 mcq", "todo");
activityMap.set("Day2 mcq", "in progress");

const statusCounts = countActivity(activityMap);
console.log(statusCounts);
