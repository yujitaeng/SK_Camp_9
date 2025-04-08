/* Array distructuring assignment (배열 구조 분해 할당) */

// 1. 기본 문법
let nameArr = ['Squirrel', 'Nam'];

// let firstName = nameArr[0];
// let lastName = nameArr[1];

let [firstName, lastName] = nameArr;

console.log(`저는 ${lastName}가 ${firstName}입니다.`);

let [firstName2, lastName2] = "다람쥐 남".split(" ");

console.log(`저는 ${lastName2}가 ${firstName2}입니다.`);

let lunchArr = ['더블비프치즈버거', '감자튀김', '치즈스틱', '제로콜라'];
let [burger, , , drink] = lunchArr;
console.log(burger + "랑 " + drink + "만 먹을 거야! 다이어트 중이니까~");

// 2. 활용: 객체 프로퍼티 할당
let user = {};
[user.firstName, user.lastName] = "Squirrel Nam".split(" ");
console.log(user);

// 3. 활용: Object.entries()와 조합
console.log(Object.entries(user));

for (let [key, value] of Object.entries(user)) {
    console.log(key);
    console.log(value);
}

// 4. 활용: 변수 교환
let cup1 = "오렌지주스";
let cup2 = "아메리카노";

[cup1, cup2] = [cup2, cup1];

// let temp = cup1;
// cup1 = cup2;
// cup2 = temp;
console.log(cup1, cup2);

// 5. 활용: rest parameters와 조합
let [king, queen, jack, ace, ...numbers] = ["KING", "QUEEN", "JACK", "ACE", 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(king);
console.log(queen);
console.log(jack);
console.log(ace);
console.log(numbers);

// 6. 활용: 기본값 설정 가능
let userArr = ["다람쥐", 190, "서울시 금천구"];

let [name="아무개", height, address, job="강사", skill="LLM"] = userArr;

console.log(name, height, address, job, skill);
