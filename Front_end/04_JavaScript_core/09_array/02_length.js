/* array length */

const arr = [1, 2, 3, 4, 5];
console.log(arr.length);

// lenght 프로퍼티 동적으로 갱신된다.
arr.push(6);
console.log(arr.length);
arr.pop();
console.log(arr.length);

// length를 기존 길이보다 작게 조절하면 배열 요소도 조절된다.
arr.length = 3;
console.log(arr);

// length를 기존 길이보다 늘이면 빈 공간이 추가될 뿐이다.
arr.length = 7;
console.log(arr);
console.log(Object.getOwnPropertyDescriptors(arr));

// JS는 배열 요소 일부가 비어있는 배열 문법적으로 허용한다.
const arr2 = [1, , , , 5];
console.log(arr2);
console.log(arr2.length);
console.log(Object.getOwnPropertyDescriptors(arr2));
