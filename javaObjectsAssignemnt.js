// Question1: Write a java script program to create an Object of student with key 
// value pairs(rollno,course,duration,start date,end date,garde) 
// and use get to display property value in the console and set method to assign value to properties


const student = {
    rollno: 123,
    course: "Computer Science",
    duration: "4 years",
    startDate: "2024-01-01",
    endDate: "2028-01-01",
    grade: "A",
    
    get rollNo() {
      console.log("Roll Number: " + this.rollno);
      return this.rollno;
    },
  
    get courseName() {
      console.log("Course: " + this.course);
      return this.course;
    },
  
    get courseDuration() {
      console.log("Duration: " + this.duration);
      return this.duration;
    },
  
    get start() {
      console.log("Start Date: " + this.startDate);
      return this.startDate;
    },
  
    get end() {
      console.log("End Date: " + this.endDate);
      return this.endDate;
    },
  
    get currentGrade() {
      console.log("Grade: " + this.grade);
      return this.grade;
    },
    set roll(roll) {
        this.rollno = roll;
      }
  };
console.log(student.rollNo);
console.log(student.courseName);
console.log(student.courseDuration);
console.log(student.start);
console.log(student.end);
console.log(student.currentGrade);
console.log(student.rollno = 555);

// Question 2: Iterate 

const person = {
    Name: "Johny",
    Age: 40,
    Cars: [
        {
            name: "ford",
            models: ["mustang", "Fiesta", "Mustang"]
        },
        {
            name: "BMW",
            models: ["320", "x3", "x5"]
        },
        {
            name: "fiat",
            models: ["500", "panda"]
        }
    ]
};

function displayProperties(obj) {
    for (const key in obj) {
        if (obj.hasOwnProperty(key)) {
            const value = obj[key];
            console.log(key + ": ");
            if (Array.isArray(value)) {
                value.forEach(item => {
                    if (typeof item === 'object') {
                        displayProperties(item);
                    } else {
                        console.log("  " + item);
                    }
                });
            } else {
                console.log("  " + value);
            }
        }
    }
}

displayProperties(person);

// Question 3: Write a JavaScript program to compare two objects to determine if the first one contains equivalent property values to the second one?

function containsEquivalentProperties(obj1, obj2) {
    for (const key in obj1) {
        if (obj1.hasOwnProperty(key)) {
            console.log("key.."+key)
            console.log("obj1Values.."+obj1[key])
            console.log("obj2Value.."+obj2[key])
            if (obj1[key] !== obj2[key]) {
                return false;
            }
        }
    }
    return true;
}

let obj1 = {                                   
    age: 23,
    degree: "CS"
}

let obj2 = {
    name: "John",
    age: 23,
    degree: "CS"
}

console.log(containsEquivalentProperties(obj1, obj2));



