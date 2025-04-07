/* let */

// 1. 변수 중복 선언 금지
// let, const 키워드로 선언된 변수는 동일 스코프 내 중복 선언 불가
let msg = '열심히 공부를 시작해 볼까요~';
// let msg = '빨간줄부터 뜨네요...';
msg = '이건 되지롱~';
console.log(msg);

// 2. 블럭 레벨 스코프
let i = 0;
for(let i = 0; i < 10; i++) {
    console.log(`${i}번째 실행중~~~`);
}
console.log(i);

// 3. 변수 호이스팅
// let 키워드로 선언한 변수는 변수 호이스팅이 발생하지 않는 것처럼 동작한다.
// 선언은 되었지만 초기화가 되지 않아 참조 시 오류가 발생하는 것이다.
console.log(test);
let test;
