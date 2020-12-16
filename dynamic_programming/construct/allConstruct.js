/*

Write a function `allConstruct(target, wordBank)` that accepts a target string and an array of strings.

The function should return a 2D array containing all of the ways that the `target` can be constructed by concatenating elements of the `wordBank` array.
Each element of the 2D array should represent one combination that constructs the `target`.

You may reuse elements of `wordBank` as many times as needed.

*/

// const allConstruct = (target, wordbank) => {

//     if (target === "") return [[]];
    
//     const result = []
//     for (let word of wordbank) {
//         if (target.indexOf(word) === 0) {
//             const suffix = target.slice(word.length);
//             const suffixWays = allConstruct(suffix, wordbank);
//             const targetWays = suffixWays.map(way => [word, ...way]);
//             result.push(...targetWays);
//         }
//     }
//     return result;
// }


// const allConstruct = (target, wordbank, memo={}) => {
//     if (target in memo) return memo[target];
//     if (target === "") return [[]];
    
//     const result = []
//     for (let word of wordbank) {
//         if (target.indexOf(word) === 0) {
//             const suffix = target.slice(word.length);
//             const suffixWays = allConstruct(suffix, wordbank, memo);
//             const targetWays = suffixWays.map(way => [word, ...way]);
//             result.push(...targetWays);
//         }
//     }
//     memo[target] = result;
//     return result;
// }

const allConstruct = (target, wordBank) => {
    const table = Array(target.length + 1)
        .fill()
        .map(() => []);
    table[0] = [[]];
    
    for (let i = 0; i <= target.length; i++) {     
        for (let word of wordBank) {
            if (target.slice(i, i + word.length) === word) {
                const newCombinations = table[i].map(subArray => [ ...subArray, word]);
                table[i + word.length].push(...newCombinations);
        }
      }
    }
    return table[target.length];
}

console.log(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]));
// [ 
//     [ 'purp', 'le' ], 
//     [ 'p', 'ur', 'p', 'le' ]
//  ]
console.log(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]));
// [ [ 'ab', 'cd', 'ef' ],
//   [ 'ab', 'c', 'def' ],
//   [ 'abc', 'def' ],
//   [ 'abcd', 'ef' ] ]

console.log(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]));//[]
console.log(allConstruct("aaaaaaaaaaaaaaaaz", [
    "a",
    "aa",
    "aaa",
    "aaaa",
    "aaaaa",
]));//[]

// m = target.length
//n = wordbank.length

//Time complexity
//brute force O(n^m)
//memoize O(m)

//Space complexity 
//brute force O(m)
//memoize O(m)

//Tabulation
//Time complexity
// O(n^m)
//Space complexity 
//O(n^m)
