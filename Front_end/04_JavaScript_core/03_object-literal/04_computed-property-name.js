/* 계산된 프로퍼티 이름 */

var prefix = "B";
var index = 1;

var boardObj = {};

boardObj[prefix + '-' + index++] = "Board 1";
boardObj[prefix + '-' + index++] = "Board 2";
boardObj[prefix + '-' + index++] = "Board 3";

console.log(boardObj)

/* ES6 */
var boardObj2 = {
    [`${prefix}-${index++}`]: "Board 4",
    [`${prefix}-${index++}`]: "Board 5",
    [`${prefix}-${index++}`]: "Board 6"
}
console.log(boardObj2)