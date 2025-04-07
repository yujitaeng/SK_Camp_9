/* const */

/*
    const 키워드는 상수(constant) 선언을 위해 사용한다.
    let 키워드와 마찬가지로 블록 레벨 스코프를 가지며
    변수 호이스팅이 발생하지 않는 것처럼 동작한다.
    (* 상수: 재할당이 금지된 변수)
*/

// 1. 선언과 동시에 초기화해야 한다.
// const TEST;
const TEST = 1;

// 2. const 키워드로 선언한 변수는 재할당이 금지된다.
// TEST = 100;

// const 키워드로 선언한 변수에 객체를 할당한 경우,
// property 값은 변경할 수 있다. (단, 재할당은 불가하다.)
const student = {
    name: "SKN 9기",
    count: 21
};

student.name = "멋있는 9기";
console.log(student);

student.studyTime = 960;
console.log(student);

student = {};
