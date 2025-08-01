function countUniqueVowels(str) {
    const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
    let a = [false, false, false, false, false]
    for(let c of str) {
        if (c == 'a' || c == 'A') {a[0] = true}
        else if (c == 'e' || c == 'E') {a[1] = true}
        else if (c == 'i' || c == 'I') {a[2] = true}
        else if (c == 'o' || c == 'O') {a[3] = true}
        else if (c == 'u' || c == 'U') {a[4] = true}
    }
    let cnt = 0
    for(let b of a) {
        if (b == true) cnt += 1;
    }
    return cnt;
}


function main() {
    const testCases = [
        "Hello",        // 2
        "Education",    // 5
        "Sky",          // 0
        "AEIOUaeiou",   // 5
        "Programming",  // 3
        "bcdxyz"        // 0
    ];

    for (let str of testCases) {
        const result = countUniqueVowels(str);
        console.log(`"${str}" → ${result} unique vowel(s)`);
    }
}


main();