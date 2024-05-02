// Question1: Write a java script program to create an Object of student with key 
// value pairs(rollno,course,duration,start date,end date,garde) 
// and use get to display property value in the console and set method to assign value to properties


class Student {
    constructor(rollno, course, duration, startDate, endDate, grade) {
        this._rollno = rollno;
        this._course = course;
        this._duration = duration;
        this._startDate = startDate;
        this._endDate = endDate;
        this._grade = grade;
    }

    // Getters
    get rollno() {
        return this._rollno;
    }

    get course() {
        return this._course;
    }

    get duration() {
        return this._duration;
    }

    get startDate() {
        return this._startDate;
    }

    get endDate() {
        return this._endDate;
    }

    get grade() {
        return this._grade;
    }

    // Setters
    set rollno(newRollno) {
        this._rollno = newRollno;
    }

    set course(newCourse) {
        this._course = newCourse;
    }

    set duration(newDuration) {
        this._duration = newDuration;
    }

    set startDate(newStartDate) {
        this._startDate = newStartDate;
    }

    set endDate(newEndDate) {
        this._endDate = newEndDate;
    }

    set grade(newGrade) {
        this._grade = newGrade;
    }
}
let student = new Student(123, 'Computer Science', '4 years', '2020-08-01', '2024-07-31', 'A');

//getters
console.log('Student Roll No:', student.rollno);
console.log('Student Course:', student.course);
console.log('Duration of Course:', student.duration);
console.log('Course Start Date:', student.startDate);
console.log('Course End Date:', student.endDate);
console.log('Student Grade:', student.grade);

//setters
student.rollno = 124;
student.grade = 'A+';

console.log('Updated Student Roll No:', student.rollno);
console.log('Updated Student Grade:', student.grade);


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

