/* 함수 호이스팅 */

/*
    함수 선언문은 런타임 이전에 JS 엔진에 의해 먼저 실행된다.
    따라서 함수 선언문 이전에 해당 함수를 참조하거나 호출할 수 있다.
    이를 JS 고유의 특징, 함수 호이스팅이라고 한다.

    단, 변수 할당문의 값은 런타임에 평가되므로
    함수 표현식으로 정의한 함수는 반드시 함수 표현식 이후에 참조 또는 호출해야 한다.
*/

console.log(hello);
console.log(hello('다람쥐'));

console.log(hi);
console.log(hi('다람쥐'));

function hello(name) {
    return `Hello, ${name}!`;
}

var hi = function(name) {
    return `하이루 ${name}~!`;
}