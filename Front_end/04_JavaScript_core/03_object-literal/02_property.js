/* property */
// 객체는 프로퍼티의 집합이며, 프로퍼티는 키와 값으로 구성된다.

var idol = {
    name: 'SVT',
    count: 13
};

var testObj = {
    normal: 'normal value',
    '@ s p a c e @': 'space value',   // 권장x
    '': '',  // 권장x
    0: 1,    // 내부적으로 문자열 변환
    var: 'var',  // 권장x
    normal: 'new normal value'
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
}
console.log(product)

var product2 = { productName, price }
console.log(product2)