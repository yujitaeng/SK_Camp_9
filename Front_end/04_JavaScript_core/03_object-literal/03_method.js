/* method */
// JS의 함수는 객체이다. (= 값으로 취급할 수 있다.)

var puppy = {
    name: '라떼',
    eat: function(food) {
        console.log(`${this.name}은(는) ${food}를 와구와구 먹는 중`);
    }
}

puppy.eat('최고급 사료');

/* 메소드 단축 */
var puppy2 = {
    name: '밍키',
    eat(food) {
        console.log(`${this.name}은(는) ${food}를 와구와구 먹는 중`)
    }
}

puppy2.eat('소고기, 양념없는 갈비');