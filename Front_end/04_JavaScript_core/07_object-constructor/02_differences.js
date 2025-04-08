/* 생성자 함수 vs 일반 함수 */

function Student(name, hobby) {
    this.name = name;
    this.hobby = hobby;
    this.getInfo = function() {
        return `${this.name}의 취미는 ${this.hobby} 입니다.`;
    };
}

// new 연산자와 함께 호출해야 생성자 함수로 동작한다.
// (그렇지 않으면 일반 함수로 동작한다.)
const student = Student('다람쥐', '맛집 탐방');
console.log(student);
console.log(hobby);

// new.target (생성자 함수가 new 연산자 없이 호출되는 것을 방지하기 위해 ES6에서 지원)
// - new 연산자와 함께 생성자 함수로서 호출 시, 함수 자기 자신을 가리킴
// - new 연산자 없이 일반 함수로서 호출 시, 함수 내부의 new.target === undefined
function Dog(name, skill) {

    // console.log(new.target);
    if(!new.target) {
        return new Dog(name, skill);
    }

    this.name = name;
    this.skill = skill;
}

const dog1 = Dog('뽀삐', '손!');
console.log(dog1);

const dog2 = new Dog('먼지', '앉아!');
console.log(dog2);

// 내장 생성자 함수는 new 연산자 없이 사용해도 빈 객체를 반환하는 식으로 잘 동작하게 만들어짐
const obj = Object();
console.log(obj);
