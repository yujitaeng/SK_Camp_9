/* 화살표 함수의 특징 */

// 1. 화살표 함수는 this를 가지지 않는다.
let theater = {
    store: "광화문점",
    titles: ["승부", "미키 17", "로비", "극장판 진격의 거인"],
    showMovieList() {
        this.titles.forEach(
            // title => console.log(this.store + ":" + title)
            function(title) {
                console.log(this.store + ":" + title)
            }
        );
    }
}

theater.showMovieList();

// 2. 화살표 함수는 new와 함께 호출할 수 없다.

// 3. 화살표 함수는 super를 가지지 않는다.

// 4. 화살표 함수는 arguments를 지원하지 않는다.
(function() {
    const arrowFunc = () => console.log(arguments);
    // const arrowFunc = function() {
    //     console.log(arguments);
    // }
    arrowFunc(3, 4);
}(1, 2));