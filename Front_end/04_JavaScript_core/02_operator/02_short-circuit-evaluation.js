/* 단축 평가 */
/* 표현식을 평가하는 도중 평가 결과가 확정된 경우 나머지 평가 과정을 생략하는 것 */

/*
 * 논리 연산자
 * and &&
 * or  ||
 * not !
 */

// OR
console.log('apple' || 'banana');
console.log(false || 'banana');
console.log('apple' || false);

// AND
console.log('apple' && 'banana');
console.log(false && 'banana');
console.log('apple' && false);

// if문 대체
var num = 101;

if (num % 2 == 0) {
    console.log('짝수');
} else {
    console.log('홀수');
}

num % 2 == 0 && console.log('짝수');
num % 2 == 0 || console.log('홀수');

// 객체로 기대되는 변수가 null 또는 undefined가 아닌지 확인하고
// 프로퍼티를 참조할 때 단축 평가를 유용하게 활용할 수 있음
var obj = null;
// var val = obj.value;
var val = obj && obj.value;
console.log(val);
