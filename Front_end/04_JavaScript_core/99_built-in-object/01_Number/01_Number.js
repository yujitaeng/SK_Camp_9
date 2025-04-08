/* 01. Number */

/* Number 생성자 함수 */
const obj = new Number();       // Number 인스턴스 생성
console.log(obj);               // 인수 전달하지 않을 경우 0을 할당

const obj2 = new Number(1);
console.log(obj2);              // 인수로 전달받은 숫자 할당

const obj3 = new Number('1');
console.log(obj3);              // 인수로 전달받은 문자 숫자로 형변환

const obj4 = new Number('number');
console.log(obj4);              // 숫자 형변환 불가 시 NaN

// new 연산자를 사용하지 않고 호출하면 Number 인스턴스가 아닌 숫자를 반환하므로 명시적 타입 형변환에 활용 가능