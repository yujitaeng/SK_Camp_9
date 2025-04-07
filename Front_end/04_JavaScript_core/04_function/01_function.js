/* function */

// 함수 선언문
function returnHello(name) {
    return `${name}님 안녕하세요 :)`;
}

// 함수 표현식
var returnHello = function returnHello(name) {
    return `${name}님 안녕하세요 :)`;
};

var returnHello = function (name) {
    return `${name}님 안녕하세요 :)`;
};

var returnHello = function hello (name) {
    return `${name}님 안녕하세요 :)`;
};

console.log(returnHello('다람쥐'));
// console.log(hello('다람쥐'));
// 함수 표현식에서 함수명은 써도 되고 생략해도 되고 같아도 되고 달라도 되지만
// 함수명과 변수명이 다른 경우, 함수명으로 호출은 불가능하다.
