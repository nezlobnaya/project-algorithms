/*

Write a function `countConstruct(target, wordBank)` that accepts a target string and an array of strings.

The function should return the number of ways that the `target` can be constructed concatenating elements of the `wordBank` array.

You may reuse elements of `wordBank` as many times as needed.

*/

// const countConstruct = (target, wordBank) => {
//     if (target === "") return 1;
//     let totalCount = 0;

//     for (let word of wordBank) {
//         if (target.indexOf(word) === 0) {
//             const numWaysForRest = countConstruct(target.slice(word.length) , wordBank);
//             totalCount += numWaysForRest;
//         }
//     }
//     return totalCount;
// }

// const countConstruct = (target, wordBank, memo={}) => {
//     if (target in memo) return memo[target]
//     if (target === "") return 1;
//     let totalCount = 0;

//     for (let word of wordBank) {
//         if (target.indexOf(word) === 0) {
//             const numWaysForRest = countConstruct(target.slice(word.length) , wordBank, memo);
//             totalCount += numWaysFor Rest;
//         }
//     }
//     memo[target] = totalCount;
//     return totalCount;
// }


//tabulation
const countConstruct = (target, wordBank) => {
    const table = Array(target.length + 1).fill(0);
    table[0] = 1;

    for (let i = 0; i <= target.length; i++) {     
            for (let word of wordBank) {
                if (target.slice(i, i + word.length) === word) {
                    table[i + word.length] += table[i]
            }
        }
    
  }
    return table[target.length];
}



console.log(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]));//2
console.log(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));//1
console.log(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]));//0
console.log(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]));//4
console.log(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
]));//0

//Time complexity
//brute force O(n^m*m)
//memoize O(n*m^2)

//Space complexity 
//brute force O(m^2)
//memoize O(m^2)

//Tabulation
//Time complexity
// O(m^2*n)
//Space complexity 
//O(m)