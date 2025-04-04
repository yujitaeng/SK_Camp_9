/* object */

var teacher = {
    // 프로퍼티티
    name: '강아지',
    team: 'helloworldlabs',
    //메소드
    getInfo: function() {
        return `${this.name}은(는) ${this.team} 소속의 선생님입니다.`
    }
};

console.log(teacher)
console.log(typeof teacher)