/*
write a function `canConstruct(target, wordBank) `hat accepts a taget string and an array of strings.

The function should return a boolean indicating whether or not the `target` can be constructed 

by concatenating elements  of the `wordBank` array.

You may reuse elememts of `wordBank` as many times as needed.


*/

// const canConstruct = (target, wordBank) => {
//     if (target === "") return true;

//     for (let word of wordBank) {
//         if (target.indexOf(word) === 0) {
//             const suffix = target.slice(word.length);
//             if (canConstruct(suffix , wordBank) === true) {
//                 return true;
//             }
//         }
//     }
//     return false;
// }

// const canConstruct = (target, wordBank, memo={}) => {
//     if (target in memo) return memo[target];
//     if (target === "") return true;

//     for (let word of wordBank) {
//         if (target.indexOf(word) === 0) {
//             const suffix = target.slice(word.length);
//             if (canConstruct(suffix , wordBank, memo) === true) {
//                 memo[target] = true;
//                 return true;
//             }
//         }
//     }
//     memo[target] = false;
//     return false;
// }

const canConstruct = (target, wordBank) => {
    const table = Array(target.length + 1).fill(false);
    table[0] = true;


    for(let i = 0; i<= target.length; i++) {
            if (table[i] === true) {
                for (let word of wordBank) {
                    //if the word matches characters starting at the position i
                    if ( target.slice(i, i + word.length) === word) {
                        table[i + word.length] = true;
                    }
                }
            }
            
        }
        return table[target.length];
    }



console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));// true
console.log(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])); //false
console.log(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]));//true
console.log(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
]));//false

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