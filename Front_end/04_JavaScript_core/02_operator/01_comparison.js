/* 비교 연산자 */

/*
- 동등 비교 ==, != : 암묵적 타입 변환을 통해 같은 값인지 비교
- 일치 비교 ===, !== : 타입과 값이 모두 일치하는지 비교
*/

console.log("====숫자 1 vs 문자 '1' vs true====")
console.log(`1 == '1' : ${1 == '1'}`)      // true
console.log(`1 == true : ${1 == true}`)    // true
console.log(`1=== '1' : ${1 === '1'}`)     // false
console.log(`1 === true : ${1 === true}`)  // false

console.log("====null vs undefined====")
console.log(`null == undefined : ${null == undefined}`)      // true
console.log(`null === undefined : ${null === undefined}`)    // false

console.log("====문자열 'hello' vs 문자열 'hello'====")
console.log(`'hello' == 'hello' : ${'hello' == 'hello'}`)    // true
console.log(`'hello' === 'hello' : ${'hello' === 'hello'}`)  // true

console.log("====NaN vs NaN====")
console.log(`NaN == NaN : ${NaN == NaN}`)       // false
console.log(`NaN === NaN : ${NaN === NaN}`)     // false
console.log(`NaN 확인법 Number.isNaN(): ${Number.isNaN(NaN)}`)   // true
