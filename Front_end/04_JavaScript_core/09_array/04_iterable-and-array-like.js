/* iterable & array-like */

/*
    iterable: Symbol.iterator 메서드가 구현된 객체
    유사배열(array-like): 인덱스와 length 프로퍼티가 있어 
                        배열처럼 보이는 객체

    - 이터러블이면서 유사 배열일 수 있고
    - 이터러블 객체라고 해서 유사 배열 객체는 아니며
    - 유사 배열 객체라고 해서 이터러블 객체인 것도 아니다.
*/

// 유사 배열 객체
let arrayLike = {
    0: "배열인듯",
    1: "배열아닌",
    2: "배열같은",
    3: "유사배열",
    length: 4
};

// console.log(arrayLike.pop());

// 이터러블 객체 (Symbol.iterator 구현)
let range = {
    from: 1,
    to: 5
};

range[Symbol.iterator] = function() {
    return {
        current: this.from,
        last: this.to,
        next() {
            if(this.current <= this.last) {
                return {done: false, value: this.current++};
            } else {
                return {done: true};
            }
        }
    }
};

// console.log(range.pop());

/*
    Array.from()은 넘겨받은 인수가 이터러블이나 유사 배열인 경우,
    새로운 배열을 만들고 객체의 모든 요소를 새롭게 만든 배열로 복사한다.
*/
let arr = Array.from(arrayLike);
console.log(arr.pop());

let arr2 = Array.from(range);
console.log(arr2.pop());

// Array.from()에는 매핑(mapping) 함수를 선택적으로 넘겨줄 수 있다.
// 요소를 배열에 추가하기 전 각 요소를 대상으로 매핑 함수를 적용해 반환된 값을 추가한다.
let arr3 = Array.from(range, num => num * num);
console.log(arr3);
