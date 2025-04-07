/* 스프레드 문법을 이용한 배열/객체 복사 */

// 배열 복사
let arr = [2025, 4, 1];
let arrCopy1 = arr;         // 얕은 복사
let arrCopy2 = [...arr];    // 깊은 복사

arrCopy1.push(500);
console.log(arr, arrCopy1);

arrCopy2.push(700);
console.log(arr, arrCopy2);

// 객체 복사
let obj = {
    name: '다람쥐',
    job: '선생님'
};
let objCopy1 = obj;         // 얕은 복사
let objCopy2 = {...obj};    // 깊은 복사

console.log(objCopy2);
console.log(obj == objCopy1);
console.log(obj == objCopy2);