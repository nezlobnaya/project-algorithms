/*Write a function `canSum(targetSum, numbers)` that takes in a targetSum 
and an array of numbers as arguments
The function should return a boolean indication whether or 
not it is possible to generate the targetSum using numbers from the array*/

// const canSum = (targetSum, numbers) => {
//     if (targetSum === 0) return true;
//     if (targetSum < 0) return false;
    
//     for (let num of numbers) {
//         const remainder = targetSum - num;
//         if (canSum(remainder, numbers) === true) {
//             return true;
//         }

//     }
//     return false;
// }

// const canSum = (targetSum, numbers, memo={}) => {
//     if (targetSum in memo) return memo[targetSum];
//     if (targetSum === 0) return true;
//     if (targetSum < 0) return false;
    
//     for (let num of numbers) {
//         const remainder = targetSum - num;
//         if (canSum(remainder, numbers, memo) === true) {
//             memo[targetSum] = true;
//             return true;
//         }

//     }
//     memo[targetSum] = false;
//     return false;
// }

// with tabulation:
const canSum = (targetSum, numbers) => {
    const table  = Array(targetSum + 1).fill(false);
    table[0] = true;
    
    for (let i = 0; i <= targetSum; i++) {
        if (table[i] ===true) {
            for (let num of numbers) {
                table[i + num] = true
            }
        }

    }
    return table[targetSum];
}

console.log(canSum(7, [2, 3]));// true
console.log(canSum(7, [5, 3, 4, 7]));// true
console.log(canSum(7, [2, 4]));// false
console.log(canSum(8, [2, 3, 5]));// true
console.log(canSum(300, [7, 14]));// false

//Time/Space
// brute force recursion: O(n^m)time  O(m) space

// memoized O(m*n)time O(m) space
