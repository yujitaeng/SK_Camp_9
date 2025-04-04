/* optional chaining operator */

/*
    ?.
    - ES11에서 도입된 연산자
    - 좌항의 피연산자가 null 또는 undefined인 경우 undefined 반환
    - 그렇지 않으면 우항의 프로퍼티 참조
*/

var obj = null;

// var val = obj.value;
var val = obj?.value;

var str = "";

var len = str.length;
console.log("len: " + len);

var len = str && str.length;
console.log("len: " + len);

var len = str?.length;
console.log("len: " + len);