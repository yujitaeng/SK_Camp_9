/* 배열의 메소드 */

// indexOf, lastIndexOf, includes
const foodList = ['물회', '삼계탕', '냉면', '수박', '물회'];
console.log('===== indexOf =====');
console.log(foodList.indexOf('물회'));
console.log(foodList.indexOf('물회', 1));
console.log(foodList.lastIndexOf('물회'));
console.log(foodList.includes('목살'));

// push, pop
console.log("===== push & pop =====");
foodList.push('팥빙수');
console.log(foodList);
console.log(foodList.pop(), foodList);
console.log(foodList.pop(), foodList);
console.log(foodList.pop(), foodList);

// shift, unshift
const chickenList = ['후라이드', '양념', '파닭'];
console.log("===== shift & unshift =====");
console.log("origin chickenList:", chickenList);
chickenList.unshift('간장치킨');
chickenList.unshift('마늘치킨');
chickenList.unshift('스노윙치킨', '불닭');
console.log("after unshift:", chickenList);
console.log(chickenList.shift());
console.log(chickenList.shift());
console.log(chickenList.shift());
console.log("after shift:", chickenList);

// concat
// arr1.concat(arr2, ...);

// slice, splice
const front = ['HTML', 'CSS', 'JavaScript', 'BootStrap'];
console.log("===== slice & splice ====");
console.log("slice:", front.slice(1, 3));
console.log(front);
console.log("splice:", front.splice(3, 1, "jQuery"));
console.log(front);

// join
console.log(front.join());

// reverse
console.log(front.reverse());
