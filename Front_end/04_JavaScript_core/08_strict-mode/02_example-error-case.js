/* strict mode 활용 */

// 1. 암묵적 전역 방지
(function(){
    // 'use strict';
    x = 1;
    console.log(x);
})();

// 2. 변수, 함수, 매개변수의 삭제 방지
(function(){
    // 'use strict';
    var x = 1;
    delete x;
})();

// 3. 매개변수 이름 중복 방지
(function(){
    // 'use strict';
    function test(x, x) {
        return x + x;
    }

    console.log(test(1, 2));
})();

// 4. with문 사용 방지
(function(){
    // 'use strict';
    with({ x: 1 }) {
        console.log(x);
    }
})();

// 5. 일반 함수에서의 this 사용 제한
// strict mode에서 일반 함수로서 호출한 함수의 this는 undefined에 바인딩된다.
(function(){
    'use strict';

    function test() {
        console.log(this);
    }

    test();
    new test();
})();

// 6. arguments 객체
// strict mode에서는 매개변수에 전달된 인수를 재할당해서 변경해도 arguments 객체에는 반영되지 않는다.
(function(arg){
    'use strict';
    arg = 1;

    console.log(arg);
    console.log(arguments);
})(100);
