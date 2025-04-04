// 줄 주석
/*
구간 주석
*/

/* string */
// 홑따옴표'', 쌍따옴표"", 백틱`` 사용 가능
// 백틱만 표현식 내 개행 가능
var str1 = '다람쥐';
var str2 = "squirrel";
var str3 = `다람쥐
선생님`;

// 문자열 합치기 (다른 자료형 간에서는 암묵적 형변환 일어남)
console.log(str1 + (2 + 3));

// 백틱에서는 ${}를 이용해 변수 사용 가능
var str = `${str1} 선생님의 SKN 9기!`;
console.log(str);