/* Nested distructuring (중첩 구조 분해) */
let lunchSet = {
    burger: {
        main: '소고기',
        sub: '치즈',
        vegetable: '양상추'
    },
    side: ['감자튀김', '코울슬로'],
    price: 18000
};

let {burger:{main, sub, vegetable}, side:[side1, side2], price} = lunchSet;

// console.log(burger, side, price);
console.log(`burger = ${main} + ${sub} + ${vegetable}`);
console.log(`side = ${side1}, ${side2}`);
console.log(price + "원");



/* function parameters (함수 파라미터) */
// JS 파라미터는 키워드 인자가 없다.
// 따라서 인수의 순서가 고정되며, 기본값을 설정하더라도 undefined로 자리를 맞춰야 한다.
function displayProduct(producer="아무개", width=0, height=0, items=[]) {
    console.log('==============================');
    console.log(`${producer} made`);
    console.log(`${width} * ${height}`);
    console.log(items);
    console.log('==============================');
}

displayProduct("다람쥐", 100, 200, ["도토리", "밤", "호두"]);
displayProduct("다람쥐", ["도토리", "밤", "호두"]);
displayProduct("다람쥐", undefined, undefined, ["도토리", "밤", "호두"]);

// 구조 분해 할당을 이용하면 파이썬의 키워드 인자처럼 사용할 수 있다.
// 순서도 무관하고 기본 값을 활용할 때에도 별도의 처리가 필요 없다.
function displayProductObject({producer="아무개", width=0, height=0, items=[]}) {
    console.log('==============================');
    console.log(`${producer} made`);
    console.log(`${width} * ${height}`);
    console.log(items);
    console.log('==============================');
}

let example = {
    producer: '다람쥐',
    // width: 100,
    // height: 100,
    items: ["호두", "밤", "도토리"]
};

displayProductObject(example);
