/* 엄격 모드 (strict mode) */

/*
    전역 선두 또는 함수의 선두에 'use strict' 작성해 사용한다.
    즉시 실행 함수로 감싼 스크립트 단위로 적용하는 것이 바람직하다.
*/

// 'use strict';

function test() {
    // 'use strict';
    x = 10;
}

test();

console.log(x);

(function() {
    'use strict';
    // 함수 내용
})();
