/* property */
// 객체는 프로퍼티의 집합이며, 프로퍼티는 키와 값으로 구성된다.

var idol = {
    name: 'BTS',
    count: 7
};

// 다양한 프로퍼티 key
var testObj = {
    normal: 'normal value',
    '@ s p a c e @': 'space value', // 오류 발생하지 않음
    '': '',                         // 오류는 발생하지 않으나 권장하지 않음
    0: 1,                           // key가 내부적으로 문자열 변환됨
    var: 'var',                     // 오류는 발생하지 않으나 권장하지 않음
    normal: 'new normal value'      // 같은 key는 나중에 추가한 value로 덮어씌워짐
};

var key = 'testKey';
testObj[key] = 'testValue';

console.log(testObj);

/* 프로퍼티 값 단축 구문 */
var productName = "Mac Mini";
var price = 9999999;

var product = {
    productName: productName,
    price: price
};
console.log(product);

var product2 = { productName, price };
console.log(product2);