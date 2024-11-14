/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let count = {};
    for(let num of nums)
        count[num] = count[num] ? ++count[num] : 1;
    
    let i = 0;
    while(count[0] > 0) {nums[i] = 0; count[0] = --count[0]; ++i};
    while(count[1] > 0) {nums[i] = 1; count[1] = --count[1]; ++i};
    while(count[2] > 0) {nums[i] = 2; count[2] = --count[2]; ++i};
};
