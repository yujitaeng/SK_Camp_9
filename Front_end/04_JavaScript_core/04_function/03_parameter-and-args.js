/* 매개변수와 인자 */

function lunch(menu) {
    // function lunch(...menu) 가변인자 사용
    console.log(menu);
    console.log(arguments);
    return `오늘 점심은 ${menu}로 정했다!`;
}

console.log(lunch('김밥'));
// console.log(menu);   // 파라미터는 함수 내부에서만 사용 가능
console.log(lunch());   // 인자가 부족해서 할당되지 않으면 undefined
console.log(lunch('닭볶음탕', '김밥', '돼지짜글이'));

function dance(danceName = '마카레나') {

    // 인자 검증
    // 1. 인자는 1개만 받아야 함
    if (arguments.length > 1) {
        throw new Error('인자는 1개만 받아야 합니다!');
    }
    
    // 2. 인자의 타입은 문자열이어야 함
    if (typeof danceName !== 'string') {
        throw new TypeError('인자는 문자열이어야 합니다!');
    }

    // 3. 빈 문자열이면 안됨
    if (danceName.trim() === '') {
        throw new Error('빈 문자열은 허용되지 않습니다!');
    }

    // throw new TypeError('잘못된 인자로 인한 에러!');
    
    return `${danceName} 춤추기 시작!`;
}

result = dance();
console.log(result);