/* Write a function `bestSum(targetSum, numbers)` that takes 
in a targetSum and an array of numbers as arguments
The function should return an array containing the shortest 
combination of numbers that add up to exactly the targetSUm
If there is a tie for the shortest combination , 
you may return any one of the shortest
*/

// const bestSum = (targetSum, numbers) => {
//     if (targetSum === 0) return [];
//     if (targetSum < 0) return null;
//     let shortestCombination = null
    
//     for (let num of numbers) {
//         const remainder = targetSum - num;
//         const remainderCombination = bestSum(remainder, numbers);
//         if ( remainderCombination !== null) {
//             const combination = [ ...remainderCombination, num];
//             if (shortestCombination === null || combination.length < shortestCombination.length) {
//                 shortestCombination = combination
//             }
//         }
//     }
//     return shortestCombination;
// }

// const bestSum = (targetSum, numbers, memo={}) => {
//     if (targetSum in memo) return memo[targetSum];
//     if (targetSum === 0) return [];
//     if (targetSum < 0) return null;
//     let shortestCombination = null
    
//     for (let num of numbers) {
//         const remainder = targetSum - num;
//         const remainderCombination = bestSum(remainder, numbers, memo);
//         if ( remainderCombination !== null) {
//             const combination = [ ...remainderCombination, num];
//             if (shortestCombination === null || combination.length < shortestCombination.length) {
//                 shortestCombination = combination
//             }
//         }
//     }
//     memo[targetSum] = shortestCombination;
//     return shortestCombination;
// }

//tabulation

const bestSum = (targetSum, numbers, memo={}) => {
    const table = Array(targetSum + 1).fill(null);
    table[0] = [];

    for (let i = 0; i <= targetSum; i++) {
        if (table[i] !== null) {
            for (let num of numbers) {
                const combination = [ ...table[i], num];
                //if this current combination is shorter that what is already stored
                if (!table[i +num] || table[i + num].length > combination.length) {
                    table[i + num] = combination;
                }
                
            }
        }
    }
    return table[targetSum];
};

console.log(bestSum(7, [5, 3, 4, 7]));// [7]
console.log(bestSum(8, [2, 3, 5]));// [3, 5]
console.log(bestSum(8, [1, 4, 5]));// [4, 4]
console.log(bestSum(100, [1, 2, 5, 25 ]));// [25, 25, 25, 25]

//Time/Space
// brute force recursion: O(n^m * m)time  O(m^2) space

// memoized O(m^2 * n)time O(m^2) space
