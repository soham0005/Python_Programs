function RomanToInteger(s){
    const sym = { 
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };
    let ans = 0;

    for(let i=0; i<s.length;i++){
        let next = sym[s[i+1]];
        let curr = sym[s[i]];

        if(next>curr){
            ans += next-curr
        }
        else{
            ans+=curr;
            i++;
        }
    }
    return ans;
}

let ans = RomanToInteger("LVIII");
console.log(ans);